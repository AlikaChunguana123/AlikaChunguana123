---
name: criar-personagem-higgsfield
description: >-
  Cria uma personagem de IA fotorrealista com rosto 100% consistente usando o MCP do Higgsfield
  (Soul 2.0 para o rosto-base + Element + Nano Banana Pro para os cenários). Use SEMPRE que o
  usuário quiser criar um personagem/persona/avatar de IA, gerar "a mesma pessoa" em vários
  cenários diferentes, criar uma figura recorrente para conteúdo, ou precisar de imagens de
  referência consistentes que depois virarão vídeos. Triggers: "criar personagem", "cria uma
  persona", "gerar um avatar", "a mesma pessoa em vários cenários", "personagem consistente",
  "personagem para meus vídeos", "/criar-personagem-higgsfield". Mesmo que o usuário não diga
  "Higgsfield", se ele quer uma personagem visual consistente, use esta skill.
---

# Criar Personagem (Higgsfield)

Esta skill cria uma personagem de IA com **rosto idêntico em qualquer cenário** e salva a referência
para reuso (inclusive nos vídeos da skill `criar-videos-vertex-veo`).

A lógica central é simples: gere **um** rosto perfeito uma vez, transforme-o num **Element** reutilizável,
e depois coloque esse Element em quantos cenários quiser. É isso que garante consistência — em vez de
torcer pra cada geração sair parecida.

## Pré-requisito
O **MCP do Higgsfield** precisa estar conectado (server cujas ferramentas incluem `generate_image`,
`show_reference_elements`, `job_display`, `balance`, `models_explore`). Se as ferramentas não
aparecerem, peça ao usuário para conectar em `https://mcp.higgsfield.ai/mcp` (Configurações →
Conectores) e **reiniciar o Claude**. Cheque o saldo com `balance` antes de gerar (imagens custam ~1 crédito).

## Fluxo

### Passo 1 — Montar o "DNA" da personagem
Pergunte ao usuário (ou extraia do pedido) os traços e monte um bloco descritivo em **inglês** — ele
será reusado IGUAL em todas as cenas. Só o cenário ao redor muda. Template:

```
A [idade]-year-old [nacionalidade] [classe/contexto] woman/man, [tom de pele] skin with natural texture,
[cabelo: cor, comprimento, corte], [olhos], [expressão], no makeup, no jewelry, wearing [roupa simples e cor].
Photorealistic, natural skin detail, soft realistic lighting.
```

### Passo 2 — Gerar a Cena 1 (o rosto-base) no Soul 2.0
Chame `generate_image` com:
- `model: "soul_2"`, `aspect_ratio: "9:16"`, `quality: "2k"`, `count: 1` (ou 2 para dar opções)
- `prompt`: o DNA + o primeiro cenário (ex.: interior de casa simples, luz natural).

Acompanhe com `job_display` até `status: "completed"`. Mostre ao usuário e **espere a aprovação do rosto**
antes de seguir — esse é o rosto oficial. Guarde o `job_id` (é o id da imagem).

### Passo 3 — Salvar como Element
Chame `show_reference_elements` com `action: "create"`, um `name` curto, `category: "character"`, e
`medias: [{ id: "<job_id da Cena 1>", type: "image_job", url: "<rawUrl da Cena 1>" }]`.
Guarde o `element_id` retornado — é a chave da consistência e deve ser anotado para reuso futuro.

### Passo 4 — Gerar os outros cenários (Nano Banana Pro + Element)
Para cada cenário novo, chame `generate_image` com:
- `model: "nano_banana_2"`, `aspect_ratio: "9:16"`, `resolution: "2k"`
- `prompt`: embuta o Element com a sintaxe `<<<element_id>>>`, assim:

```
Photorealistic full vertical photo of <<<ELEMENT_ID>>>, the same [descrição curta da personagem],
standing [CENÁRIO NOVO em inglês]. She/He keeps the exact same face and identity.
Candid documentary photo, realistic skin texture.
```

Acompanhe com `job_display`, baixe os arquivos (use os `rawUrl`) para a pasta `personagem/` do projeto.

### Passo 5 — Salvar a referência
Registre na memória/projeto: o `element_id`, o `seed` da Cena 1, e os caminhos das imagens. É isso que
permite reusar a MESMA personagem em sessões futuras e na skill de vídeos.

## ⚠️ Armadilha crítica (não ignore)
O **`soul_2` com imagem de referência liga um "enhancer" automático que REESCREVE o prompt**, descrevendo
a foto de referência em vez do cenário novo — ele troca cenário, etnia, adiciona acessórios. Não dá para
desligar (`enhance_prompt:false` é ignorado). **Por isso a Cena 1 é text-only no Soul, e todas as cenas
seguintes usam `nano_banana_2` + Element**, que respeita o cenário descrito e mantém o rosto.

## Boas práticas
- Sempre **gere 1 e aprove o rosto** antes de produzir o resto — evita desperdício de créditos.
- O Higgsfield gratuito faz imagens, mas **não faz vídeo**. Para vídeo, use a skill `criar-videos-vertex-veo`.
- Veja `personagem/` neste projeto para um exemplo real (cena1_casa.png, cena2_inss.png, cena3_rua.png).
