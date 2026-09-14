# Template: Minimalist Bold

Template visual editorial brutal. Pra marcas tech, marketing moderno, designers, criativas, terapeutas modernas — qualquer marca cerebral / sharp / contemporânea.

> Vibe: NYT Opinion · Pentagram · Stripe · Linear

---

## DNA visual

**Paleta default (substituível):**
```
--cream:     #F5F1EA   /* off-white quente base */
--ink:       #0A0A0A   /* quase-preto, fundo alternativo */
--carmin:    #B83A2E   /* vermelho saturado — accent NYT Opinion */
```

**Substitutos comuns pro carmin (escolha do nicho):**
- Verde profundo `#2D5C42` — wellness moderno
- Azul cobalto `#1E3A5F` — consultoria séria, advocacia
- Laranja queimado `#D85A1E` — branding criativo
- Roxo digital `#5B2D8C` — tech feminino

**Tipografia:**
- **Inter Black 900** — display, peso brutal, ZERO italic
- **Inter Regular 400** — body, com palavras-chave em Inter 800
- **JetBrains Mono 500** — paginação + palavra-código CTA

---

## Estrutura dos 8 slides

Mesma estrutura do Editorial Quiet — capa full-bleed + 7 layouts variados. Diferenças visuais:

- **Monograma:** quadrado carmin com letra cream-100 (não circular)
- **Eyebrow:** bloco carmin sólido com texto cream-100 (não hairlines)
- **Swipe indicator:** quadrado ink/carmin (não circular)
- **Highlight box:** fundo cream-100 com border 4px carmin à esquerda (não hairlines top/bottom)
- **Comparativo:** caixa ink semi-transparente vs caixa carmin sólida
- **CTA:** bloco carmin com palavra-código em fundo cream-100
- **Alternância tonal:** ink (slides com mais peso) × cream (slides de respiração)

---

## Como adaptar pra uma aluna nova

### 1. Substituir paleta

```css
:root {
  --cream:   [cor cream/off-white da marca];
  --ink:     [cor escura, quase-preto];
  --carmin:  [cor accent saturada];
}
```

### 2-4. Mesmo procedimento dos outros templates
Substituir monograma + nome + fotos + copy. Ver `../editorial-quiet/README.md` pra detalhes do procedimento (idêntico).

---

## Quando recomendar Minimalist Bold pra uma aluna

✅ Marca tem vibe **moderna, sharp, cerebral**
✅ Cliente é **B2B ou profissional contemporâneo**
✅ Nicho: tech, marketing, design, consultoria, terapia moderna
✅ Aluna **não se identifica com "premium feminino dourado"**
✅ Quer comunicação **direta, sem suavização**

❌ Aluna tem marca delicada/feminina/calorosa → use **Editorial Quiet** ou **Warm Premium**
❌ Nicho wellness/coaching maternal → use **Warm Premium**

---

## Observações técnicas

- **Slides ink** precisam de `<body class="body-ink">` + `<style>html, body { background: #0A0A0A !important; }</style>` no `<head>`
- **Slide 8 (CTA)** não tem swipe-indicator
- **Capa (slide 1)** usa `.slide.ink.has-photo` — foto editorial + overlay ink + texto cream alinhado à esquerda (não centralizado como no Editorial Quiet)
