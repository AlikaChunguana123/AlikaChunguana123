---
name: imperial-week
description: |
  Skill orquestradora do sistema Imperium. Pega um tema guarda-chuva e gera plano
  de 7 dias coordenados pro Instagram com pauta detalhada (story, reel, post,
  carrossel) + função declarada (Posicionar/Atrair/Conversão/Reconectar) +
  audiência alvo + hook + CTA por dia. APÓS APROVAÇÃO, cria 7 scheduled tasks que
  rodam automaticamente todo dia no horário escolhido — Claude executa o conteúdo
  do dia (carrossel/reel/post) com contexto pré-definido, gera PNG/roteiro e salva
  em pasta organizada por data. Aluna não precisa dar comandos durante a semana.
  Triggers: "/imperial-week", "semana inteira", "planejar semana", "7 dias de
  conteúdo", "calendário editorial", "pauta da semana".
allowed-tools: Read, Write, Glob, Grep, WebSearch, WebFetch, Bash
---

# Imperial Week

A skill que transforma 45 minutos em **7 dias de conteúdo automatizado**.

> Você senta uma vez. A semana inteira roda sozinha.

---

## QUANDO USAR

Use proativamente quando:
- Usuária pede `/imperial-week`, "planejar semana", "pauta da semana"
- Sábado/domingo (rotina padrão da Sessão Imperial)
- Início de lançamento ou mudança de ciclo

NÃO use quando:
- Pede 1 conteúdo isolado (use a skill específica)
- Pede planejamento mensal (rode imperial-week 4× sequencial)

---

## FLUXO DE EXECUÇÃO

### Etapa 1 — Entrevista única (10 itens em uma mensagem, 3 blocos)

> "Pra planejar essa semana e agendar a execução automática, preciso de 10 coisas
> (responde tudo numa mensagem só):
>
> **SOBRE O CONTEÚDO DA SEMANA:**
>
> 1. **Tema guarda-chuva** — UMA pergunta que orienta os 7 dias (ex: 'premium não é preço, é tese')
> 2. **Etapa de funil dominante** — Topo (atrair fria) / Meio (nutrir morna) / Fundo (lançamento ativo) / Pós-conversão (alto-ticket)
> 3. **Lançamento ativo?** Se sim: produto, preço, prazo
> 4. **Sobre você** — 2 frases (o que vende, pra quem) + voz/palavras-marca/vetadas
> 5. **Zeitgeist relevante?** — filme estreando, evento, data comemorativa que dialoga com o tema (opcional)
>
> **SOBRE A IDENTIDADE VISUAL** (pra passar pras outras skills sem você precisar repetir):
>
> 6. **Estilo** — Editorial Quiet (Vogue) / Minimalist Bold (NYT) / Warm Premium (Aesop)
> 7. **Cor primária HEX** — pra paleta da marca
> 8. **Fotos editoriais** — onde estão? (ideal 5 fotos)
> 9. **Assinatura** — nome + monograma (1 letra) + sub-marca
>
> **SOBRE O AGENDAMENTO AUTOMÁTICO:**
>
> 10. **Horário diário** — que horas o Claude deve gerar o conteúdo do dia automaticamente? (sugiro 9h da manhã pra você revisar antes do meio-dia)"

### Etapa 2 — Aplicar mix por etapa

Baseado na etapa de funil declarada, aplique o template de mix.

#### MEIO (padrão entre lançamentos)

| Dia | Formato | Função | Audiência |
|---|---|---|---|
| SEG | Story + Post | Posicionar | Morna |
| TER | Reel | Atrair | Fria |
| QUA | Post | Posicionar | Morna |
| QUI | Story + Reel | Atrair | Fria |
| SEX | Carrossel | Conversão (lead magnet) | Morna |
| SÁB | Reel | Posicionar | Morna |
| DOM | Post | Reconectar | Morna/Quente |

#### TOPO (semana de aquecimento)

| Dia | Formato | Função | Audiência |
|---|---|---|---|
| SEG | Story + Post | Atrair | Fria |
| TER | Reel | Atrair | Fria |
| QUA | Carrossel | Atrair | Fria |
| QUI | Reel | Atrair | Fria |
| SEX | Post | Posicionar | Morna |
| SÁB | Reel | Atrair | Fria |
| DOM | Post | Reconectar | Morna |

#### FUNDO (lançamento ativo)

| Dia | Formato | Função | Audiência |
|---|---|---|---|
| SEG | Story + Carrossel | Conversão | Quente |
| TER | Reel | Conversão | Quente |
| QUA | Post | Posicionar | Morna |
| QUI | Reel | Conversão | Quente |
| SEX | Carrossel | Conversão (última chamada) | Quente |
| SÁB | Reel | Conversão | Quente |
| DOM | Post | Reconectar | Quente |

#### PÓS-CONVERSÃO (alto-ticket)

| Dia | Formato | Função | Audiência |
|---|---|---|---|
| SEG | Post | Posicionar | Quente |
| TER | Reel | Reconectar | Quente |
| QUA | Carrossel | Posicionar | Quente |
| QUI | Story + Post | Conversão (alto ticket) | Quente |
| SEX | Reel | Reconectar | Quente |
| SÁB | Carrossel | Conversão (alto ticket) | Quente |
| DOM | Post | Posicionar | Quente |

### Etapa 3 — Gerar overview semanal

```markdown
# SEMANA [YYYY-WXX]: [Tema guarda-chuva]

**Etapa dominante:** [...]  ·  **Lançamento ativo:** [sim/não]  ·  **Estilo visual:** [...]
**Agendamento:** todo dia às [HH:MM] · Total: 7 tasks

## Calendário

| Dia | Data | Formato | Função | Audiência | Tema do dia |
|---|---|---|---|---|---|
| SEG | DD/MM | ... | ... | ... | ... |
| TER | DD/MM | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |

## Arco da semana
- **Abertura:** [como SEG entra no tema guarda-chuva]
- **Desenvolvimento:** [TER-QUI desenvolvem]
- **Pico:** [SEX se Fundo, ou peça-âncora]
- **Reflexão:** [DOM Reconectar fecha]
```

### Etapa 4 — CHECKPOINT A: aprovar overview ANTES de detalhar

```markdown
**O calendário tá certo? Posso detalhar cada dia (hook, CTA, conexão narrativa)?**

- "aprova" → detalho os 7 dias
- "troca [DIA] pra [formato/função]" → ajusto antes
- "muda etapa pra [X]" → aplico outro mix
- "outro arco" → repenso a narrativa da semana
```

### Etapa 5 — Pauta detalhada por dia

Pra cada um dos 7 dias:

```markdown
## SEG — DD/MM

**Formato:** [Story / Reel / Carrossel / Post]
**Função:** [Posicionar / Atrair / Conversão / Reconectar]
**Audiência alvo:** [Fria / Morna / Quente]
**Tema do dia:** [recorte específico do tema guarda-chuva]
**Hook escolhido:** "[hook em 1 frase autoral]"
**CTA:** [específico da etapa de funil]
**Conexão narrativa:** [como liga ao dia anterior e próximo]
**Stories de apoio (3-5):** [...]
```

### Etapa 6 — Aplicar 10 filtros antes do checkpoint B

Ver `references/filtros.md`:
1-9: filtros universais (palavras vetadas, CTAs proibidos, AI-flavored, etc.)
10: **Anti-frase-de-efeito vazia** (CRÍTICO — toda headline tem cena concreta)

### Etapa 7 — CHECKPOINT B: aprovar pauta detalhada

```markdown
**Pauta detalhada da semana. Tudo certo pra eu agendar a execução automática?**

- "aprova" → crio as 7 scheduled tasks e a semana começa a rodar sozinha
- "ajusta [DIA]" → refaço só esse dia (hook, CTA, tema)
- "muda tom pra [adjetivo]" → recalibro voz na semana toda
- "regenera tudo" → outra abordagem
```

### Etapa 8 — Salvar plano estruturado

Salve o plano em formato consumível pelas scheduled tasks:

```bash
mkdir -p conteudo/semana-[YYYY-WXX]
```

Crie `conteudo/semana-[YYYY-WXX]/plano.json`:

```json
{
  "tema_guarda_chuva": "Premium não é preço, é tese",
  "etapa": "Meio",
  "lancamento_ativo": false,
  "estilo_visual": "editorial-quiet",
  "paleta_primaria": "#1F0D23",
  "fotos_path": "fotos/",
  "assinatura": {
    "nome": "Bianca Freitas",
    "monograma": "B",
    "sub_marca": "Mentoria Castle"
  },
  "voz": {
    "palavras_marca": ["imperadora", "tese", "categoria"],
    "palavras_vetadas": ["amiga", "linda", "potencializar"]
  },
  "dias": [
    {
      "data": "2026-05-12",
      "dia_semana": "SEG",
      "formato": "post",
      "tipo_post": "tweet-post",
      "funcao": "Posicionar",
      "audiencia": "Morna",
      "tema_do_dia": "Premium se prova pelo que recusa",
      "hook": "Você cobra alto e ouve 'cabe parcelar?'",
      "cta": "Comente CADERNO",
      "conexao": "Abre a semana com a tese central",
      "stories": [
        "Aquecimento: pergunta-caixinha",
        "Teaser visual",
        "Print da capa"
      ]
    },
    {
      "data": "2026-05-13",
      "dia_semana": "TER",
      "formato": "reel",
      "formato_reel": "talking-head",
      "duracao": "30s",
      "funcao": "Atrair",
      ...
    },
    ...
  ]
}
```

### Etapa 9 — Criar 7 scheduled tasks

Pra cada um dos 7 dias, use `mcp__scheduled-tasks__create_scheduled_task` com:

**Schedule:** `cron` no horário escolhido + dia específico
- Ex: `0 9 12 5 *` (todo 12 de maio às 9h) — mas usar formato adequado da MCP

**Prompt da task:**

```
Você está rodando como scheduled task da imperial-week.

Hoje é [DIA_SEMANA] [DD/MM/YYYY].

LEIA o plano completo em `conteudo/semana-[YYYY-WXX]/plano.json` e execute o conteúdo do dia.

Contexto do dia:
- Formato: [post/reel/carrossel]
- Função: [Posicionar/Atrair/Conversão/Reconectar]
- Tema do dia: [...]
- Hook: [...]
- CTA: [...]

Identidade visual (já definida no plano):
- Estilo: [editorial-quiet / minimalist-bold / warm-premium]
- Paleta primária: [#HEX]
- Fotos: [path]
- Assinatura: [nome / monograma / sub-marca]

AÇÃO:
1. Invoque /imperial-[carousel|reel|post] com TODO o contexto acima
2. PULE A ENTREVISTA — tudo já está definido no plano
3. PULE O CHECKPOINT — copy aprovada pela aluna na sessão semanal
4. Gere o conteúdo direto (PNG ou roteiro)
5. Salve em `conteudo/[YYYY-MM-DD]/` (pasta do dia)
6. Crie um arquivo `conteudo/[YYYY-MM-DD]/status.md` indicando "Conteúdo do dia pronto"

Stories de apoio do dia também devem ser gerados e salvos em `conteudo/[YYYY-MM-DD]/stories.md`.
```

### Etapa 10 — Confirmar entrega e mostrar resumo

```markdown
## ✓ Semana agendada com sucesso

**Tema:** [...]
**Etapa:** [...]
**Estilo visual:** [...]
**Horário diário:** [HH:MM]

### Calendário com agendamentos:
| Dia | Data | Formato | Horário | Status |
|---|---|---|---|---|
| SEG | 12/05 | Post | 09:00 | ⏰ Agendado |
| TER | 13/05 | Reel | 09:00 | ⏰ Agendado |
| ... | ... | ... | ... | ⏰ Agendado |

### Plano completo salvo em:
`conteudo/semana-[YYYY-WXX]/plano.json`

### Como funciona daqui pra frente:
- **Todo dia às [HH:MM]**, abra o Claude Code
- O task do dia dispara automaticamente
- O Claude gera o conteúdo (PNG ou roteiro) na pasta `conteudo/[DATA]/`
- Você abre, revisa em 5min, posta

### Algo pra ajustar?
- "cancela agendamento" → removo as 7 tasks
- "muda horário" → atualizo as 7 tasks
- "regenera plano" → refazemos a semana
```

---

## IMPORTANTE — limitação de scheduled tasks

**Scheduled tasks do Claude Code precisam que o Claude Code esteja acessível na hora.**
Se a aluna não abrir o Claude Code num dia, a task daquele dia fica pendente e dispara
quando ela abrir.

Avise isso explicitamente ao apresentar o resumo final:

> "Importante: pra a automação funcionar, abra o Claude Code todo dia perto do horário
> agendado. Se você fechar a semana inteira, as tasks ficam pendentes e disparam todas
> quando você abrir."

---

## REGRAS DE OURO

1. **Tema guarda-chuva é não-negociável.** Sem tema central, recuse e ajude a destilar.

2. **Mix coerente com etapa.** "Semana de venda" com 5 Atrair = falha. Recalibre.

3. **Variedade obrigatória** de formato. 7 carrosséis seguidos = falha.

4. **Story todo dia.** Conteúdo principal varia, story é diário.

5. **CTA da etapa de funil.** Topo → lead magnet. Fundo → palavra-código/checkout.

6. **Função declarada por dia.** UMA por dia, não "Posicionar + Conversão no mesmo".

7. **Reconectar uma vez por semana.** Domingo é o dia natural.

8. **Sequência narrativa, não lista.** Os 7 dias contam UMA história.

9. **Lançamento muda regras.** Fundo de funil tem prioridade.

10. **Filtro 10 (anti-frase-de-efeito) é CRÍTICO** — passar todas as headlines/hooks
    pelo teste da cena concreta antes de aprovar.

11. **2 checkpoints obrigatórios:**
    - **Checkpoint A** após overview (calendário 7 dias)
    - **Checkpoint B** após pauta detalhada (hooks + CTAs)

12. **Entrevista única** — 10 itens em uma mensagem. Pra a aluna passar TODA a info
    visual + verbal pra que as scheduled tasks não precisem perguntar nada depois.

13. **Plano salvo em JSON estruturado** — pra que cada scheduled task leia o contexto
    do dia sem ambiguidade.

14. **Scheduled tasks com prompt completo** — cada task tem TODO o contexto pra
    invocar a skill correta pulando entrevista e checkpoint.

---

## REGRA DE OURO META

A imperial-week é a skill que **transforma cliente em fã do sistema**. É aqui que a
aluna percebe que pode **operar conteúdo sem dar comando toda semana** — só uma
sessão de 30min por semana e o resto roda sozinho.

Critério de sucesso:
- A aluna sai com plano CONCRETO + 7 tasks agendadas
- O plano tem ARCO emocional
- Respeita ETAPA do funil
- A aluna pode fechar o Claude Code e abrir só de manhã durante a semana
- Cada dia ela tem o conteúdo pronto na pasta — só revisa e posta
