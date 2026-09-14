# Template: Editorial Quiet

Template visual canônico do sistema. Pra marcas premium feminino, mentorias, advocacia, terapia, lifestyle alto.

> Vibe: Vogue · The Cut · editorial dark com peso italic + sans bold

---

## DNA visual

**Paleta default (substituível pela paleta da aluna):**
```
--ink:           #1F0D23   /* dark plum — fundo principal */
--champagne:     #CDAC6C   /* dourado — accent em fundos dark */
--cream:         #F4ECD8   /* off-white — fundo alternativo */
--terracota:     #B25E47   /* accent em fundos cream */
```

**Tipografia:**
- **Cormorant Garamond italic** — display da CAPA (linha-soft + linha-loud CAPS) + citações literais
- **DM Sans Bold 700-800** — headlines dos slides intermediários
- **DM Sans Regular 400** — body, com palavras-chave em bold
- **JetBrains Mono** — paginação + palavra-código CTA

---

## Estrutura dos 8 slides

| Slide | Função | Layout | Foto |
|---|---|---|---|
| 01 | Capa-tese | Full-bleed (foto cobre todo o slide) + Cormorant CAPS centralizado | Foto editorial principal |
| 02 | Setup/dor | Só tipografia (dark) | Sem foto |
| 03 | Reframe | Split 60-40 (texto esq + foto dir) cream | Foto contextual (ex: escritório, decisão) |
| 04 | Aplicação | Só tipografia + comparativo 2 colunas (dark) | Sem foto |
| 05 | Lista de sinais | Split 60-40 (lista I/II/III esq + foto dir) dark | Foto autoridade (ex: palco, ação) |
| 06 | Manifesto | Centralizado puro (cream) | Sem foto |
| 07 | O que muda | Split 45-55 (foto esq + texto dir) dark | Foto resultado (ex: café/laptop) |
| 08 | CTA | Split 60-40 (texto esq + foto dir) dark, SEM seta swipe | Foto assinatura (ex: ambiente sofisticado) |

---

## Elementos comuns

**Em todos os slides:**
- **Topo esquerdo:** monograma circular (ex: "B") + nome + sub-marca
- **Topo direito:** linha 1 "Carrossel · Posicionar" + linha 2 paginação "0N — 08"
- **Lateral direita:** seta circular de swipe (slides 1-7, ausente no 8)
- **Rodapé:** meta discreto (esquerda: contexto do slide / direita: numeração romana)

---

## Como adaptar pra uma aluna nova

### 1. Substituir paleta

Edite as 4 variáveis no `style.css`:

```css
:root {
  --ink:        [cor escura principal da marca];
  --champagne:  [accent dourado/destaque];
  --cream:      [off-white quente];
  --terracota:  [accent terra/cream-accent];
}
```

**Derivação automática a partir de 1 cor:**
Se a aluna passar só 1 cor primária (ex: `#3A1F2D` bordô), derive:
- `--ink` = primary escurecida 15%
- `--champagne` = complementar dourado (ou pedir à aluna)
- `--cream` = neutro quente (#F4ECD8 ou #F2EDE3)
- `--terracota` = primary aclarada + saturada 30%

### 2. Substituir monograma + nome

Em **todos os 8 HTMLs**, troque:
```html
<div class="logo-mark">B</div>
<div class="logo-text">Bianca Freitas<span class="sub">Mentoria Castle</span></div>
```

por:
```html
<div class="logo-mark">[INICIAL]</div>
<div class="logo-text">[NOME DA ALUNA]<span class="sub">[MARCA/OFERTA]</span></div>
```

### 3. Substituir fotos

Crie pasta `photos/` no projeto da aluna com 5 fotos:
- `foto-capa.jpg` — retrato editorial principal (slide 1)
- `foto-escritorio.jpg` — cena de decisão/trabalho (slide 3)
- `foto-palco.jpg` — autoridade/ação (slide 5)
- `foto-cafe.jpg` — lifestyle/operando o negócio (slide 7)
- `foto-jornal.jpg` — ambiente sofisticado/assinatura (slide 8)

Se a aluna tem menos fotos, distribua as que tem ou pergunte qual usar em cada contexto. **Nunca repetir a mesma foto em 2 slides.**

### 4. Substituir copy

Copy de cada slide deve seguir os princípios:
- **DOR ou DESEJO concreto** — não frase de efeito vazia
- **Cena reconhecível** — frase exata que cliente fala ("cabe parcelar?"), número, prazo
- **Tipografia equilibrada** — italic só em quotes literais; resto sans bold
- **Palavras-chave em `<strong>`** — negrito + accent color

Veja `../filtros.md` (filtro 10) pra lista de padrões a evitar.

---

## Render → PNG

Cada HTML é um arquivo standalone que renderiza em 1080×1350. Use Chrome/Edge headless:

```powershell
$chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
foreach ($n in 1..8) {
  $slug = 'slide-{0:D2}' -f $n
  & $chrome --headless --disable-gpu --hide-scrollbars `
    "--screenshot=$slug.png" --window-size=1080,1350 `
    --virtual-time-budget=10000 --force-device-scale-factor=1 `
    "file:///$($pwd.Path -replace '\\','/')/$slug.html"
}
```

Resultado: 8 PNGs prontos pra upload no Instagram (slide-01.png ... slide-08.png).

---

## Observações importantes

- **Slide 6 (manifesto cream)** requer `<body class="body-cream">` + `<style>html, body { background: #F4ECD8 !important; }</style>` no `<head>` pra evitar faixa preta no rodapé.
- **Slide 8 (CTA)** não tem `<div class="swipe-indicator">` (último slide).
- **Body do slide 6** centraliza vertical com `.manifesto-center`. Os demais usam `.layout-text` (só texto) ou `.layout-split` (com foto).
