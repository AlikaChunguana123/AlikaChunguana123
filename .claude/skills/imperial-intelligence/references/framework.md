# Framework Imperial Intelligence

5 categorias de inteligência de mercado + lógica de priorização. Como pensar
varredura semanal sem se perder no volume de informação.

---

## AS 5 CATEGORIAS DE INTELIGÊNCIA

### Categoria 1 — TENDÊNCIAS (sempre)
**O que captura:** temas em alta no nicho específico, semana atual.
**Fontes:** sites de referência do nicho, perfis influentes, hashtag analysis.
**Output:** 5 temas com função sugerida.

### Categoria 2 — ZEITGEIST (sempre)
**O que captura:** filme estreando, série bombando, evento, data, polêmica viralizada.
**Fontes:** Google Trends, agenda cultural, datas oficiais.
**Output:** 1-2 zeitgeists relevantes pra marca.

### Categoria 3 — LACUNA (modo Padrão e Completo)
**O que captura:** tema que ninguém aborda direito = oportunidade de categoria.
**Fontes:** cruzamento de tendências × concorrentes × tese da marca.
**Output:** 1 lacuna identificada.

### Categoria 4 — CONCORRÊNCIA (modo Completo)
**O que captura:** padrões dos 3 concorrentes principais nos últimos 9 posts.
**Fontes:** WebFetch ou análise guiada via Claude in Chrome.
**Output:** análise de 3 perfis + padrões agregados + espaço de diferenciação.

### Categoria 5 — MÉTRICA DE NICHO (modo Completo)
**O que captura:** saúde geral do nicho — saturação, espaço editorial, comportamento de venda.
**Fontes:** análise qualitativa do que foi coletado nas categorias 1-4.
**Output:** recomendação estratégica de posicionamento.

---

## LÓGICA DE PRIORIZAÇÃO

Em uma execução padrão (~10min), priorizar:

1. **Tendências (sempre)** — base de qualquer planejamento
2. **Zeitgeist (sempre)** — janela temporal limitada, perde se atrasa
3. **Lacuna** — gera diferenciação imediata
4. **Concorrência** — útil mas pesa no tempo
5. **Métrica** — síntese de tudo, opcional

Modo Express: só 1 e 2.
Modo Padrão: 1, 2, 3.
Modo Completo: 1, 2, 3, 4, 5.

---

## REGRAS DE FONTE DE DADOS

### O que vale buscar
- Sites de referência do nicho (cadastrados em `intelligence-config.md`)
- Posts de concorrentes específicos (cadastrados)
- Eventos oficiais (datas comemorativas, lançamentos culturais)
- Hashtags do nicho (com cautela — podem ser inflacionadas)

### O que NÃO vale buscar
- Tudo do Twitter/X (saturado de ruído, baixa qualidade)
- Buzzfeed/clickbait
- "Top 10 tendências que vão mudar o marketing em 2026" (genéricos)
- Sites com SEO inflado mas conteúdo raso

### Como filtrar resultados
1. Data: descartar > 30 dias (a menos que seja análise de longo prazo)
2. Fonte: descartar sem credibilidade clara
3. Relevância: descartar sem conexão com cliente ideal
4. Originalidade: descartar repetição (5 fontes dizendo a mesma coisa = 1 tema)

---

## ANATOMIA DE UM TEMA EM ALTA BEM IDENTIFICADO

Cada tema do output deve responder:

1. **O QUE é o tema?** (1 frase clara, sem clichê)
2. **POR QUE está em alta?** (gatilho real — evento, polêmica, sazonalidade)
3. **HÁ QUANTO TEMPO?** (janela: emergente / em pico / em queda)
4. **PARA QUEM IMPORTA?** (qual segmento do cliente ideal se identifica)
5. **QUE ÂNGULO É ÓBVIO?** (pra evitar — todo mundo já tá batendo)
6. **QUE ÂNGULO É AUTORAL?** (pra explorar — sua tese sobre)

Se um tema não responde essas 6 perguntas, NÃO entra no output. Tema vago = ruído.

---

## ZEITGEIST — MAPA DE QUALIFICAÇÃO

Pra cada zeitgeist candidato, avaliar:

| Pergunta | Sim | Não |
|---|---|---|
| Janela ainda quente? (últimos 14 dias) | ✅ usar | ❌ tarde demais |
| Audiência principal conhece? | ✅ relevante | ❌ obscuro pra ela |
| Dialoga com tese da marca? | ✅ usar | ❌ desconectado |
| Não bate com `05-rejeicao.md`? | ✅ permitido | ❌ filtrado |
| Concorrentes ainda não saturaram? | ✅ espaço | ❌ saturado |

Apenas zeitgeists que passam em **todas as 5** entram no output.

---

## LACUNA — COMO DETECTAR

Lacunas são raras e valiosas. Aparecem quando:

### Padrão A — Tema importante ignorado
Os 5 temas em alta incluem algo relevante pro cliente, mas os concorrentes IGNORAM.

**Exemplo:** "como precificar serviço durante pandemia". Cliente precisa saber — concorrentes evitam.

### Padrão B — Tema mal abordado
Os concorrentes tocam o tema mas raso, sem postura, sem prova.

**Exemplo:** "IA pra empreendedoras". Todos falam genérico ("o futuro é IA"). Você fala método ("IA com passaporte").

### Padrão C — Tema sob ângulo errado
Concorrentes abordam pelo ângulo X. Você tem tese pelo ângulo Y, mais rico.

**Exemplo:** todos falam "como Conversão mais". Você fala "como recusar mais clientes". Mesmo nicho, ângulo invertido.

### Padrão D — Tema sob plataforma errada
Concorrentes saturaram um formato. Você abre outro.

**Exemplo:** todos fazem reels frenéticos. Você faz carrossel reflexivo. Mesmo conteúdo, outro lugar.

---

## CONCORRÊNCIA — O QUE OBSERVAR

Análise não é estudo psicográfico. É **observação operacional**.

### Em cada perfil de concorrente, captar:

1. **Função dominante** — Posicionar / Atrair / Conversão / Reconectar (frequência %)
2. **Formato dominante** — quantos reels vs carrosséis vs posts simples
3. **Frequência de venda direta** — X em 9 posts
4. **Tom dominante** — premium-quiet / didático / agressivo / vulnerável
5. **Ângulo recorrente** — qual viés temático aparece sempre
6. **Frase-marca** — qual expressão/manifesto se repete

### Não captar (irrelevante):
- Quantidade de seguidores
- Engajamento absoluto
- Identidade visual deles (você não vai copiar)
- Vida pessoal deles

### Saída útil

> "@concorrente1 faz 60% Posicionar, 30% Atrair, 10% Conversão. Tom é mentora-acessível.
> Frase-marca: '[X]'. Ângulo recorrente: [Y]. Vende direto pouco — só em lançamento."

---

## REGRA DE OURO

Inteligência boa **filtra**, não acumula. Se o output tem 20 temas, 10 zeitgeists e 5
lacunas, a aluna não usa nada — vira sobrecarga.

5 temas. 1-2 zeitgeists. 1 lacuna. Pronto.

Curadoria é o produto.
