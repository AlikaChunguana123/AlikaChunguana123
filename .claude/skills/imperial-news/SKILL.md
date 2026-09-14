---
name: imperial-news
description: |
  Skill de post-notícia do sistema Imperium. A mentorada pede "card de notícia" ou
  "reel de notícia" e a skill faz tudo: acha notícia ATUAL e VERIFICADA no nicho dela,
  aplica os 4 testes anti-notícia-reciclada, monta card 3:4 (1080×1440) ou reel 9:16
  de 7 segundos (Veo + ffmpeg) com a identidade visual DELA, + legenda + hashtags
  dentro das regras de publicidade da profissão dela. Primeira execução: setup único
  que monta o mapa de fontes do nicho. Triggers: "/imperial-news", "notícia do dia",
  "card de notícia", "reel de notícia", "post de notícia", "faz a notícia de hoje",
  "transforma essa notícia em post".
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch
---

# Imperial News

1 pedido → 1 notícia verificada do nicho da mentorada → card 3:4 **ou** reel de 7s,
com a identidade visual dela, legenda e hashtags. Pronto pra revisar e postar.

> Nasceu de um piloto real (16/07/2026, perfil de advocacia previdenciária): no mesmo
> dia em que dezenas de portais empurravam como "notícia" uma pauta de 2025 reciclada,
> o processo desta skill pegou a armadilha antes de publicar. A verificação não é
> burocracia — é o produto.

---

## ARQUIVOS POR MENTORADA (no projeto dela)

| Arquivo | O que é |
|---|---|
| `contexto/imperial-news.config.md` | Perfil: nicho, leitor, marca, paleta, fontes, regras da profissão (criado na 1ª execução) |
| `conteudo/_rotina/estado-news.json` | Alternância card/reel + pautas dos últimos 30 dias |
| `conteudo/posts/AAAA-MM-DD-slug/` | Cards entregues |
| `conteudo/reels/AAAA-MM-DD-slug/` | Reels entregues |

---

## ETAPA 0 — Setup (só na primeira execução)

Se `contexto/imperial-news.config.md` **não existe**:

1. **Antes de perguntar, leia `contexto/` inteiro** (Glob `contexto/**`). O passaporte-imperial
   e outras skills podem já ter marca, voz, paleta e nicho. Só pergunte o que faltar.

2. **Entrevista única** (tudo numa mensagem só):
   - **Nicho** e **leitor final** — quem é o cliente final? (nunca o colega de profissão)
   - **Handle** + **nome da marca** + **monograma** (1 letra)
   - **Cor primária HEX** (sem resposta → mantém o carmim `#B83A2E` default)
   - **Profissão regulamentada?** (advocacia/OAB, medicina/CFM, psicologia/CRP,
     nutrição/CFN, mercado financeiro/CVM…) — define as regras da legenda
   - **Ferramenta de imagem do card** — a escolha é DELA (detalhes e receitas em
     `references/geracao-imagem.md`):
     - **Nano Banana no Vertex** (`gemini-2.5-flash-image`) — recomendada: mesma
       conta Google do Veo, ~US$0,04/imagem, sem fila
     - **Higgsfield** (`soul_2`) — se ela tem conta/créditos
     - **Outra ferramenta MCP** que ela tenha conectada
     - **Fotos próprias / banco de imagens**
     - **Sem foto** (fundo sólido)
     Grave a preferida + a ordem de fallback no config (`imagem.preferida`, `imagem.fallback`).
   - **Vai querer reel?** Se sim: tem conta Google Cloud com a Avaliação Gratuita de
     US$300 ativa? (setup na skill `criar-videos-vertex-veo`, Passo 1 — a mesma conta
     serve pro Nano Banana do card)

3. **Monte o mapa de fontes do nicho** (WebSearch): 5-8 fontes oficiais/primárias
   (órgãos, tribunais, agências públicas do setor), imprensa que cita fonte primária,
   e candidatas a blacklist. Siga os critérios de `references/verificacao.md`.
   **Mostre pra ela aprovar antes de gravar.**

4. **Se profissão regulamentada:** pesquise as regras de publicidade da categoria e
   resuma no config, com o número do ato. Exemplo verificado: advocacia → Provimento
   OAB 205/2021 (sem promessa de resultado, sem captação, fecho "consulte um advogado
   de sua confiança").

5. Grave `contexto/imperial-news.config.md` e crie `conteudo/_rotina/estado-news.json`:
   ```json
   {
     "ultimo_formato": null,
     "ultima_execucao": null,
     "pautas_recentes": []
   }
   ```

Nas execuções seguintes: leia o config e o estado e vá direto pra Etapa 1.

---

## ETAPA 1 — O pedido

Ela diz **"card"** ou **"reel"**. Se não disser, olhe `ultimo_formato` no estado e
proponha o outro (alternância por estado, não por data — sobrevive a dias pulados).

---

## ETAPA 2 — Achar e VERIFICAR a pauta

Leia `references/verificacao.md` e siga à risca:

- Busque notícia dos **últimos 3 dias** nas fontes do config. Nunca na blacklist.
- Aplique os **4 testes** em toda candidata: (1) ano na URL, (2) dia da semana,
  (3) prazo vivo, (4) ação do leitor. Reprovou em um → descarta.
- Não repita pauta de `pautas_recentes` (30 dias).
- Prefira pauta em que o leitor tem algo a **fazer** sobre pauta institucional.

**Sem pauta fresca que passe nos 4 testes?** Entregue a melhor pauta perene verificada
do nicho — mas obrigatoriamente:
- Peça **SEM tarja de data**, enquadrada como conteúdo educativo.
- Avise em negrito na entrega: **"Sem pauta nova hoje — isto é conteúdo perene."**
  e liste o que descartou e por quê.
- **NUNCA apresente pauta velha como fresca.** Essa trava é inegociável.

---

## ETAPA 3 — CHECKPOINT (obrigatório antes de renderizar)

Mostre: manchete + accent, linha fina, fonte + data de publicação, legenda completa,
hashtags. Só avance com **"aprova"**. Iterar texto é barato; render e vídeo são caros.

---

## ETAPA 4A — CARD (1080×1440, 3:4)

1. Copie `references/templates/card-noticia.template.html` + `styles/` pra
   `conteudo/posts/AAAA-MM-DD-slug/`.
2. **Paleta dela:** substitua `--carmin` no `:root` dos DOIS css pela cor primária
   do config. (Os tokens `--cream`/`--ink` só mudam se a marca pedir.)
3. **Foto de fundo — pela ferramenta que ELA escolheu no config.** Leia
   `references/geracao-imagem.md` e siga a receita da preferida dela (Nano Banana no
   Vertex / Higgsfield / outra MCP / foto própria / banco / sem foto), com a escada
   de fallback do config. Regras universais de lá, pra qualquer ferramenta:
   - Cena documental **genérica** do tema — nunca fingindo retratar o fato real —,
     sem texto legível, espaço negativo no terço superior (o scrim cobre o rabisco).
   - Foto de IA ou de banco → selo **"Imagem ilustrativa"** SEMPRE.
   - **Olhe a imagem** (Read) antes de aplicar no card.
   - Último recurso: card **sem foto** (remova o `background-image` e a div do selo)
     — fundo escuro sólido é válido. Avise qual degrau falhou.
4. Preencha os placeholders. O `{{ACCENT}}` é o número/termo de impacto — **curto
   (1-3 palavras)**, senão estoura a caixa.
5. Renderize com Chrome headless — **o `--screenshot` exige caminho ABSOLUTO no
   Windows** (relativo devolve "Acesso negado"), e a URL `file:///` leva `%20` nos espaços:
   ```
   "C:\Program Files\Google\Chrome\Application\chrome.exe" --headless --disable-gpu
     --hide-scrollbars "--screenshot=<ABSOLUTO>\post.png" --window-size=1080,1440
     --virtual-time-budget=10000 --force-device-scale-factor=1 "file:///<caminho-com-%20>"
   ```
   (Mac: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`.)
6. **Leia o PNG** e confira antes de entregar (manchete dentro do box, rabisco de IA
   invisível sob o scrim). Se ela quiser 4:5 (1080×1350), remova a classe `r3x4` do
   `<html>` e re-renderize com `--window-size=1080,1350`.

---

## ETAPA 4B — REEL (1080×1920, 7s)

**Cheque os pré-requisitos ANTES de prometer o reel:**
- `gcloud auth print-access-token` devolve token? (senão → skill `criar-videos-vertex-veo`, Passo 1)
- ffmpeg existe? (senão → `winget install Gyan.FFmpeg`)

Depois siga **`references/pipeline-reel.md` à risca** — cada aviso ali custou tempo
real no piloto. Resumo do fluxo: Veo 3 Fast gera B-roll de 8s (~US$1,20 do trial dela)
→ overlay de texto vira PNG transparente via Chrome → ffmpeg escala, compõe e corta
pra 7s exatos.

Regra de ouro do texto: manchete de **3-6 palavras** + sub de 1-2 linhas, no template
`references/templates/reel-overlay.template.html`. **NUNCA peça texto ao Veo** — IA de
vídeo escreve rabisco.

---

## ETAPA 5 — Legenda, entrega e estado

**Legenda:** hook (1-2 linhas) + desenvolvimento com os dados verificados (3-5 linhas)
+ orientação prática (canal oficial de consulta do nicho). **Regras de publicidade do
config são inegociáveis** — sem promessa de resultado, sem captação, sem sensacionalismo.
Fecho padrão: *"consulte um(a) [profissional da categoria] de sua confiança"* — nunca
"chama no direct". 8-12 hashtags do nicho.

**Entrega:** arquivo + pauta (fonte, data, como passou nos 4 testes) + legenda +
hashtags + avisos (pauta perene, crédito acabando, fonte oficial fora do ar).
**Nada é publicado automaticamente** — ela revisa e posta.

**Estado:** atualize `estado-news.json` (`ultimo_formato`, `ultima_execucao`, adicione
a pauta em `pautas_recentes` e pode a lista em 30 dias).

---

## ROTINA DIÁRIA (opcional — ofereça no final da primeira entrega)

Se ela quiser receber todo dia útil às 10h sem pedir: crie uma tarefa agendada
(app desktop, cron `0 10 * * 1-5`) com prompt **auto-contido** apontando pro config e
estado DELA, alternância por estado. Avise: a tarefa roda com o app aberto, e a
primeira execução deve ser manual ("Run now") pra pré-aprovar as permissões.
Se o ambiente não tiver tarefas agendadas, ensine: "roda `/imperial-news` toda manhã".

---

## REGRAS DE OURO

1. **Verificação vem antes de estética.** Post errado assinado pela marca custa mais
   que um dia sem post.
2. **Pauta velha nunca vira "notícia de hoje".** Perene = sem tarja de data.
3. **Selo "Imagem ilustrativa"** sempre que a imagem não for real.
4. **Checkpoint antes de qualquer render.**
5. **Accent curto** (1-3 palavras); no reel, com `white-space: nowrap` e `&nbsp;`
   entre número e palavra (senão quebra em duas caixas e parece bug).
6. **O leitor é o cliente final do nicho** — não o colega de profissão.
7. **Tempo esperado:** card < 15 min; reel pode levar ~1h (a fila do Veo já chegou a
   45 min — é fila, não erro).
