# Pipeline do reel — Veo (Vertex AI) + ffmpeg

Validado em produção em 16/07/2026. Siga na ordem. **Cada aviso ⚠️ aqui custou tempo
real numa execução de verdade — não "simplifique" nenhum.**

Comandos em PowerShell/Windows. Mac: adapte pra bash e troque os caminhos de binário.

---

## 0. Pré-requisitos (cheque ANTES de prometer o reel)

- **gcloud** em `%LOCALAPPDATA%\GoogleCloudSDK\google-cloud-sdk\bin\gcloud.cmd`
  (setup: skill `criar-videos-vertex-veo`, Passo 1 — a mentorada usa a própria conta
  Google com a Avaliação Gratuita de US$300).
- `gcloud auth print-access-token` devolve token; `gcloud config get-value project`
  devolve o projeto DELA.
- **ffmpeg**: `winget install Gyan.FFmpeg` → binário em
  `%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_*\ffmpeg-*\bin\ffmpeg.exe`
  (após instalar, o PATH só vale em shell novo — use o caminho absoluto).
- **Custo:** ~US$1,20/vídeo no Veo 3 Fast (o trial de US$300 cobre ~250 vídeos).
- Billing sem instalar componente `beta` do gcloud:
  `curl.exe -s "https://cloudbilling.googleapis.com/v1/projects/<PROJ>/billingInfo" -H "Authorization: Bearer <TOKEN>"`
  → precisa de `"billingEnabled": true`.
- **Modelos:** confirme acesso com um POST de corpo vazio — HTTP **400 "Empty
  instances"** = modelo liberado; HTTP **404** = não existe nesse projeto.
  Padrão: `veo-3.0-fast-generate-001`. (No projeto do piloto, Imagen dava 404 —
  cheque antes de prometer imagem via Vertex.)

## 1. Submeter o B-roll (8s, 9:16, sem áudio)

Prompt: cena documental **genérica** do tema; SEM texto legível em qualquer
superfície; sem pessoa falando pra câmera; movimento lento; **luz generosa**
("warm natural light", "bright", nunca "dark moody" — o scrim do overlay já escurece
por cima); terminar com "no text, no logos, no watermark, vertical 9:16".

```powershell
$dir  = "<PASTA DO REEL>"
$g    = "$env:LOCALAPPDATA\GoogleCloudSDK\google-cloud-sdk\bin\gcloud.cmd"
$t    = & $g auth print-access-token
$proj = (& $g config get-value project)
$payload = @{ instances = @(@{ prompt = "<PROMPT>" }); parameters = @{ aspectRatio = "9:16"; durationSeconds = 8; generateAudio = $false } } | ConvertTo-Json -Depth 6 -Compress
[System.IO.File]::WriteAllText("$dir\veo-req.json", $payload, (New-Object System.Text.UTF8Encoding $false))
$url = "https://us-central1-aiplatform.googleapis.com/v1/projects/$proj/locations/us-central1/publishers/google/models/veo-3.0-fast-generate-001:predictLongRunning"
$r = (curl.exe -s -X POST $url -H "Authorization: Bearer $t" -H "Content-Type: application/json" -H "Expect:" --data-binary "@$dir\veo-req.json") -join ""
if ($r -match '"name":\s*"([^"]+)"') { $Matches[1] | Out-File "$dir\operation.txt" -Encoding ascii -NoNewline }
```

⚠️ **Use `curl.exe`, nunca `Invoke-RestMethod`** — PowerShell 5.1 dá erro de TLS e
HTTP 417. Header `Expect:` vazio, body via `--data-binary "@arquivo"` em UTF-8 **sem BOM**.

## 2. Acompanhar — com PACIÊNCIA

⚠️ **`Get-Content -Raw` NÃO devolve string pura.** Devolve string decorada com
`PSPath`/`PSProvider`/`PSDrive`; no `ConvertTo-Json` vira um objeto inteiro e o Vertex
responde `Invalid value (operation_name), Starting an object on a scalar field`. Faça:

```powershell
$op   = [System.IO.File]::ReadAllText("$dir\operation.txt").Trim()
$body = '{"operationName":"' + $op + '"}'
[System.IO.File]::WriteAllText("$dir\fetch.json", $body, (New-Object System.Text.UTF8Encoding $false))
$url = "https://us-central1-aiplatform.googleapis.com/v1/projects/$proj/locations/us-central1/publishers/google/models/veo-3.0-fast-generate-001:fetchPredictOperation"
$r = (curl.exe -s -X POST $url -H "Authorization: Bearer $t" -H "Content-Type: application/json" -H "Expect:" --data-binary "@$dir\fetch.json") -join ""
```

⚠️ **O job pode levar 45+ minutos** (fila), não os "1-3 min" da documentação.
Enquanto a resposta for só `{"name": ...}` sem `error` nem `raiFilteredReason`, está
vivo — espere em blocos de 5-7 min (`sleep` em background), sem polling agressivo.
Se vier `raiFilteredReason`: o filtro de conteúdo derrubou o prompt — reescreva a cena
mais neutra e re-submeta.

## 3. Salvar e conferir

```powershell
$j = $r | ConvertFrom-Json
[System.IO.File]::WriteAllBytes("$dir\veo.mp4", [System.Convert]::FromBase64String($j.response.videos[0].bytesBase64Encoded))
```

⚠️ **O ffprobe vai mostrar 720×1280 — é o normal do Veo Fast, NÃO é erro.** A escala
pra 1080×1920 acontece na composição (passo 5).

Extraia 1 frame e **olhe**: `ffmpeg -ss 4 -i veo.mp4 -frames:v 1 -y frame-check.png`.
Sem texto-rabisco visível? Cena casa com a pauta?

## 4. Overlay de texto (HTML → PNG transparente)

Use `templates/reel-overlay.template.html` (placeholders documentados nele).

```
chrome --headless --disable-gpu --hide-scrollbars --default-background-color=00000000
  "--screenshot=<CAMINHO ABSOLUTO>\texto.png" --window-size=1080,1920
  --virtual-time-budget=10000 --force-device-scale-factor=1 "file:///<url com %20>"
```

⚠️ Caminho **absoluto** no `--screenshot` (relativo = "Acesso negado" no Windows).
Confira o PNG: deve ser RGBA, accent numa caixa só, nada estourando.

## 5. Compor (escala + overlay + corte 7s) — comando exato validado

```
ffmpeg -i veo.mp4 -i texto.png \
  -filter_complex "[0:v]scale=1080:1920:flags=lanczos[bg];[bg][1:v]overlay=0:0:format=auto[v]" \
  -map "[v]" -t 7 -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart -y reel.mp4
```

`ffprobe` deve dar exatamente `1080×1920` e `duration=7.000000`.

## 6. Verificação final

Extraia um frame do meio do `reel.mp4` e **leia a imagem**: texto legível, overlay
alinhado, scrim funcionando. Só então entregue. Limpe os temporários
(`veo-req.json`, `fetch.json`, `operation.txt`, `frame-check.png`).
