---
name: imperial-post
description: |
  Skill canônica de post-frase única do sistema Imperium. Pega 1 frase (do reel já
  gravado, do DM real, da live, do depoimento, do livro) e gera post visual 1080×1350
  com identidade da marca + legenda + hashtags. 5 tipos × 3 estilos editoriais
  (Editorial Quiet / Minimalist Bold / Warm Premium) = 15 combinações. Entrevista
  única no início, checkpoint da frase+legenda antes do render, export PNG via
  Chrome headless. Triggers: "/imperial-post", "post simples", "post com essa frase",
  "post-frase", "tweet-post", "frase-imagem", "post âncora".
allowed-tools: Read, Write, Glob, Grep, Bash
---

# Imperial Post

A skill mais granular do sistema. 1 frase → 1 PNG visual 1080×1350 pronto pra postar.

> O post-frase sustenta o feed entre carrosséis e reels. Frequência alta (2-4x/semana).
> Por isso o rigor é maior — qualquer slip aparece muito.

---

## QUANDO USAR

Use proativamente quando:
- Usuária pede `/imperial-post`, "post com essa frase", "tweet-post", "frase-imagem"
- Frase marcante de reel já gravado vai virar post
- DM real autorizada vira print-DM (prova social)
- Quote de livro/podcast/palestra alinhado com tese
- Manifesto da marca / efeméride

---

## FLUXO DE EXECUÇÃO

### Etapa 1 — Entrevista única (copy + visual juntos)

Use o que a usuária já mencionou. Pergunte só o que falta — TUDO em uma mensagem:

> "Pra gerar esse post, preciso de 8 coisas (responde numa mensagem só):
>
> **SOBRE O CONTEÚDO:**
>
> 1. **Frase principal** — qual a frase que vira o post? (de reel, DM, livro, etc.)
> 2. **Tipo de post** — qual encaixa melhor?
>    - **tweet-post** — cartão estilo tweet, frase autoral curta intelectual
>    - **frase-quote** — manifesto editorial centralizado, peso de aforismo
>    - **frase-do-reel** — foto/cena do reel ao fundo + frase + play icon
>    - **print-dm** — depoimento real de DM autorizada (prova social)
>    - **post-âncora** — foto editorial + statement, peça manifesto
> 3. **Etapa de funil** — Topo / Meio / Fundo / Pós-conversão? (define CTA da legenda)
> 4. **Sobre você** — 2 frases sobre seu negócio + voz/palavras-marca/vetadas
>
> **SOBRE A IDENTIDADE VISUAL:**
>
> 5. **Estilo** — Editorial Quiet / Minimalist Bold / Warm Premium (se não souber,
>    sugiro baseado no nicho)
> 6. **Cor primária HEX** — substitui a paleta default do estilo. Se não tiver, uso default
> 7. **Foto disponível** (só pra frase-do-reel e post-âncora) — onde está?
> 8. **Sua assinatura** — nome + monograma (1 letra) + sub-marca"

### Etapa 2 — Validar a frase

#### Filtro de tamanho (por tipo)
- Tweet-post: max 20 palavras (frase principal)
- Frase-quote: max 15 palavras
- Frase-do-reel: max 12 palavras (frase precisa caber em texto grande sobre foto)
- Print-DM: max 25 palavras (msg da pessoa)
- Post-âncora: max 18 palavras

Acima do limite: sugira cortar OU dividir em frase principal + apoio.

#### Filtro de palavras vetadas
Aplicar `references/filtros.md` (lista universal + da marca específica da usuária).

#### Print-DM = autorização obrigatória
Confirme com a usuária que tem autorização da cliente. NUNCA invente DM. Anonimize
quando solicitado.

### Etapa 3 — Gerar copy completa

Gere TUDO antes do checkpoint:

1. **Frase principal** (ajustada se passou do limite)
2. **Acento** — palavra/parte que vai em cor accent (champagne / carmin / terracota)
3. **Atribuição/footer** — quem assina (nome + sub-marca)
4. **Legenda do post:**
   ```
   [Hook — 1-2 linhas, soa como ela]

   [Desenvolvimento — 3-5 linhas aprofundando a tese OU contexto da frase]

   [CTA — 1-2 linhas conforme etapa de funil]
   ```
5. **Hashtags** — 8-12 em uma linha

**Princípios de copy:**
- A frase é o herói. Legenda **complementa**, não duplica
- Sem frase de efeito vazia (ver filtro 10 em `filtros.md`)
- CTA específico, nunca "comenta aí"

### Etapa 4 — Validar pelos filtros

Ver `references/filtros.md`. Aplicar TODOS os filtros:
1. Palavras vetadas (universais + da marca)
2. Clichês AI-flavored
3. Tipo certo pro contexto (frase autoral → tweet-post; quote outro autor → frase-quote)
4. CTA específico (não genérico)
5. Print-DM com autorização confirmada
6. **Filtro 10 — anti-frase-de-efeito vazia** (ver lista em `filtros.md`)

### Etapa 5 — CHECKPOINT: aprovar copy ANTES de renderizar (OBRIGATÓRIO)

**NÃO gere PNG sem antes mostrar tudo à usuária e ter aprovação explícita.**

Apresente assim:

```markdown
## Post pronto: [Frase truncada]

**Tipo:** [tweet-post / frase-quote / frase-do-reel / print-dm / post-âncora]
**Estilo:** [Editorial Quiet / Minimalist Bold / Warm Premium]
**Paleta:** [cor primária]
**Etapa:** [Topo / Meio / Fundo / Pós-conversão]

---

### Frase principal
> "[Frase completa]"

**Acento (em cor):** "[parte destacada]"

### Legenda
[texto completo: hook + desenvolvimento + CTA]

### Hashtags
[# # # ... 8-12]

---

**A copy passa? Posso renderizar o PNG?**

- **"aprova"** → renderizo o PNG com o template e paleta escolhidos
- **"refrase"** → reescreve a frase principal mantendo essência
- **"encurta"** → versão mais curta
- **"tom mais [adjetivo]"** → recalibra
- **"troca CTA"** → reformula
- **"muda tipo pra [X]"** → mesma frase, outro layout
- **"muda estilo pra [X]"** → mesma frase, outro template visual
```

**Só depois que a usuária disser "aprova", avance pra Etapa 6.**

### Etapa 6 — Gerar HTML usando template

Pegue o template correspondente em `references/templates/`:

```
references/templates/
├── tweet-post.template.html
├── frase-quote.template.html
├── frase-do-reel.template.html
├── print-dm.template.html
├── post-ancora.template.html
└── styles/
    ├── editorial-quiet.css
    ├── minimalist-bold.css
    └── warm-premium.css
```

**Lógica de adaptação:**

1. **Copiar o template do tipo escolhido** pra `conteudo/posts/[YYYY-MM-DD]-[slug]/index.html`
2. **Copiar a pasta `styles/`** completa
3. **Substituir os placeholders no HTML:**
   - `{{STYLE}}` → nome do estilo (editorial-quiet / minimalist-bold / warm-premium)
   - `{{BG}}` → cor de fundo correspondente (ver tabela abaixo)
4. **Substituir conteúdo no HTML:**
   - Nome / monograma / sub-marca
   - Frase principal + acento (`<span class="accent">...</span>`)
   - Atribuição
   - Foto (se tipo precisar): `style="background-image:url('photos/foto.jpg')"`
5. **Substituir paleta no CSS escolhido** (em `:root {}`) pelas cores da marca da aluna
   (ou manter default se a aluna não passou paleta)

**Tabela `{{BG}}` por tipo × estilo:**

| Tipo | Editorial Quiet | Minimalist Bold | Warm Premium |
|---|---|---|---|
| tweet-post (dark) | `#1F0D23` | `#0A0A0A` | `#3D2817` |
| frase-quote (light) | `#F4ECD8` | `#F5F1EA` | `#EFE7D8` |
| frase-do-reel (dark) | `#1F0D23` | `#0A0A0A` | `#3D2817` |
| print-dm (light) | `#F4ECD8` | `#F5F1EA` | `#EFE7D8` |
| post-âncora (dark) | `#1F0D23` | `#0A0A0A` | `#3D2817` |

### Etapa 7 — Renderizar PNG via Chrome headless

```powershell
$chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
$html = 'conteudo/posts/[pasta]/index.html'
$png  = 'conteudo/posts/[pasta]/post.png'
$url = 'file:///' + ($html -replace '\\','/')

cmd /c """$chrome"" --headless --disable-gpu --hide-scrollbars ""--screenshot=$png"" --window-size=1080,1350 --virtual-time-budget=8000 --force-device-scale-factor=1 ""$url"" 2>nul"
```

**Alternativa Mac/Linux:** trocar binário por `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` ou `google-chrome`.

### Etapa 8 — Entregar PNG final

```markdown
## Post pronto: [Frase truncada]

**Tipo:** [...]  ·  **Estilo:** [...]  ·  **Pasta:** conteudo/posts/[YYYY-MM-DD]-[slug]/

### Arquivos:
- `post.png` — pronto pra upload (1080×1350)
- `index.html` — fonte, caso queira editar
- `styles/[estilo].css` — paleta da marca aplicada
- `photos/` (se aplicável) — foto editorial usada

---

**Algo pra ajustar no visual?**
- "muda tipo pra [X]" — mesma frase, outro layout (refaz HTML + render)
- "muda estilo pra [X]" — mesmo tipo, outro template visual
- "ajusta paleta pra [HEX]" — re-renderiza com nova cor primária
- "troca foto" — outra foto do banco (se aplicável)
- (Copy já aprovada — pra mudar a frase, rode a skill de novo)
```

---

## REGRAS DE OURO

1. **A frase é o herói.** Tudo no post serve a frase. Se o design rouba foco, refaz.

2. **1 frase = 1 post.** Se há 2 frases boas, 2 posts separados.

3. **5 tipos × 3 estilos = 15 combinações.** Use sempre um dos templates como base —
   não improvise HTML/CSS do zero.

4. **Filtro 10 (anti-frase-de-efeito) é CRÍTICO.** Posts simples são frequentes
   (2-4x/semana) — qualquer slip de copy vazia aparece muito.

5. **Tipo certo pro contexto:**
   - Frase autoral original → **tweet-post** ou **frase-quote**
   - Frase de reel publicado → **frase-do-reel**
   - DM real → **print-dm** (com autorização)
   - Quote de outro autor → **frase-quote** (com atribuição)
   - Manifesto pessoal → **post-âncora**

6. **Legenda complementa, não duplica.** A frase está no post — a legenda contextualiza.

7. **CTA específico, nunca "comenta aí".** Pergunte qual CTA OU sugira 2-3 conforme
   etapa de funil.

8. **Identidade visual rigorosa.** Paleta exata da marca substituindo o default
   do template.

9. **Print-DM = autorização obrigatória.** Confirme antes de gerar. Anonimize quando
   solicitado.

10. **CHECKPOINT obrigatório antes de renderizar PNG.** Frase + legenda aprovadas
    pela usuária antes de chamar Chrome headless. Iterar texto é barato.

11. **Entrevista é única.** Pergunte os 8 itens (4 copy + 4 visual) numa mensagem
    só no início. Não pergunte de novo depois do checkpoint.

---

## REGRA DE OURO META

Posts simples são frequentes — 2-4 por semana. Qualquer slip de qualidade aparece
muito. A skill é mais rigorosa em posts simples que em outras peças.

Tempo total da execução: < 2 minutos da entrevista até o PNG. Mas dentro desses 2
min, **rigor**: frase validada, copy aprovada, design adaptado à marca, PNG pronto.
