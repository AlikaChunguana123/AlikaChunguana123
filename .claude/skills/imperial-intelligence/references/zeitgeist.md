# Zeitgeist — detecção e qualificação

Como identificar e filtrar zeitgeist relevante pra marca. Não todo zeitgeist em alta
serve — só o que dialoga com tese e cliente.

---

## CATEGORIAS DE ZEITGEIST

### 1. Filmes em estreia
**Janela quente:** 7 dias antes ao 14 dias depois da estreia
**Como buscar:** "filmes estreia [mês ano]"
**Filtros:** descartar produções B, manter apenas com buzz cultural

### 2. Séries em alta
**Janela quente:** 14-30 dias após episódio bombástico ou final
**Como buscar:** "séries lançamento [mês ano]" + "séries finalizadas [mês]"
**Filtros:** descartar séries de nicho extremo

### 3. Lançamento literário
**Janela quente:** 14-21 dias após lançamento (ou primeiras semanas no Brasil se traduzido)
**Como buscar:** "livro lançamento [mês]" + "autora [tema]"
**Filtros:** verificar se autora é referência pro nicho

### 4. Eventos culturais
**Categorias:**
- Premiação (Met Gala, Oscar, Grammy, Cannes)
- Festival (Coachella, Tomorrowland)
- Convenção do nicho (Web Summit, RD Summit)
- Data significativa (aniversário Imperium, lançamento de marca)
**Janela quente:** 3 dias antes a 7 dias depois

### 5. Datas comemorativas
**Tier 1 (sempre relevantes):**
- Dia da Mulher (8/03)
- Dia das Mães (2º domingo de maio)
- Dia do Empreendedorismo Feminino (datas variam)
- Aniversário da própria marca

**Tier 2 (relevantes pra alguns nichos):**
- Black Friday
- Dia do Cliente
- Dia da Beleza
- Dia da Saúde Mental

**Tier 3 (cuidado):**
- Datas religiosas — só se a marca tem postura
- Datas políticas — geralmente evitar

### 6. Polêmicas/discussões viralizadas
**Janela quente:** 3-7 dias (passa rápido)
**Filtros rigorosos:**
- Dialoga com tese da marca?
- Pode adicionar valor ao debate (não só engajar com ódio)?
- Não viola `05-rejeicao.md`?

---

## QUERIES POR CATEGORIA

```
# Filmes
"filmes estreia [mês ano]"
"filmes mais aguardados [ano]"
"site:[fonte_cinema_referencia]"

# Séries
"séries lançamento [mês ano]"
"séries em alta [ano]"
"final de temporada [mês]"

# Eventos culturais
"[evento] [ano]" "data"
"agenda cultural [mês ano]"

# Datas
"datas comemorativas [mês]"
"calendário [setor] [ano]"

# Polêmicas
[Geralmente vem orgânico via WebSearch dos itens acima — não buscar diretamente]
```

---

## MAPA DE QUALIFICAÇÃO

Pra cada candidato a zeitgeist, aplicar 5 perguntas:

| # | Pergunta | Sim → | Não → |
|---|---|---|---|
| 1 | Janela ainda quente? (próximos 14 dias) | Continua | Descarta |
| 2 | Audiência principal conhece/se interessa? | Continua | Descarta |
| 3 | Dialoga com tese da marca (`01-empresa.md`)? | Continua | Descarta |
| 4 | Não viola `05-rejeicao.md`? | Continua | Descarta |
| 5 | Concorrentes ainda não saturaram? | **APROVADO** | Reconsidera ângulo único |

Apenas zeitgeists que passam em **5/5** entram no output.

Se passa em 4/5 e o item que falhou é #5 (saturação): registrar com nota
"Saturado por concorrentes — usar apenas com ângulo MUITO autoral".

---

## ÂNGULOS POR CATEGORIA

Pra cada categoria de zeitgeist, padrões de ângulo que funcionam pra marcas premium
femininas (adaptar conforme nicho da aluna):

### Filme/série
**Ângulos potentes:**
- Reframe da personagem feminina ("Glinda vs Elphaba não é vilã/heroína — é
  conformista vs protagonista")
- Cena específica como metáfora ("a cena onde X faz Y é exatamente como [tema da marca]")
- Subversão da leitura óbvia ("todo mundo lê de um jeito, eu leio de outro")

**Ângulos a evitar:**
- "Eu vi e amei" (sem tese)
- "10 lições do filme Y" (genérico)
- Spoilers na primeira semana

### Lançamento literário
**Ângulos potentes:**
- Citação de trecho + aplicação ao tema da marca
- Tese da autora como gancho pra tese da própria marca
- Crítica da abordagem da autora (se discordar — postura)

### Evento cultural
**Ângulos potentes:**
- Look de uma celebridade como gancho pra branding
- Discurso/frase memorável como gancho pra tese
- Comportamento observado (postura, recusa, escolha) como gancho

### Data comemorativa
**Ângulos potentes:**
- Reframe da data (não o óbvio "Dia das Mães é amor", mas "Dia das Mães é
  responsabilidade compartilhada")
- Manifesto de marca usando o gancho temporal
- Cliente que viveu/celebra a data de jeito particular

**Ângulos a evitar:**
- "Parabéns, mulheres incríveis!" (genérico)
- "Aproveita 30% off em homenagem ao [data]" (mercantilização)
- Tom institucional/corporate

### Polêmica
**Ângulos potentes (raros — usar com cuidado):**
- Tese da marca contra postura comum sobre a polêmica
- Recusa pública do debate ("não vou opinar sobre [polêmica X], mas vou opinar sobre
  o que a polêmica revela sobre [tema da marca]")

---

## ZEITGEIST × FUNÇÃO

| Categoria de zeitgeist | Função recomendada |
|---|---|
| Filme/série | Posicionar (reframe) ou Atrair (analogia) |
| Lançamento literário | Posicionar (resposta editorial) |
| Evento cultural | Atrair (hype) ou Reconectar (testemunho) |
| Data comemorativa | Reconectar (intimismo) ou Conversão (lançamento alinhado) |
| Polêmica | Posicionar (postura) — raro |

---

## INTEGRAÇÃO COM SKILLS DE CARROSSEL

Quando o zeitgeist é forte (filme estreando, evento iminente):
- Recomendar `carrossel-zeitgeist-bianca` se a aluna é Bianca/Castle
- Recomendar `imperial-carousel` com input `Zeitgeist:[nome]` pra outras marcas

Quando zeitgeist é menor (data comemorativa morna, série em alta mas não bombando):
- Sugerir como ÂNGULO de hook em conteúdo regular
- Não dedicar carrossel inteiro

---

## REGRA DE OURO

Zeitgeist é **acelerador de relevância**, não substituto de tese. Filme bom + sua tese
forte = post viral. Filme bom + tese fraca = ruído no feed.

Sempre perguntar: **"O que MINHA marca tem a dizer sobre isso?"**

Se resposta é "nada particular", o zeitgeist não é seu — passa.
