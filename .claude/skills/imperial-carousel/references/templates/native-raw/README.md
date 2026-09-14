# Template: Native Raw (Nativo / Cru)

Template visual **anti-design**. Foto cheia ocupando o slide inteiro + uma caixa branca de legenda, como se fosse um post tirado na hora e legendado direto no app. Zero elementos editoriais (sem monograma, sem eyebrow, sem swipe, sem paginação).

> Vibe: photo dump nativo do Instagram · close friends · stories printados · feed orgânico de gente real

Pra marca/aluna que quer parecer **presente e humana, não "agência"**. Funciona muito bem em conta pessoal, bastidores, conteúdo de processo, e quando a foto JÁ é forte e deve ser a protagonista. Também é o estilo que mais "engana o algoritmo de aparência de anúncio" — parece conteúdo, não criativo pago.

---

## DNA visual

**Paleta default (substituível):**
```
--caption-bg:    rgba(255, 255, 255, 0.95)   /* caixa branca quase sólida */
--caption-text:  #1b1b1b                      /* quase-preto legível */
--caption-radius: 6px                         /* canto sutil, cara de app */
```

A "paleta" aqui é mínima de propósito — a cor vem da FOTO, não do design. A caixa é neutra pra não competir com a imagem.

**Variante CRU-DARK (opcional):** se as fotos da aluna forem muito claras/lavadas e a caixa branca sumir, troque no `:root`:
```css
--caption-bg:   rgba(0, 0, 0, 0.55);
--caption-text: #ffffff;
```

**Tipografia:**
- **Arial / Helvetica Neue** — a fonte de sistema do feed. É proposital: a fonte "sem fonte" é o que vende o nativo. NÃO troque por serifada/display.
- Tamanho 46px, line-height 1.32, centralizado.
- Palavras-chave em `<strong>` (700) — único recurso de ênfase.

---

## Estrutura dos 8 slides

Mesma curva narrativa dos outros templates (capa → setup → virada → aplicação → itens → solução → CTA). O que muda é a forma:

- **Cada slide = 1 foto full-bleed + 1 caixa de legenda.** Nada além disso.
- **A caixa é FIXA** — mesmo `bottom`, mesmo `left/right` em todos os 8 slides (ponto aprovado no carrossel original). Não mova a caixa entre slides; a constância é o que dá ritmo de "álbum".
- **O enquadramento da foto é a única variável visual** — ajuste `background-size` (100%+ pra dar zoom) e `background-position` pra posicionar o ponto focal acima/atrás da caixa.
- **Listas:** quando o slide é item de lista, comece a frase com o número em negrito (`<strong>1. ...</strong>`).
- **Capa (slide 1)** e **CTA (slide 8)** levam as fotos editoriais mais fortes da aluna.

---

## Como adaptar pra uma aluna nova

### 1. Paleta — quase nada a fazer
Na maioria dos casos, mantenha o branco default. Só ative a variante CRU-DARK se as fotos forem claras demais.

### 2. Fotos (o passo que importa)
- Coloque 8 fotos em `photos/` como `p-01.jpg` ... `p-08.jpg`.
- Fotos **autênticas/orgânicas** funcionam melhor que fotos de estúdio perfeitas — o ponto é parecer real.
- Ajuste `background-position` slide a slide pra que o rosto/ponto focal não fique escondido atrás da caixa branca.

### 3. Copy
- Substitua o texto dentro de `.caption p`. Frases curtas (cabem ~2-3 linhas na caixa).
- Use `&ccedil;`, `&atilde;`, `&eacute;` etc. (entities HTML) pra acentos renderizarem certo no Chrome headless.
- 1 palavra-chave em `<strong>` por slide — não pontilhe negrito.

### 4. Render
Mesmo procedimento dos outros templates (Chrome headless, 1080×1350).

---

## Quando recomendar Native Raw pra uma aluna

✅ Marca quer parecer **humana, próxima, presente** (não corporativa/agência)
✅ Conteúdo de **bastidores, processo, rotina, opinião pessoal**
✅ A **foto é forte** e deve ser protagonista
✅ Aluna quer fugir do "cara de anúncio" / quer alcance orgânico
✅ Conta pessoal, creator, profissional liberal que aparece muito

❌ Marca precisa de **autoridade editorial/luxo formal** → use **Editorial Quiet**
❌ Conteúdo **cerebral/tech/dado-pesado** que pede estrutura → use **Minimalist Bold**
❌ Não tem fotos boas disponíveis → Native Raw depende de foto; prefira um template tipográfico

---

## Observações técnicas

- A caixa de legenda usa variáveis em `:root` — pra mexer em posição/cor, edite lá uma vez e vale pros 8 slides.
- `image-orientation: from-image` evita foto deitar/rotacionar errado no headless.
- Não há fundo alternativo (terra/ink/cream) como nos outros templates — o fundo é sempre a foto.
- Slide 8 não tem tratamento especial de CTA além da palavra-código em negrito — a simplicidade é o ponto.
- **Origem:** este template foi extraído do carrossel aprovado `2026-06-24-musica-nativo-ok` (tese "carrossel + áudio em alta = alcance qualificado").
