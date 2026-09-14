---
name: criar-videos-vertex-veo
description: >-
  Gera vídeos verticais 9:16 com áudio de uma personagem falando, em escala, usando o Veo no Google
  Vertex AI (cobertos pela Avaliação Gratuita de US$300 do Google). Use SEMPRE que o usuário quiser
  transformar roteiros/falas em vídeos com uma personagem, gerar vários vídeos de uma vez, criar
  vídeos UGC/avatar falando com IA, animar uma imagem de personagem com fala, ou usar Veo/Vertex.
  Triggers: "gerar os vídeos", "criar vídeos com a personagem", "vídeos em escala", "vídeo da
  personagem falando", "transforma esses roteiros em vídeo", "Veo", "Vertex", "/criar-videos-vertex-veo".
  Use junto com a personagem criada pela skill criar-personagem-higgsfield.
---

# Criar Vídeos (Vertex / Veo)

Esta skill transforma **roteiros de fala + imagens da personagem** em vídeos 9:16 com áudio, usando o
Veo no Vertex AI. O segredo da consistência é **image-to-video**: cada imagem da personagem vira o
**primeiro quadro** do vídeo, então o rosto é literalmente o dela e o cenário varia conforme a imagem escolhida.

Roda no Windows (PowerShell). Os scripts auxiliares estão em `scripts/`.

**Funciona para qualquer nicho e idioma.** A personagem, o idioma e as falas são todos configuráveis
(`-SpeakerDesc`, `-Language`, e a `line` de cada roteiro) — nada é amarrado a um nicho específico. O
exemplo de advocacia em `personagem/` é só ilustrativo.

## Passo 1 — Garantir o setup do Vertex (uma vez)
Verifique se o `gcloud` existe em `%LOCALAPPDATA%\GoogleCloudSDK\google-cloud-sdk\bin\gcloud.cmd`.
Se não existir, rode `scripts/setup_vertex.ps1` — ele baixa/instala o Google Cloud SDK, inicia o
**login no navegador** (o usuário faz o login; o Claude nunca vê a senha), define o projeto e liga a
API `aiplatform.googleapis.com`. Pré-requisito do usuário: ter uma conta Google Cloud com a
**Avaliação Gratuita (US$300)** ativada em console.cloud.google.com.

Confirme o setup rodando `gcloud auth print-access-token` (deve devolver um token) e `gcloud config get-value project`.

## Passo 2 — Preparar o manifesto dos vídeos
Monte um JSON (modelo em `references/manifest-exemplo.json`) com um item por vídeo:
```json
{ "id": "V01", "scene": "casa", "hook": "rótulo curto", "line": "Fala em português COM ACENTOS" }
```
- `scene` mapeia para um arquivo de imagem (ex.: `casa` → `cena1_casa.png`) que será o primeiro quadro.
- `line` é a fala — **mantenha os acentos** (ç, ã, á…), senão a pronúncia sai errada.

## Passo 3 — Gerar 1 vídeo de teste ANTES do lote
Sempre valide rosto + pronúncia com um único vídeo antes de gastar créditos no lote inteiro. Use o
mesmo `scripts/generate_videos.ps1` com um manifesto de 1 item.

## Passo 4 — Gerar todos
Rode `scripts/generate_videos.ps1` passando: `-Project`, `-ImagesDir`, `-Manifest`, `-OutDir`, e (importante
pra adaptar ao nicho) `-SpeakerDesc` (quem é a personagem) e `-Language` (idioma falado).
Ele submete todos, faz polling e baixa cada `.mp4`. Acompanhe pelo arquivo de status que o script grava.
No fim, liste os resultados por grupo, com o gancho de cada um, e informe o custo (~US$1,20/vídeo no Veo Fast).

## Como a API funciona (referência)
- Token: `gcloud auth print-access-token`
- Enviar: `POST .../publishers/google/models/veo-3.0-fast-generate-001:predictLongRunning`
  body `instances:[{prompt, image:{bytesBase64Encoded, mimeType}}]`, `parameters:{aspectRatio:"9:16", durationSeconds:8, generateAudio:true}`
- Acompanhar: `POST .../veo-3.0-fast-generate-001:fetchPredictOperation` com `{operationName}`
- Resultado: `response.videos[0].bytesBase64Encoded` → decodificar para `.mp4`

Prompt de fala (genérico, serve pra qualquer nicho — o script monta isto automaticamente a partir de
`$SpeakerDesc`, `$Language` e da `line` de cada item):
```
[SpeakerDesc] looks directly into the camera and speaks in warm, natural [Language] with clear, correct
pronunciation, saying: '[FALA COM ACENTOS]' Subtle natural facial movement and lip sync, gentle ambient
sound, candid documentary style, vertical 9:16.
```
Adapte ao nicho da pessoa: `-SpeakerDesc` descreve quem fala (ex.: "a young fitness coach", "um homem de
negócios brasileiro"), `-Language` define o idioma (ex.: "English", "Spanish"). Se um item do manifesto
trouxer um campo `prompt`, o script usa ele inteiro (controle total por vídeo); um campo `speaker`
sobrescreve a descrição só naquele item.

## ⚠️ Armadilhas (já resolvidas nos scripts, mas saiba)
- **Use `curl.exe`, não `Invoke-RestMethod`** — o PowerShell 5.1 dá erro de TLS e 417 (Expectation Failed).
  Os scripts usam curl com header `Expect:` vazio e forçam TLS 1.2.
- **Acentos na fala** — escreva os arquivos em UTF-8 (sem BOM); o script já faz isso.
- **Clipes saem com ~8s** (limite do Veo Fast). Para 10-15s, gere e estenda, ou junte trechos.
- **Plano gratuito do Higgsfield não gera vídeo** — por isso o vídeo é feito no Vertex.

## Exemplo real
Veja `personagem/run40.ps1`, `personagem/videos40.json` e `personagem/videos/` neste projeto — foi assim
que 40 vídeos foram gerados de uma vez.
