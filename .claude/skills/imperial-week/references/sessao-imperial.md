# Sessão Imperial — cronograma operacional de 45 minutos

A rotina semanal que transforma sábado em produção mensal de conteúdo. Como executar
a Sessão Imperial em 45 minutos bem usados.

> A Sessão Imperial é o ritual. 45 minutos uma vez por semana. Nunca mais "improvisar
> conteúdo na quarta às 23h".

---

## QUANDO RODAR

**Padrão:** sábado de manhã, entre 9h e 11h. A audiência está menos ativa, você opera
em paz, e o sistema gera conteúdo que sai a partir de segunda.

**Alternativas viáveis:**
- Domingo à noite (planejamento + relaxamento, conteúdo sai segunda)
- Sexta à tarde (encerramento da semana atual + planejamento da próxima)
- Qualquer dia FIXO toda semana — o importante é a regularidade

**A evitar:**
- Segunda de manhã (já tem segunda pra postar)
- Dias variáveis (perde ritual, vira "quando der")

---

## O QUE PRECISA TER ABERTO

Antes de começar, garantir que está pronta:

1. **Claude Code** rodando no projeto
2. **`contexto/` preenchido** (passaporte feito antes — não na hora)
3. **`conteudo/` existe** com pastas por formato
4. **Notion ou calendário editorial** aberto pra anotar

---

## CRONOGRAMA DE 45 MINUTOS

### MINUTO 0-5 — VARREDURA

**Comando:** `/imperial-intelligence`

**O que fazer:**
- Roda a skill de inteligência de mercado
- Recebe 5 temas em alta no nicho
- Identifica zeitgeist da semana (filme estreando, evento, data)
- Vê o que o concorrente principal postou na semana anterior

**Output esperado:**
- Lista de 5 temas com função sugerida (qual deles é Posicionar, qual é Atrair, etc.)
- 1 zeitgeist identificado (se houver) com janela temporal
- 1 lacuna no nicho (tema que ninguém tá tocando direito)

**Tempo realista:** 4-5 minutos.

---

### MINUTO 5-15 — PLANO DA SEMANA

**Comando:** `/imperial-week`

**Inputs:**
- Tema guarda-chuva (escolhido a partir da varredura)
- Etapa de funil dominante (sabe o que está vendendo no momento)
- Lançamento ativo? Sim/não
- Zeitgeist? Da varredura

**O que fazer:**
- Skill gera plano de 7 dias
- Mostra calendário, pauta detalhada, conexão narrativa
- **Aprova ou ajusta** pauta a pauta (5-10 min)

**Output esperado:**
- `conteudo/semanas/[data]-[slug]/plano.md` salvo
- Stories da semana planejados
- Pelo menos 1-2 dias-âncora identificados pra detalhar agora

**Tempo realista:** 8-10 minutos.

---

### MINUTO 15-30 — DETALHAMENTO DOS DIAS-ÂNCORA

**Comandos:**
- `/imperial-carousel Tema:[X] Função:[Y]` — pra carrosséis
- `/imperial-reel Tema:[X] Função:[Y] Formato:[talking-head/b-roll]` — pra reels
- `/imperial-post Frase:[X] Tipo:[tweet-post/quote]` — pra posts simples

**O que fazer:**
- Pega os 2-3 dias mais importantes da semana (geralmente o pico de venda + um Posicionar
  forte + um Reconectar pesado)
- Roda a skill específica pra cada um
- Aprova/ajusta o output

**Output esperado:**
- 2-3 conteúdos completos com copy + roteiro + design HTML
- Salvos em `conteudo/[formato]/[data]-[slug]/`

**Tempo realista:** 12-15 minutos.

> **Atenção:** não detalhar TODOS os 7 dias agora. Deixe os "menos críticos" como pauta
> e detalhe na hora de gravar/postar (geralmente 1-2 horas antes).

---

### MINUTO 30-40 — EXPORT DE PNGS

**Comando:** dependendo da skill, gera Playwright em batch.

**O que fazer:**
- Pra cada conteúdo de design (carrossel, post-frase) gerado: rodar export
- Playwright abre cada HTML em viewport 1080×1350 e tira screenshot
- PNGs salvos na pasta correspondente

**Output esperado:**
- 8-15 PNGs salvos (carrosséis têm 8 slides cada, posts simples têm 1)
- Pasta organizada por formato e data

**Tempo realista:** 8-10 minutos (Playwright é rápido, mas a primeira vez baixa Chromium
~1 min).

---

### MINUTO 40-45 — CALENDÁRIO E TRANSFERÊNCIA

**O que fazer:**
- Cola o plano da semana em Notion / Google Calendar / app de agendamento
- Marca dias e horários de publicação
- Transfere PNGs pro celular (AirDrop / iCloud / Google Drive)
- Confere stories planejados pra próxima segunda

**Output esperado:**
- Calendário editorial preenchido
- PNGs no celular, prontos pra publicar
- Próximas 24h sem dúvida do que postar

**Tempo realista:** 5 minutos.

---

## TOTAL: 45 MINUTOS

| Minuto | Etapa | Comando |
|---|---|---|
| 0-5 | Varredura | /imperial-intelligence |
| 5-15 | Plano | /imperial-week |
| 15-30 | Detalhamento | /imperial-carousel + /imperial-reel + /imperial-post |
| 30-40 | Export | Playwright (automático) |
| 40-45 | Calendário | Notion + transferência celular |

= **7 dias com design. 45 minutos. Todo sábado.**

---

## VARIAÇÕES DA SESSÃO

### Sessão Express (20 min)

Quando a semana é simples (tema claro, sem lançamento):

| Minuto | Etapa |
|---|---|
| 0-3 | Varredura express |
| 3-8 | Plano (modo simplificado) |
| 8-15 | Detalhar APENAS o pico de venda da semana |
| 15-20 | Export + calendário |

Os outros dias da semana entram só como pauta. Detalha cada um na hora de gravar/postar.

### Sessão Profunda (90 min)

Quando há lançamento ativo OU mês inteiro a planejar:

| Minuto | Etapa |
|---|---|
| 0-10 | Varredura ampla (5 dias de tendências) |
| 10-25 | Plano da semana atual |
| 25-50 | Detalhar 4-5 dias-âncora |
| 50-75 | Export todos os PNGs |
| 75-90 | Calendário detalhado + planejar próxima semana |

Use uma vez por mês ou no início de lançamento.

### Sessão de Recuperação (15 min)

Quando perdeu a Sessão Imperial e precisa improvisar:

| Minuto | Etapa |
|---|---|
| 0-3 | Tema guarda-chuva pegado da semana anterior |
| 3-8 | Plano simplificado de 5 dias (segunda a sexta) |
| 8-12 | Detalhar APENAS o post de quinta (próximo a postar) |
| 12-15 | Calendário + transferência |

Não ideal, mas melhor que improvisar sem método.

---

## ANTI-PADRÕES (NÃO FAZER)

### "Detalhar os 7 dias na sessão"
Tentação: deixar TUDO pronto. Realidade: 7 conteúdos detalhados em 45min = qualidade
fraca. Detalha 2-3 dias-âncora; deixa o resto como pauta + detalha 1-2h antes de
publicar.

### "Pular a varredura"
"Eu já sei o que vou postar." Talvez. Mas a varredura traz zeitgeist e vê o que está
em alta — sem ela, você posta no escuro.

### "Mudar o dia da Sessão toda semana"
Sábado essa semana, terça a outra. Vira "quando der", não vira ritual. O cérebro precisa
de constância pra criar disciplina sem força de vontade.

### "Operar com contexto vazio"
Se `contexto/` não está preenchido, a Sessão produz output genérico. Não tente compensar
escrevendo manualmente — isso destrói o ganho de tempo. Faça o passaporte ANTES.

### "Gerar conteúdo e não publicar"
Sessão completa, PNGs prontos, calendário no Notion — e não posta. Acontece. Pra evitar:
publicação automática via app (Buffer, Later, Metricool) OU lembrete específico ao
calendário.

---

## INDICADORES DE QUE A SESSÃO FUNCIONOU

Saída ideal da Sessão Imperial:

✅ Plano de 7 dias visível em uma tela
✅ Pelo menos 2 conteúdos com PNGs prontos pra publicar
✅ Stories planejados pra próximos 3 dias
✅ Você sai sem dúvida do que postar segunda

Saída de Sessão que falhou:

❌ Você ainda tá em dúvida sobre o tema
❌ Os PNGs não exportaram
❌ Os hooks não soaram como você
❌ Sentiu que precisa "voltar pra ajustar"

Se falhou: identificar o gargalo e ajustar a próxima sessão.

---

## REGRA DE OURO

A Sessão Imperial é uma **decisão semanal**. Você decide o que vai falar pra audiência
durante 7 dias, em 45 minutos.

Quando você não decide, o feed decide por você (você reage ao que está em alta, copia
trend, posta o que dá tempo). Decisão constante = marca constante.

45 minutos é o preço da consistência. Quem paga esse preço todo sábado, em 6 meses tem
audiência outra. Quem não paga, depois de 6 meses ainda tá perguntando "o que eu posto
hoje?".
