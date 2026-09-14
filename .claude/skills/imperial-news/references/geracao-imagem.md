# Geração da foto do card — a mentorada escolhe a ferramenta

A skill NÃO é casada com o Higgsfield. A escolha é da mentorada, feita no setup e
gravada no config (`imagem.preferida` + `imagem.fallback`). Regras que valem pra
**qualquer** ferramenta estão no fim deste arquivo.

O CSS do card usa `background-size: cover` — qualquer proporção razoável funciona,
mas peça 3:4 quando a ferramenta suportar.

---

## OPÇÃO A — Nano Banana no Vertex (`gemini-2.5-flash-image`) — RECOMENDADA

**Por quê:** usa a MESMA conta Google que a mentorada já configurou pro Veo (skill
`criar-videos-vertex-veo`). ~US$0,04/imagem do trial de US$300, **sem fila**, sem
conta extra. Validada em produção em 16/07/2026 (imagem real gerada e conferida).

**Probe de acesso** (POST com body `{}`): HTTP **400** = modelo liberado;
HTTP **404** = não existe nesse projeto. As versões `-preview` costumam dar 404 —
use `gemini-2.5-flash-image` estável.

**Receita (PowerShell, validada):**

```powershell
$g    = "$env:LOCALAPPDATA\GoogleCloudSDK\google-cloud-sdk\bin\gcloud.cmd"
$t    = & $g auth print-access-token
$proj = (& $g config get-value project)
$payload = @{
  contents = @(@{ role = "user"; parts = @(@{ text = "<PROMPT>" }) })
  generationConfig = @{ responseModalities = @("TEXT","IMAGE"); imageConfig = @{ aspectRatio = "3:4" } }
} | ConvertTo-Json -Depth 8 -Compress
[System.IO.File]::WriteAllText("$dir\req.json", $payload, (New-Object System.Text.UTF8Encoding $false))
$url = "https://us-central1-aiplatform.googleapis.com/v1/projects/$proj/locations/us-central1/publishers/google/models/gemini-2.5-flash-image:generateContent"
curl.exe -s -X POST $url -H "Authorization: Bearer $t" -H "Content-Type: application/json" -H "Expect:" --data-binary "@$dir\req.json" -o "$dir\resp.json"
$j = [System.IO.File]::ReadAllText("$dir\resp.json") | ConvertFrom-Json
$part = $j.candidates[0].content.parts | Where-Object { $_.inlineData } | Select-Object -First 1
[System.IO.File]::WriteAllBytes("$dir\photos\foto-capa.png", [System.Convert]::FromBase64String($part.inlineData.data))
```

- ⚠️ `curl.exe` com `Expect:` vazio e JSON em UTF-8 **sem BOM** (mesmas regras do
  pipeline do Veo).
- Sai ~864×1184 (3:4). Abaixo dos 1080×1440 do card, mas o `cover` + scrim escuro
  absorvem bem. Se a mentorada exigir mais resolução, gere e faça upscale.
- A resposta pode trazer um part de texto antes do de imagem — filtre por `inlineData`.

---

## OPÇÃO B — Higgsfield (MCP)

Se a mentorada tem conta Higgsfield conectada:

1. Cheque o saldo com a ferramenta `balance` **testando de verdade** — não conclua
   que está fora do ar só porque o harness lista o servidor como "precisa de OAuth";
   esse aviso já se provou falso em produção (16/07/2026: aviso presente, `balance`
   respondendo normal).
2. Modelo `soul_2`, `aspect_ratio: "3:4"` (~0,12 crédito) — ótimo pra retrato
   editorial. `nano_banana_pro` do Higgsfield custa 2 créditos — só com saldo folgado.
3. Plano free tem fila de 5-10 min (já chegou a mais): aguarde com `sleep` em
   background, sem polling agressivo.

---

## OPÇÃO C — Outra ferramenta de imagem conectada (MCP)

A mentorada pode ter qualquer outro gerador conectado (freepik, recraft, etc.).
Descubra com ToolSearch ("generate image"), confirme custo/parâmetros da ferramenta,
peça 3:4 (ou aceite outra proporção — o `cover` resolve) e salve como
`photos/foto-capa.png`. As regras universais abaixo valem igual.

---

## OPÇÃO D — Foto própria ou banco de imagens

- **Foto própria:** ela indica o arquivo (ensaio, banco pessoal); copie pra
  `photos/foto-capa.png`. Se for foto real dela/do negócio, **sem** selo.
- **Banco livre** (Unsplash/Pexels): licença livre pra uso comercial, sem atribuição
  obrigatória — mas confira a licença da foto específica. Com selo "Imagem ilustrativa".

---

## OPÇÃO E — Sem foto

Remova o `style="background-image:..."` do `<section>` e a div do selo. O card em
fundo escuro sólido é válido — é fallback digno, não gambiarra.

---

## REGRAS UNIVERSAIS — valem pra QUALQUER ferramenta

1. **Cena documental GENÉRICA do tema.** Nunca uma imagem que finja retratar o fato
   noticiado (o evento real, a pessoa real da matéria).
2. **Sem texto legível** no prompt ("no text, no logos, no watermark") — IA escreve
   rabisco em papel/tela/placa. Componha com espaço negativo no terço superior e
   deixe o scrim escuro cobrir as superfícies de texto.
3. **PEÇA FOTO CLARA.** O scrim do card já escurece por cima — se a foto vier escura,
   o resultado é um retângulo preto (aconteceu em produção em 16/07/2026 e o card
   teve que ser refeito). No prompt: "bright", "airy", "abundant natural daylight",
   "luminous", "gentle shadows". NUNCA: "dark moody atmosphere", "deep shadows",
   "penumbra". A foto entra com luz sobrando, não faltando.
4. **Selo "Imagem ilustrativa"** sempre que a imagem for de IA ou de banco.
5. **Olhe a imagem antes de aplicar** (Read no arquivo): rabisco visível? mão com
   6 dedos? cena escura demais? cena que não casa com a pauta? Gere de novo antes
   de renderizar o card.
6. Escada de fallback: preferida do config → fallback do config → sem foto. Nunca
   deixe o card quebrar por causa da foto — e avise qual degrau falhou.
