---
name: youtube-transcricao-carrossel
description: >
  Pipeline completo e autocontido de conteúdo, que se adapta à marca de QUEM usa (lê o
  contexto/ da pessoa). Pega 1 vídeo do YouTube (link dado OU busca um em alta no NICHO
  DA PESSOA) → transcreve localmente → resumo estratégico + 5 ideias → salva no Notion →
  gera carrosséis prontos pra postar (8 slides desenhados + legenda + hashtags + stories),
  na voz e na identidade visual da pessoa. Faz TUDO sozinha, sem chamar outras skills.
  Também mostra como rodar isso toda segunda-feira. Use quando alguém quiser transformar
  um vídeo (ou "a semana") em conteúdo pronto. Triggers: "/youtube-transcricao-carrossel",
  "roda a semana", "transforma esse vídeo em carrossel", "do vídeo ao carrossel", "acha um
  vídeo em alta e faz os carrosséis", "pega esse vídeo do YouTube e cria conteúdo", "cria o
  conteúdo da semana".
---

# YouTube → Transcrição → Carrossel

Pipeline autocontido: do vídeo do YouTube aos carrosséis renderizados. **NÃO chama outras
skills** — o template de design está em `references/template/`.

> **Multi-marca.** Esta skill serve pra QUALQUER pessoa/nicho. Ela NÃO tem marca fixa:
> lê tudo (nicho, voz, cliente, oferta, paleta, fotos) do `contexto/` do projeto de quem
> está usando. Nunca assuma marca/nicho/oferta — sempre puxe do contexto.

---

## QUANDO USAR
- A pessoa dá um link de YouTube e quer virar carrossel/conteúdo.
- A pessoa pede "roda a semana" / "cria o conteúdo da semana" (aí você BUSCA um vídeo em alta).
- Rotina semanal de conteúdo a partir de uma referência.

NÃO use pra: carrossel de tema solto sem vídeo, roteiro de reel isolado, plano semanal sem vídeo.

---

## FASE 0 · Carregar o contexto da marca (SEMPRE primeiro)

Leia os arquivos em `contexto/` do projeto atual (preenchidos pela skill de onboarding /
passaporte). Extraia e use em TODO o resto:
- `01-empresa.md` → **nicho** (usado na busca do vídeo), posicionamento, nome da marca + @handle.
- `02-voz-e-tom.md` → **voz**, palavras-marca, palavras vetadas, ritmo.
- `03-cliente-ideal.md` → pra quem é, dor, linguagem real.
- `04-diferenciais.md` → provas, método, números.
- `05-identidade-visual.md` → **paleta e fontes** (pra adaptar o `style.css`) + monograma/assinatura.
- `06-ofertas.md` → **a oferta/isca** que o CTA vai promover.

> Se `contexto/` estiver vazio ou faltando `02-voz-e-tom.md` e `03-cliente-ideal.md`:
> **PARE** e diga: "Pra criar na sua voz, rode antes o /passaporte-imperial pra preencher
> seu contexto. Volto aqui depois." Não invente marca/voz/nicho.

---

## FASE 1 · Fonte do vídeo

- **Se a pessoa deu um link do YouTube:** use ele.
- **Se pediu "roda a semana" / não deu link:** use **WebSearch** pra achar 1 vídeo RECENTE
  (últimas ~2-3 semanas) e relevante do **NICHO DA PESSOA** (o que você leu em `01-empresa.md`).
  Pode ser internacional (inglês etc.) — priorize a MELHOR referência, não a mais brasileira.
  Monte as buscas com os termos do nicho dela (ex.: nutrição, advocacia, moda, fitness...).
  Anote: título, canal, idioma, URL e por que está em alta.

---

## FASE 2 · Transcrição (local, sem Algrow)

Extraia o VIDEO_ID e rode via Bash:
```bash
python -c "from youtube_transcript_api import YouTubeTranscriptApi; api=YouTubeTranscriptApi(); ft=api.fetch('VIDEO_ID', languages=['pt','en']); print(' '.join(s.text.replace(chr(10),' ') for s in ft.snippets))"
```
- Se faltar a lib: `pip install youtube-transcript-api` e tente de novo.
- Fallback: `yt-dlp --skip-download --write-auto-subs --sub-langs "pt,en" --sub-format vtt -o "sub.%(ext)s" "URL"` e leia o .vtt.
- Se o vídeo for em inglês, tudo bem — o conteúdo final sai SEMPRE em português, adaptado
  ao público da pessoa.

---

## FASE 3 · Resumo estratégico + 5 ideias

Na voz da pessoa (Fase 0) e pro público dela, gere em português:
- **Resumo estratégico:** tese central, contexto, principais dicas, o que aposentar.
- **5 ideias de conteúdo** (mix reels + carrosséis), cada uma com: gancho, formato,
  objetivo (atrair/conectar/posicionar/vender) e CTA. **Aterre no nicho e no cliente dela.**
- **Ordem sugerida** de publicação.

**Fidelidade:** se a copy citar dado/algoritmo/fala de executivo (ex.: "o Instagram fez X",
"fulano disse Y"), CONFIRME com WebSearch antes de afirmar. Não coloque palavra na boca de
ninguém. Melhor suavizar do que expor a marca a uma informação errada.

---

## FASE 4 · Salvar no Notion

Crie uma página no Notion. Se houver uma pasta-mãe de conteúdo definida no contexto/projeto,
use ela; senão, pergunte onde salvar (ou crie no nível superior). Título:
`Conteúdo da Semana — <AAAA-MM-DD>: <tema>`. Conteúdo: (1) Fonte (título+canal+URL),
(2) Resumo estratégico, (3) As 5 ideias, (4) Transcrição integral.

---

## FASE 5 · Gerar os carrosséis (template embutido)

Padrão: **2 carrosséis** (as 2 ideias de carrossel mais fortes). Pergunte se quer outras/mais.

### 5.1 Pastas
```
conteudo/carrosseis/<AAAA-MM-DD>/<NN>-<slug>/
  ├── style.css   ├── photos/   ├── slide-1..8.html   └── legenda-e-stories.md
```
Copie `references/template/style.css` pra cada pasta. **Adapte a paleta** no `:root` do CSS
pelas cores de `05-identidade-visual.md` (se a pessoa passou HEX). Senão, mantenha o default.

### 5.2 Design (ver `references/template/exemplo-*.html`)
- **8 slides**, alternando fundos: `slide--photo` / `slide--dark` / `slide--cream`.
  Fotos nos slides **1 (capa), ~4, ~6 e 8 (CTA)**; os demais tipográficos.
- **Capa:** `slide--photo` + `caption cap-center` + `h1.display.h-cover`.
- **Títulos:** `.display` (serif, **negrito 700**, grande). Destaque em `.gold`/`.serif-it`.
  Sempre negrite e dê destaque aos títulos.
- **Body:** `.body.body--lg`, palavras-chave em `<strong>`. **Listas:** `<ul class="list">`.
- **CTA (slide 8):** foto + `.lead` + `.body` + `<span class="chip">Comenta &#8594; PALAVRA</span>`
  + `<span class="codeword gold-l">PALAVRA</span>`. Ação = **comentar** a palavra-código.
- **Assinatura:** o @handle e o monograma da pessoa (de `01-empresa.md`), não fixos.
- Copie a estrutura exata dos `exemplo-*.html`.

### 5.3 CTA estratégico (funil)
O CTA promove **a isca/oferta DA PESSOA** (de `06-ofertas.md`) — nunca um produto de
terceiros. Palavra-código + o que ela entrega no direct. Ex. genérico: "Comenta [PALAVRA]
que eu te mando [a isca dela]". A lógica é: carrossel atrai → CTA leva pra isca → isca
aquece pra oferta.

### 5.4 Fotos
Banco: `contexto/fotos/` do projeto da pessoa.
- Capa e CTA SEMPRE com foto. Nunca repita a mesma foto no mesmo carrossel NEM entre os dois.
- Foto **preenche o quadro** (rosto no terço superior). Nada de pessoa pequena com fundo vazio —
  dê zoom via `background-size`/`background-position`.
- A caixa/texto **nunca** cobre o rosto.
- Prefira retratos bonitos e variados. Se não houver fotos, faça **tipográfico** (sem foto).

### 5.5 Copy sem cara de IA
Humana, aterrada na dor/desejo do cliente dela. Sem frase de efeito vazia; evite o padrão
repetido "não é X, é Y" (no máximo 1 por carrossel); itálico só em citação/ênfase real;
negrito nas palavras-chave, não pontilhado. Respeite palavras-marca e vetadas do `02-voz-e-tom.md`.
Áudio nas dicas: precisa estar **em alta E alinhado** ao posicionamento.

### 5.6 Render (Chrome headless, 1080×1350)
```powershell
$dir='conteudo/carrosseis/<pasta>'
$chrome='C:\Program Files\Google\Chrome\Application\chrome.exe'
foreach ($n in 1..8) {
  $html=Join-Path $dir "slide-$n.html"; $png=Join-Path $dir "slide-$n.png"
  $url='file:///'+($html -replace '\\','/')
  & $chrome --headless --disable-gpu --hide-scrollbars "--screenshot=$png" --window-size=1080,1350 --virtual-time-budget=12000 --force-device-scale-factor=1 $url 2>$null | Out-Null
}
```
Depois **leia os PNGs** da capa e de 1-2 slides e ajuste enquadramento/quebras de linha.

### 5.7 Legenda + hashtags + stories
Gere `legenda-e-stories.md` por carrossel (legenda: hook+arco+CTA; 8-12 hashtags do nicho
dela; 3-5 stories). CTA de comentar a palavra-código.

---

## FASE 6 · Índice e entrega
Crie `conteudo/carrosseis/<data>/00-resumo-da-semana.md` com: vídeo usado, link do Notion,
as 5 ideias e o caminho de cada carrossel. No topo: **"RASCUNHOS — revisar fotos,
enquadramento e copy antes de postar."** Entregue mostrando as capas.

---

## FASE 7 · Rodar toda segunda-feira (a parte automática)

A skill FAZ a busca + transcrição + tudo sozinha. Pra isso acontecer **toda segunda**, tem
dois caminhos:

**A) Confiável (recomendado):** toda segunda, abra o Claude na pasta do projeto e diga
**"roda a semana"**. A skill acha o vídeo em alta do seu nicho e faz o resto. 2 minutos de
clique, saída com revisão.

**B) Automático (avançado, Windows):** uma Tarefa Agendada semanal (segunda 10h) que chama
o Claude em modo headless rodando esta skill. Passos: (1) copie o `claude.exe` pra uma pasta
local acessível; (2) crie um `.cmd` que faz `type prompt.txt | claude.exe -p --dangerously-skip-permissions`;
(3) agende no Agendador (segunda 10h, "iniciar quando disponível" ligado, "não iniciar na
bateria" desligado). ⚠️ **Ressalva honesta:** o modo headless pode ser instável dependendo
da máquina (falta de console interativo trava o processo). Se travar, use o caminho A.

> Pra qualquer um dos dois, o PC precisa estar ligado na segunda.

---

## REGRAS DE OURO
1. **Sem marca fixa.** Leia SEMPRE o `contexto/` da pessoa. Nunca assuma nicho, voz, @handle,
   paleta ou oferta.
2. **Autocontida:** design em `references/template/`. Não chame outras skills.
3. **Sem Algrow:** WebSearch + transcrição local.
4. **Fiel aos fatos:** confirme dados/citações com WebSearch antes de afirmar.
5. **CTA na oferta DELA** (funil), nunca produto de terceiros. Ação = comentar palavra-código.
6. **Fotos:** preenchem o quadro, rosto acima da caixa, sem repetir, bonitas (ou tipográfico).
7. **Voz humana**, sem clichê de IA. Respeite palavras-marca/vetadas do contexto.
8. **Saída = rascunhos:** sinalize revisão antes de postar.
9. Autônoma → sem checkpoint. Com humano → mostre a copy antes de renderizar (texto é barato,
   render é caro).
