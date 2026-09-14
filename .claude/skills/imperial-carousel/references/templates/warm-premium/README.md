# Template: Warm Premium

Template visual orgânico/caloroso. Pra marcas wellness, nutricionistas, coaches calorosas, terapeutas maternais, skincare natural, lifestyle warm.

> Vibe: Aesop · & Other Stories · Sézane · wellness premium

---

## DNA visual

**Paleta default (substituível):**
```
--cream:        #EFE7D8   /* off-white quente base */
--terra-deep:   #3D2817   /* marrom terra escuro, fundo alternativo */
--terracota:    #C2785C   /* accent terracota — alma quente */
--sand:         #C9B7A0   /* areia, secondary suave */
--olive:        #5C6849   /* verde-musgo opcional pra wellness */
```

**Substitutos comuns:**
- Wellness pure: terracota → verde-musgo `#5C6849`
- Skincare botânico: terracota → rosé `#C18B7A` + verde-sálvia
- Cafeteria/produto artesanal: manter terracota

**Tipografia:**
- **Cormorant Garamond 500** — display sem italic (italic só em quotes literais)
- **Lato Regular 400** — body, com palavras-chave em Lato 700
- **JetBrains Mono 500** — paginação + palavra-código CTA

---

## Estrutura dos 8 slides

Mesma estrutura dos outros templates. Diferenças visuais do Warm Premium:

- **Monograma:** círculo com borda terracota + letra terracota italic
- **Eyebrow:** hairline curta terracota + texto Lato bold CAPS
- **Swipe indicator:** círculo terracota sólido com seta cream
- **Textura:** noise SVG mais visível (papel/linho — mix-blend multiply)
- **Box highlight:** translúcida com hairlines terracota top/bottom (similar ao Editorial Quiet, mas com paleta terra)
- **Comparativo:** colunas com borders sand entre elas
- **CTA:** bloco translúcido cream com border terracota à esquerda
- **Alternância tonal:** terra (peso/profundidade) × cream (claridade/lifestyle)

---

## Como adaptar pra uma aluna nova

### 1. Substituir paleta

```css
:root {
  --cream:      [cor cream/off-white quente];
  --terra-deep: [cor terra escura, fundo dark];
  --terracota:  [cor terra accent];
  --sand:       [cor areia secondary];
}
```

### 2-4. Mesmo procedimento dos outros templates

---

## Quando recomendar Warm Premium pra uma aluna

✅ Marca tem vibe **calorosa, orgânica, natural**
✅ Cliente busca **acolhimento, cuidado, conexão**
✅ Nicho: nutrição, wellness, coaching feminino caloroso, terapia maternal, skincare natural, beleza, cafeteria premium, produto artesanal
✅ Paleta da aluna **tem tons terra, beges, verdes orgânicos**

❌ Aluna tem marca **dark/dramática/clássica** → use **Editorial Quiet**
❌ Marca **moderna/tech/cerebral** → use **Minimalist Bold**

---

## Observações técnicas

- **Slides terra** precisam de `<body class="body-terra">` + `<style>html, body { background: #3D2817 !important; }</style>` no `<head>`
- **Slide 8 (CTA)** não tem swipe-indicator
- **Capa (slide 1)** usa `.slide.terra.has-photo` — foto editorial + overlay terra + texto cream centralizado
