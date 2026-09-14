# Templates HTML/CSS por tipo de post

Cada tipo tem template-base que é calibrado pela identidade visual da marca
(`contexto/05-identidade-visual.md`).

> Todos os templates renderizam em **1080×1350px** — formato vertical Instagram feed.

---

## ESTRUTURA HTML BASE (todos os tipos)

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>[Tipo] — [slug-frase]</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=[FONT]&display=swap" rel="stylesheet">
<style>
  :root {
    /* Lê de contexto/05-identidade-visual.md */
    --primary: #...;
    --primary-deep: #...;
    --accent: #...;
    --cream: #...;
    --ink: #...;
  }
  body { margin: 0; padding: 0; background: var(--ink); }
  .post {
    width: 1080px;
    height: 1350px;
    position: relative;
    overflow: hidden;
    /* Specifics by type below */
  }
</style>
</head>
<body>
  <section class="post post-[tipo]">
    <!-- conteúdo do tipo específico -->
  </section>
</body>
</html>
```

---

## TIPO 1 — TWEET-POST

### Visual

- Cartão centralizado com borda sutil
- Avatar circular no topo (logo OU foto editorial da criadora)
- Handle e nome
- Texto em fonte sans (Inter ou similar) tamanho médio-grande
- Acentos em palavras-chave (champagne/dourado)
- Fundo: dark da marca

### CSS-template

```css
.post-tweet-post {
  background: var(--ink);
  display: flex;
  align-items: center;
  justify-content: center;
}

.tweet-card {
  width: 880px;
  background: var(--ink-card);
  border: 1px solid rgba(217, 195, 154, 0.15);
  border-radius: 24px;
  padding: 60px 70px;
  box-shadow: 0 30px 80px -20px rgba(0,0,0,0.4);
}

.tweet-header {
  display: flex;
  align-items: center;
  gap: 18px;
  margin-bottom: 40px;
}

.tweet-avatar {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: var(--accent);
  /* OU foto editorial */
}

.tweet-name {
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  font-size: 22px;
  color: var(--cream);
}

.tweet-handle {
  font-family: 'Inter', sans-serif;
  font-size: 18px;
  color: var(--muted);
}

.tweet-body {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 38px;
  line-height: 1.35;
  color: var(--cream);
  letter-spacing: -0.01em;
}

.tweet-body .em {
  color: var(--accent);
}

.tweet-meta {
  margin-top: 50px;
  padding-top: 24px;
  border-top: 1px solid rgba(217, 195, 154, 0.1);
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  color: var(--muted);
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
```

### Elementos opcionais
- Eyebrow acima do header ("VIA REEL DE QUINTA")
- Logo discreto no rodapé do cartão

---

## TIPO 2 — FRASE-QUOTE

### Visual

- Frase ÚNICA, centralizada, fonte serif italic display
- Fundo dark com identidade visual
- Acento champagne em 1 palavra-chave da frase
- Logo discreto canto inferior
- Hairline editorial (linha fina decorativa)

### CSS-template

```css
.post-frase-quote {
  background: var(--primary-deep);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 120px 100px;
  position: relative;
}

.quote-eyebrow {
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  letter-spacing: 0.32em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 80px;
  font-weight: 500;
}

.quote-rule {
  width: 60px;
  height: 1px;
  background: var(--accent);
  margin: 0 auto 60px;
}

.quote-body {
  font-family: 'Cormorant Garamond', 'Playfair Display', serif;
  font-weight: 400;
  font-style: italic;
  font-size: 88px;
  line-height: 1.08;
  color: var(--cream);
  text-align: center;
  letter-spacing: -0.015em;
  max-width: 880px;
}

.quote-body .em {
  color: var(--accent);
}

.quote-attribution {
  margin-top: 80px;
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 500;
}

.quote-logo {
  position: absolute;
  bottom: 60px;
  right: 60px;
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  font-size: 18px;
  letter-spacing: 0.16em;
  color: var(--muted);
}
```

### Variação se quote é de outro autor
Adicionar atribuição com nome do autor no rodapé:
```html
<div class="quote-attribution">— Autora · Livro</div>
```

---

## TIPO 3 — FRASE-DO-REEL

### Visual

- Foto/screenshot do reel ao fundo (com overlay escuro 60-70%)
- Frase em primeiro plano, tipografia bold
- Ícone de play centralizado ou no canto
- Eyebrow "VÍDEO COMPLETO NO FEED"

### CSS-template

```css
.post-frase-do-reel {
  background-image: linear-gradient(rgba(20,7,26,0.72), rgba(20,7,26,0.85)),
                    url('reel-screenshot.jpg');
  background-size: cover;
  background-position: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 100px;
  position: relative;
}

.reel-eyebrow {
  font-family: 'Inter', sans-serif;
  font-size: 18px;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 40px;
  font-weight: 600;
}

.reel-play {
  width: 80px;
  height: 80px;
  border: 2px solid var(--accent);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 60px;
  /* Triângulo dentro */
}

.reel-frase {
  font-family: 'Inter', sans-serif;
  font-weight: 800;
  font-size: 76px;
  line-height: 1.06;
  color: var(--cream);
  text-align: center;
  letter-spacing: -0.025em;
  max-width: 920px;
}

.reel-frase .em {
  color: var(--accent);
}

.reel-cta {
  margin-top: 80px;
  font-family: 'Inter', sans-serif;
  font-size: 18px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--cream);
  font-weight: 500;
}
```

---

## TIPO 4 — PRINT-DM

### Visual

- Layout estilizado de DM (premium, NÃO replica literal de Instagram)
- Avatar do cliente (autorizado/anonimizado)
- Mensagem em balão com identidade visual
- Frase principal destacada
- Tag "DEPOIMENTO REAL" pra credibilidade

### CSS-template

```css
.post-print-dm {
  background: var(--ink);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 80px;
}

.dm-eyebrow {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 60px;
  font-weight: 600;
}

.dm-conversation {
  width: 880px;
  background: var(--ink-card);
  border: 1px solid rgba(217, 195, 154, 0.15);
  border-radius: 16px;
  padding: 50px;
}

.dm-header {
  display: flex;
  align-items: center;
  gap: 16px;
  padding-bottom: 30px;
  border-bottom: 1px solid rgba(217, 195, 154, 0.1);
}

.dm-avatar {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: var(--muted);
}

.dm-from {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 18px;
  color: var(--cream);
}

.dm-handle {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  color: var(--muted);
  letter-spacing: 0.04em;
}

.dm-message {
  margin-top: 40px;
  padding: 32px 40px;
  background: var(--primary);
  border-radius: 24px 24px 24px 4px;
  font-family: 'Inter', sans-serif;
  font-size: 30px;
  line-height: 1.4;
  color: var(--cream);
}

.dm-frase-destaque {
  font-weight: 600;
  color: var(--accent);
}

.dm-meta {
  margin-top: 30px;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  color: var(--muted);
  letter-spacing: 0.16em;
  text-transform: uppercase;
}
```

---

## TIPO 5 — POST-ÂNCORA EDITORIAL

### Visual

- Foto editorial profissional (full bleed ou 50/50 com texto)
- Frase como statement em tipografia generosa
- Logo + ano em rodapé editorial
- Hairlines decorativas
- Identidade visual mais elaborada

### CSS-template (variante 50/50)

```css
.post-ancora {
  display: grid;
  grid-template-columns: 1fr 1fr;
  height: 1350px;
}

.ancora-foto {
  background-image: url('foto-editorial.jpg');
  background-size: cover;
  background-position: center;
}

.ancora-texto {
  background: var(--primary-deep);
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 80px 70px;
  position: relative;
}

.ancora-eyebrow {
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 500;
  margin-bottom: 16px;
}

.ancora-rule {
  width: 80px;
  height: 1px;
  background: var(--accent);
  margin-bottom: 50px;
}

.ancora-frase {
  font-family: 'Cormorant Garamond', 'Playfair Display', serif;
  font-weight: 400;
  font-style: italic;
  font-size: 64px;
  line-height: 1.12;
  color: var(--cream);
  letter-spacing: -0.015em;
}

.ancora-frase .em {
  color: var(--accent);
}

.ancora-signature {
  position: absolute;
  bottom: 70px;
  left: 70px;
  right: 70px;
  display: flex;
  justify-content: space-between;
  border-top: 1px solid rgba(217, 195, 154, 0.15);
  padding-top: 20px;
}

.ancora-name {
  font-family: 'Cormorant Garamond', serif;
  font-style: italic;
  font-size: 20px;
  color: var(--accent);
}

.ancora-meta {
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}
```

### Variante full-bleed (foto cobre tudo, texto sobre overlay):

Pra peças mais cinematográficas. Foto ocupa 100%, texto overlay com gradient.

---

## REGRAS DE FORMATAÇÃO DE TEXTO

1. **Aspas tipográficas sempre** — " " ao invés de ""
2. **Travessões em** — — ao invés de -
3. **Acento de palavra-chave** — wrap em `<span class="em">palavra</span>` na palavra
   que carrega peso
4. **CAPS apenas em eyebrows** — texto principal em case normal
5. **Highlight ÚNICO por frase** — não pintar 3 palavras de dourado, só 1-2

---

## VALIDAÇÃO PÓS-RENDER

Antes de exportar PNG, checar:

1. **Frase cabe sem cortar?** — verificar overflow no preview
2. **Acento champagne contrasta com fundo?** — testar legibilidade
3. **Logo está no lugar?** — não cortado, não invisível
4. **Identidade visual reconhecível?** — coerente com `05-identidade-visual.md`

Se algum falha, ajustar antes de exportar.

---

## REGRA DE OURO

Cada template é um esqueleto. A IDENTIDADE VISUAL específica da marca preenche.
Mesmo template + paleta diferente = post irreconhecivelmente diferente.

A coerência visual da marca > a inovação de layout.
