---
name: imperial-carousel
description: |
  Skill canônica de criação de carrossel Instagram do sistema Imperium. Funciona de
  forma conversacional — pergunta direto no chat o que precisa saber sobre marca, voz,
  oferta E identidade visual. 4 templates editoriais (Editorial Quiet / Minimalist Bold
  / Warm Premium / Native Raw) cobrem qualquer nicho de aluna. Gera 8 slides HTML+CSS premium,
  exporta 8 PNGs 1080×1350 via Chrome headless, + legenda + hashtags + stories.
  Triggers: "/imperial-carousel", "carrossel sobre [tema]", "carrossel pra [oferta]",
  "preciso de carrossel", "post novo de carrossel".
allowed-tools: Read, Write, Glob, Grep, WebSearch, WebFetch, Bash
---

# Imperial Carousel

Carrossel Instagram autoral premium editorial. Copy aterrada em dor/desejo + design
sistema (não Canva genérico) + export PNG pronto pro feed.

> A aluna conversa com você. Você gera 8 PNGs prontos pra postar. Sem fricção.

---

## QUANDO USAR

Use proativamente quando:
- Usuária pede `/imperial-carousel`, "carrossel sobre [X]", "post novo de carrossel"
- A pessoa quer transformar uma frase, ideia ou tema em peça de feed

NÃO use quando:
- Pede roteiro de reel (use `/imperial-reel`)
- Pede post-frase único (use `/imperial-post`)
- Pede plano semanal (use `/imperial-week`)

---

## FLUXO DE EXECUÇÃO

### Etapa 1 — Entrevista única (copy + identidade visual juntos)

Use o que a usuária já mencionou. Pergunte só o que falta. Pra evitar ida-e-volta,
pegue TUDO em uma mensagem só (até 8 itens, agrupados em 2 blocos):

> "Pra gerar carrossel que soa como você E parece sua marca, preciso de 8 coisas
> (responde tudo numa mensagem só):
>
> **SOBRE O CONTEÚDO:**
>
> 1. **Tema** — sobre o que é? (ex: "precificação premium", "5 erros de empresária")
> 2. **Função** — Posicionar (postura), Atrair (alcance), Conversão (vender),
>    Reconectar (intimidade)?
> 3. **Sobre você** — me conta seu negócio em 2 frases (o que vende, pra quem)
> 4. **Voz** — como você descreve seu jeito de falar? Tem palavras-marca que você
>    sempre usa? Palavras que você nunca usa?
>
> **SOBRE A IDENTIDADE VISUAL:**
>
> 5. **Qual estilo bate com sua marca?** Tenho 4 templates calibrados:
>    - **Editorial Quiet** — vibe Vogue, dark plum + dourado, Cormorant italic.
>      Pra mentora premium feminino, advogada, lifestyle alto.
>    - **Minimalist Bold** — vibe NYT Opinion, cream + ink + carmin, Inter Black brutal.
>      Pra tech, marketing moderno, designer, criativa, terapeuta moderna.
>    - **Warm Premium** — vibe Aesop, cream + terra + terracota, Cormorant + Lato.
>      Pra wellness, nutricionista, coach calorosa, beleza, lifestyle warm.
>    - **Native Raw** — vibe photo dump nativo, foto cheia + caixa branca, Arial.
>      Pra conta pessoal, bastidores, creator, quem quer parecer humana e fugir
>      do "cara de anúncio". Depende de fotos fortes.
>
>    (Se não souber, eu sugiro baseado no que você contou em 3 e 4.)
>
> 6. **Cor primária HEX** — me passa 1 cor da sua marca (ex: #1F0D23). Eu derivo
>    a paleta completa a partir dela. Se não tiver, uso o default do estilo.
>
> 7. **Fotos editoriais disponíveis** — onde estão? Idealmente 5 fotos suas:
>    retrato, escritório/decisão, ação/palco, lifestyle/operando, ambiente sofisticado.
>    Se tem menos, me diz quantas. Se não tem, faço só com tipografia.
>
> 8. **Sua assinatura** — nome completo + monograma (1 letra) + sub-marca pro topo
>    (ex: 'Bianca Freitas / B / Mentoria Castle')."

**Importante:** essa entrevista é única. Não pergunte de novo depois. A partir
daqui, vai gerar copy → checkpoint → render.

### Etapa 1.5 — O tema engancha em algo em alta? (PORTÃO CONDICIONAL)

Depois de ler o tema na entrevista, faça **uma checagem rápida** (sem pesquisar ainda):
o tema é, ou pode virar, uma **analogia com algo em alta agora**? Ou seja:

- Filme estreando ou bombando · série recém-lançada com buzz · livro de autora relevante
- Evento cultural (Oscar, Met Gala, Cannes, Copa, premiação do nicho)
- Data comemorativa nos próximos ~14 dias (Dia da Mulher, Dia das Mães, etc.)
- Polêmica/discussão viral do momento que dialogue com a marca
- A própria aluna já pediu o gancho ("aproveita o hype de [X]")

**SE NÃO houver gancho natural com algo em alta** (tema evergreen — "precificação
premium", "5 erros de empresária", "como cobrar mais") → **não force nada.** Siga
direto pro passo 2 (Sugestão de estilo) e toque o fluxo normal.

**SE houver um gancho claro com algo em alta** → **PERGUNTE ANTES de aplicar** (não
decida sozinho). Uma linha só:

> "Teu tema [T] dá um gancho natural com **[algo em alta — ex: a estreia de Wicked]**.
> Quer que eu construa o carrossel usando essa analogia (puxa a atenção pelo assunto
> do momento) ou faço reto, sem analogia?"

- **Se ela disser não** → segue o fluxo normal, sem analogia.
- **Se ela disser sim** → aplique a lógica da skill **`carrossel-zeitgeist-bianca`**
  (a de carrossel por analogia com algo em alta) DENTRO deste fluxo:
  1. **WebSearch pra aterrar o assunto** — no **máximo 2-3 buscas**: cenas/falas
     icônicas, por que está em alta agora, frases marcantes. **Pule a pesquisa** se o
     assunto for óbvio ou a aluna já tiver passado a tese pronta. Nunca invente fato
     sobre o assunto — se não tem certeza, busca ou pergunta.
  2. **Estrutura de copy por analogia** (alimenta a Etapa 4): capa puxando pelo assunto
     do momento (manifesto OU cliffhanger) → setup da leitura óbvia → **cena específica
     do assunto + interpretação não óbvia** → **virada com vocativo direto** ao público
     → (3 sinais ancorados na cena, se couber) → tese/prova → solução → CTA editorial.
  3. O assunto em alta é **porta de entrada, não hook performático** ("tem uma cena que
     vai te chocar" = proibido). A analogia subverte a leitura óbvia.

A `imperial-carousel` continua dona do **visual** (4 templates + render PNG). O que entra
aqui é só a **inteligência de copy por analogia**, e só quando o tema pede E a aluna topa.
Framework completo da analogia: ver a skill `carrossel-zeitgeist-bianca`
(`references/framework.md` dela).

### Sugestão automática de estilo (se a aluna não souber)

Cruze com o que ela contou em "sobre você" + "voz":

| Sinal na conversa | Sugestão |
|---|---|
| Vocabulário: "premium", "imperadora", "categoria", "tese" | Editorial Quiet |
| Vocabulário: "estratégia", "performance", "framework", "dado" | Minimalist Bold |
| Vocabulário: "acolhimento", "cuidado", "jornada", "presença" | Warm Premium |
| Nicho: mentoria premium, advocacia premium, lifestyle alto | Editorial Quiet |
| Nicho: marketing, consultoria tech, design, criativa | Minimalist Bold |
| Nicho: nutrição, wellness, coaching feminino, terapia, beleza | Warm Premium |
| Vocabulário: "real", "sem firula", "na real", "bastidor", "verdade" | Native Raw |
| Nicho/objetivo: conta pessoal, creator, bastidores, alcance orgânico, "sem cara de anúncio" | Native Raw |

Apresente a sugestão + as outras 2 opções pra confirmar.

### Etapa 3 — Aplicar curva por função

Baseado na função declarada, aplique a estrutura de 8 slides (ver `references/framework.md`):

| Função | Curva resumida |
|---|---|
| **Posicionar** | Capa-tese → Setup → Reframe → Aplicação → 3 sinais → Tese-virada → Resultado → CTA |
| **Atrair** | Hook curiosidade → Setup → 5 itens (3-7) → Diferencial → CTA topo |
| **Conversão** | Promessa → Dor → O que é → Como funciona → Prova → Objeção → Escassez → CTA fundo |
| **Reconectar** | Confissão → Setup → Virada → Lição → Aplico hoje → Espelho → Manifesto → CTA suave |

### Etapa 4 — Gerar copy slide a slide

Pra cada slide, monte:

1. **Eyebrow** (3-6 palavras CAPS tracked) — contexto OU pra-quem-é
2. **Headline** (8-15 palavras) — frase-âncora autoral, **dor ou desejo concreto**
3. **Body** (30-60 palavras) — aprofunda com cenas, frases reais de cliente, números
4. **Palavras-chave em `<strong>`** — accent color (champagne dark / terracota cream)
5. **Quote literal entre aspas** quando houver — em Cormorant italic

**Princípios obrigatórios de copy (ver filtro 10):**
- **Sem frase de efeito vazia** — toda headline tem CENA + VERBO TRANSITIVO + objeto específico
- **Sem padrão "X é Y, não Z" abstrato** — refazer como cena concreta
- **Italic só em quotes literais de cliente** — não como decoração tipográfica
- **Negrito em palavras-chave** — não pontilhar negrito por todo lado

### Etapa 5 — Gerar legenda + hashtags + stories

Já gere TUDO (slides + legenda + hashtags + stories) antes do checkpoint, pra a
aluna aprovar o pacote completo de uma vez.

**Legenda:**
```
[Hook — 1-2 linhas, soa como ela]

[Arco — 3-5 linhas resumindo a tese sem entregar tudo]

[CTA — 1-2 linhas conforme etapa]
```

**Hashtags:** 8-12 em uma linha, mistura de nicho-específico + amplas.

**3-5 stories de apoio** (sequência narrativa que conduz ao carrossel):
1. Aquecimento (1 dia antes)
2. Teaser
3. Story do dia do post
4. Aprofundamento
5. CTA reforço

### Etapa 6 — Validar (passar pelos 10 filtros)

Ver `references/filtros.md`. Aplicar TODOS os filtros à copy gerada
(slides + legenda + stories):
1. Palavras vetadas da marca
2. Clichês AI-flavored
3. Padrões anti-IA estruturais
4. Coerência com posicionamento
5. Coerência com cliente ideal
6. Prova/autoridade (se Conversão)
7. CTA específico
8. Densidade textual por slide
9. Consistência de voz entre slides
10. **Anti-frase-de-efeito vazia (CRÍTICO)** — ver lista de padrões em `filtros.md`

Se qualquer filtro falhar, regenere o trecho violador ANTES de mostrar à aluna.

### Etapa 7 — CHECKPOINT: aprovar copy ANTES de renderizar (OBRIGATÓRIO)

**NÃO gere PNG sem antes mostrar a copy à usuária e ter aprovação explícita.**

Renderizar 8 PNGs custa Chrome headless rodando 8x. Iterar texto é barato. Sempre
apresente a copy primeiro em formato legível e peça confirmação.

Apresente assim:

```markdown
## Copy do carrossel: [Tema]

**Função:** [...]  ·  **Estilo visual:** [Editorial Quiet / Minimalist Bold / Warm Premium]
**Paleta:** [cor primária]  ·  **Fotos:** [N fotos disponíveis]

---

### Slide 01 — Capa
**Eyebrow:** [...]
**Headline:** [...]
**Highlight/Body:** [...]

### Slide 02 — Setup
**Eyebrow:** [...]
**Headline:** [...]
**Body:** [...] (palavras-chave em **bold**)

[... 8 slides ...]

---

### Legenda do post
[texto completo com hook + arco + CTA]

### Hashtags (8-12)
#... #... #...

### Stories de apoio (3-5)
1. Aquecimento (1 dia antes): [...]
2. Teaser: [...]
3. Dia do post: [...]
4. Aprofundamento: [...]
5. CTA reforço: [...]

---

**A copy passa? Posso renderizar os PNGs?**

- **"aprova"** → renderizo os 8 PNGs com o template e paleta escolhidos
- **"ajusta slide N"** → refaço só esse slide (eyebrow / headline / body)
- **"muda tom pra [adjetivo]"** → recalibro a voz no carrossel inteiro
- **"outro hook"** → refaço só a capa
- **"troca CTA"** → reformulo o slide 8
- **"regenera tudo"** → ofereço abordagem diferente
- **"muda função pra [X]"** → aplica outra curva
```

**Só depois que a usuária disser "aprova" (ou equivalente), avance pra Etapa 8.**

Se ela pedir ajuste, refaça e mostre de novo. Itere até ter aprovação. Esse loop
é barato (só texto). Sem aprovação, sem render.

---

### Etapa 8 — Gerar HTML usando o template escolhido

Pegue o template correspondente em `references/templates/[ESTILO]/`:

```
references/templates/
├── editorial-quiet/   ← vibe Vogue, dark + dourado, Cormorant italic
├── minimalist-bold/   ← vibe NYT Opinion, cream + ink + carmin, Inter Black
├── warm-premium/      ← vibe Aesop, cream + terra + terracota, Cormorant + Lato
└── native-raw/        ← vibe photo dump nativo, foto cheia + caixa branca, Arial
```

> **Native Raw é diferente dos outros 3:** não tem monograma, eyebrow, swipe nem
> paginação. Cada slide é só foto full-bleed + caixa de legenda branca fixa. A
> adaptação é quase toda nas FOTOS (enquadramento via `background-position`) e na
> copy dentro de `.caption p`. Ver `references/templates/native-raw/README.md`.

Cada template tem `style.css` + 8 `slide-NN.html` + `README.md` com instruções
específicas de adaptação. Estrutura dos 8 slides é a mesma — varia o DNA visual.

Pra adaptar à aluna:

1. **Copiar a pasta inteira** pra `conteudo/carrosseis/[YYYY-MM-DD]-[slug-tema]/`
2. **Substituir paleta** em `:root {}` no `style.css` pelas cores da aluna
   (ou manter default do estilo se a aluna não passou paleta)
3. **Em cada HTML, substituir:**
   - Monograma: `<div class="brand-mark">[INICIAL]</div>` (ou `.logo-mark` no Editorial Quiet)
   - Nome: `[NOME DA ALUNA]<span class="sub">[MARCA]</span>`
   - Fotos: `style="background-image:url('photos/[foto-N].jpg')"`
   - Eyebrow / Headline / Body adaptados à copy da aluna
4. **Slides com fundo alternativo** (cream no Editorial Quiet, ink no Minimalist
   Bold, terra no Warm Premium) precisam de `<body class="body-[fundo]">` +
   `<style>html, body { background: [cor] !important; }</style>` no `<head>` pra
   evitar faixa preta no rodapé. Ver README.md específico do template.

### Etapa 9 — Renderizar 8 PNGs via Chrome headless

```powershell
$dir = 'conteudo/carrosseis/[pasta-do-carrossel]'
$chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
foreach ($n in 1..8) {
  $slug = 'slide-{0:D2}' -f $n
  $html = Join-Path $dir "$slug.html"
  $png  = Join-Path $dir "$slug.png"
  $url = 'file:///' + ($html -replace '\\','/')
  & $chrome --headless --disable-gpu --hide-scrollbars `
    "--screenshot=$png" --window-size=1080,1350 `
    --virtual-time-budget=10000 --force-device-scale-factor=1 `
    $url 2>$null | Out-Null
}
```

**Alternativa Mac/Linux:** trocar `$chrome` por `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` (Mac) ou `google-chrome` (Linux).

**Resultado:** 8 PNGs `slide-01.png` ... `slide-08.png` prontos pra upload no Instagram.

### Etapa 10 — Entregar os PNGs renderizados (final)

A legenda, hashtags e stories já foram aprovados no checkpoint (Etapa 7) — agora
só entrega o resultado visual final.

```markdown
## Carrossel pronto: [Tema]

**Função:** [...]  ·  **Template:** [Editorial Quiet / Minimalist Bold / Warm Premium]

---

### 8 PNGs gerados em:
`conteudo/carrosseis/[YYYY-MM-DD]-[slug]/`

Slides:
- `slide-01.png` — Capa
- `slide-02.png` — Setup
- ... (até slide-08.png)

### Pacote completo na pasta
- `slide-01.html` ... `slide-08.html` (HTMLs fonte, caso queira editar)
- `style.css` (paleta + tipografia da aluna)
- `photos/` (5 fotos editoriais aplicadas)
- 8 PNGs prontos pra upload no Instagram

---

**Algo pra ajustar no visual?**
- "regenera slide N" → re-renderizo só esse PNG
- "muda paleta pra [HEX]" → re-renderizo os 8 com nova cor primária
- "troca template pra [outro]" → re-aplica em estilo diferente
- "troca foto do slide N" → outra foto do banco
- (Copy já aprovada — pra mudar copy, rode a skill de novo)
```

#### Resgate (caso a aluna esqueceu da legenda/stories aprovados)

```markdown
### Legenda aprovada
[texto]

### Hashtags
[#... #... ...]

### Stories de apoio (3-5)
[lista]

---

**Algo pra ajustar?**
- "regenera slide [N]" — refaz só esse slide (copy + render)
- "muda função pra [X]" — regera curva inteira
- "tom mais [adjetivo]" — ajusta voz
- "troca foto do slide [N]" — pra outra do banco
- "ajusta paleta" — muda cor primária e re-renderiza
```

---

## REGRAS DE OURO

1. **Use sempre um dos 4 templates como base.** Não improvise HTML/CSS do zero —
   adapte o template escolhido (Editorial Quiet / Minimalist Bold / Warm Premium /
   Native Raw). A escolha cabe à aluna OU à sua sugestão baseada no nicho/vocabulário dela.

2. **Sistema tipográfico bloqueado** (vale pros 3 templates editoriais; **Native Raw é exceção** — ver nota abaixo):
   - Cormorant Garamond italic — só na capa (line-soft + line-loud CAPS) + quotes literais
   - DM Sans Bold 700-800 — headlines dos slides intermediários
   - DM Sans Regular 400 — body, com palavras-chave em bold
   - JetBrains Mono — paginação + palavra-código CTA
   - **Exceção Native Raw:** usa Arial/Helvetica (fonte de sistema) de propósito — a "fonte sem fonte" é o que vende o nativo. Não aplique o sistema acima nesse template.

3. **Italic NÃO é decoração** — usar só em quotes literais de cliente entre aspas
   (ex: "cabe parcelar?", "quando começamos?"). Em todo o resto, sans bold + accent
   por cor.

4. **Negrito em palavras-chave do body** — não pontilhar negrito em frases inteiras.
   Negrito + accent color destaca o conceito-chave, não toda linha.

5. **Filtro 10 (anti-frase-de-efeito) é CRÍTICO** — toda headline passa pelo teste
   da cena concreta antes de aprovar.

6. **Cliente real, não persona genérica** — usar palavras DELA, frases reais que ela
   ouve no DM, números reais.

7. **CTA específico, nunca "comenta aí"** — palavra-código + tempo de resposta + DM
   ou link.

8. **Voz preservada** — palavras-marca da aluna aparecem ao menos 1x no carrossel.
   Palavras vetadas, jamais.

9. **Iteração granular** — sempre ofereça regeneração de slide específico.

10. **Foto editorial em slide-âncora** — capa (slide 1) e CTA (slide 8) levam foto
    editorial obrigatoriamente, se disponível. Slides intermediários alternam com/sem
    foto pra ritmo visual.

11. **CHECKPOINT obrigatório antes de renderizar PNGs** — toda copy (slides + legenda
    + stories) tem que ser aprovada pela usuária antes de chamar Chrome headless.
    Iterar texto é barato. Renderizar 8 PNGs sem confirmação = retrabalho garantido.
    Padrão: gerar copy → mostrar tudo → pedir "aprova?" → só então render.

12. **Entrevista é única.** Pergunte os 8 itens (4 copy + 4 visual) numa mensagem
    só no início. Não pergunte de novo depois do checkpoint. Se ela passou tudo
    no comando, pule a entrevista e gere direto.

13. **Portão de analogia (Etapa 1.5).** Se o tema engancha em algo em alta, faça UMA
    pergunta curta oferecendo a analogia ANTES de aplicar — essa é a única exceção
    permitida à "entrevista única". Se o tema é evergreen, nem mencione: siga reto.
    Quando a aluna topa, embuta a lógica da `carrossel-zeitgeist-bianca` (máx 2-3
    WebSearches, nunca inventar fato sobre o assunto).

---

## REGRA DE OURO META

Esta skill **opera por conversa**, não por arquivo. A aluna abre o Claude Code, te
diz quem ela é (no chat), pede o carrossel, recebe 8 PNGs prontos em até 2 minutos.

Se a aluna nunca te falou nada antes, faça a entrevista curta (4 perguntas de copy
+ 3 visuais). Se já te contou o negócio em mensagens anteriores ou nas instruções
do projeto, use o contexto e gere direto.

O design é editorial premium (não Canva genérico). A copy é aterrada em dor/desejo
concreto (não frase de efeito). O conjunto é entrega completa: PNGs + legenda +
stories.
