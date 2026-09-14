---
name: imperial-intelligence
description: |
  Skill de inteligência de mercado do sistema Imperium. Faz WebSearch pra detectar
  5 temas em alta no nicho + 1-2 zeitgeists relevantes (filme, evento, data) + 1
  lacuna no nicho + análise de até 3 concorrentes. Entrevista única no início,
  checkpoint do tema escolhido antes de finalizar, output estruturado em JSON que
  alimenta `/imperial-week` direto. Triggers: "/imperial-intelligence", "varredura",
  "o que está em alta no nicho", "análise de concorrência", "tendências",
  "zeitgeist da semana".
allowed-tools: Read, Write, Glob, Grep, WebSearch, WebFetch, Bash
---

# Imperial Intelligence

A única skill com componente real de pesquisa. Antes de criar conteúdo, saber o que
está em alta — e o que NÃO está sendo tocado direito.

> Ninguém posta no escuro depois que isso roda.

---

## QUANDO USAR

Use proativamente quando:
- Usuária pede `/imperial-intelligence`, "varredura", "o que está em alta"
- Sempre **antes** de `/imperial-week` (abre a Sessão Imperial)
- Início de novo ciclo (mensal, pré-lançamento)

---

## FLUXO DE EXECUÇÃO

### Etapa 1 — Entrevista única (4 itens em uma mensagem)

Use o que a usuária já mencionou. Pergunte só o que falta:

> "Pra varredura de mercado, preciso de 4 coisas (responde numa mensagem):
>
> 1. **Seu nicho** — qual o segmento específico? (ex: marketing premium feminino,
>    advocacia de família, terapia de casal, nutrição esportiva)
> 2. **Modo** — escolhe um:
>    - **Express (5min)** → só tendências + zeitgeist
>    - **Padrão (10min)** → + lacuna do nicho
>    - **Completo (15min)** → + análise de 3 concorrentes + métrica de saúde
> 3. **Concorrentes** (só se Completo) — me passa 3 perfis Instagram do nicho
> 4. **Janela temporal** — última semana ou último mês?"

Se a usuária já passou nicho/concorrentes em conversas anteriores OU nas instruções
do projeto Claude Code, use direto e pule a pergunta.

### Etapa 2 — Varredura de tendências (sempre)

Use **WebSearch** com 6 queries calibradas pelo nicho:

```
1. "[nicho]" tendências [mês atual] [ano atual]
2. "[nicho]" [ano próximo] novidade
3. site:[blog_referencia_1] OR site:[blog_referencia_2]
4. "[problema central do cliente]" "[ano atual]"
5. "[oferta principal]" como
6. "[tema central]" tendência
```

**Filtros de qualidade (descartar):**
- Conteúdo > 30 dias
- Fontes sem credibilidade (Buzzfeed-style, listicles vazios, sites de SEO)
- Genéricos ("Top 10 tendências de marketing 2026")
- Repetições (5 fontes mesma coisa = 1 tema único)

**Sintetizar em 5 temas em alta**, cada um com:

```markdown
### N. [Tema]
**Por que está em alta:** [1-2 frases — gatilho real, não vago]
**Função sugerida:** [Posicionar / Atrair / Conversão / Reconectar]
**Como dialoga com sua marca:** [1 frase]
**Ângulo único possível:** [1 ângulo que diferencia dos concorrentes]
```

### Etapa 3 — Detecção de zeitgeist (sempre)

Buscar:
- Filmes em estreia (próximas 2 semanas)
- Séries em alta (recém-lançada com buzz mensurável)
- Lançamento literário de autora referência
- Eventos culturais (Met Gala, Oscar, Cannes, eventos do nicho)
- Datas comemorativas (próximos 14 dias)
- Polêmicas viralizadas (SÓ se dialogam com tese da marca)

**Aplicar 5 perguntas pra qualificar:**

| # | Pergunta | Sim → | Não → |
|---|---|---|---|
| 1 | Janela ainda quente? (próximos 14 dias) | Continua | Descarta |
| 2 | Audiência principal conhece/se interessa? | Continua | Descarta |
| 3 | Dialoga com tese da marca? | Continua | Descarta |
| 4 | Não viola palavras vetadas da usuária? | Continua | Descarta |
| 5 | Concorrentes ainda não saturaram? | **APROVADO** | Ângulo único obrigatório |

Apenas 5/5 entra no output (1-2 zeitgeists). Não force inclusão se não passa.

```markdown
### Zeitgeist: [Filme/série/evento/data]
**O que é:** [1-2 frases]
**Janela:** [data início — data fim, com peak]
**Por que pega na sua audiência:** [conexão concreta]
**Ângulo possível:** [como sua marca pode usar — concreto, não abstrato]
```

### Etapa 4 — Lacuna do nicho (modo Padrão e Completo)

Cruze os 5 temas com posts dos concorrentes. Identifique:
- Temas em alta que concorrentes **IGNORAM**
- Temas em alta que abordam **mal** (raso, sem postura, copy genérica)
- Temas onde a tese da usuária resolve o vazio

```markdown
### Lacuna: [Tema]
**O que ninguém tá fazendo:** [1-2 frases]
**Por que tem espaço:** [1 frase]
**Como você ocupa:** [1 frase com ação concreta]
**Função recomendada:** [normalmente Posicionar — pede postura forte]
```

### Etapa 5 — Análise de concorrência (modo Completo)

Pergunte à usuária os 3 perfis. Pra cada um:

**Opção A** — Se a usuária tem **Claude in Chrome**: peça pra abrir extensão no
perfil e mandar o resumo dos últimos 9 posts.

**Opção B** — Se não tem: peça pra colar legendas dos últimos 9 posts no chat.

Pra cada perfil, captar:
- **Função dominante** (Posicionar/Atrair/Conversão/Reconectar)
- **Formato dominante** (carrossel/reel/post)
- **Frequência de venda direta**
- **Tom dominante** (mentora-firme / amiga-acessível / sharp-tech / etc.)
- **Frase-marca recorrente**
- **Ângulo recorrente**

**Sintetizar agregado:**
- O que **TODOS** fazem (saturação) → você EVITA
- O que **NENHUM** faz (espaço) → você OCUPA
- Diferenciação possível em 1-2 frases concretas

### Etapa 6 — Métrica de saúde (modo Completo)

Avaliação rápida do nicho:
- **Saturação geral** (Alta / Média / Baixa)
- **Espaço editorial** (Lotado / Equilibrado / Aberto)
- **Volume de venda direta** nos concorrentes (Alto / Médio / Baixo)

**Recomendação estratégica:**
- Saturação alta → **Posicionar** com tese contra-corrente
- Saturação baixa → **Atrair** (espaço pra crescer rápido)
- Venda direta alta nos outros → **Reconectar** (humaniza enquanto eles vendem)
- Espaço editorial aberto → **lacuna identificada** vira tema-âncora

### Etapa 7 — Validar pelos filtros (incluindo filtro 10)

Antes de mostrar à usuária, passar os 5 temas + zeitgeist + lacuna pelo filtro 10:
- Nenhum tema sugerido pode usar padrão "X é Y, não Z" abstrato
- Nenhum tema pode ser frase de efeito vazia ("decola suas vendas",
  "potencializa seu negócio", "destrava o crescimento")
- Toda sugestão tem **cena concreta** ou **verbo transitivo** + objeto específico

Se algum tema falha no filtro, regenere com ângulo concreto.

### Etapa 8 — Output consolidado + MINI-CHECKPOINT do tema

```markdown
# Inteligência da Semana — [DATA]

**Nicho:** [...]  ·  **Modo:** [Express / Padrão / Completo]  ·  **Janela:** [última semana / mês]

---

## TL;DR — Sugestão da skill

**Meu candidato a tema da semana:** "[tema escolhido]"
**Por quê:** [1-2 frases — combinação de em alta + lacuna + ângulo único]
**Função sugerida:** [Posicionar / Atrair / Conversão / Reconectar]

---

## 1. Os 5 temas em alta
[lista detalhada de cada um]

## 2. Zeitgeist da semana
[se houver — 1-2 candidatos]

## 3. Lacuna do nicho (modo Padrão+)
[se identificada]

## 4. Análise de concorrência (modo Completo)
[se aplicável]

## 5. Métrica de saúde (modo Completo)
[se aplicável]

---

## ESCOLHA O TEMA-ÂNCORA DA SEMANA

Qual desses vira o tema guarda-chuva pro `/imperial-week`?
- "tema [N]" → vou com o tema da lista
- "zeitgeist" → vou com o zeitgeist como tema
- "lacuna" → vou com a lacuna
- "[outro tema]" → você descreve um diferente baseado no que viu

(Default: meu candidato no TL;DR se você só disser "ok")
```

### Etapa 9 — Salvar output estruturado pra `/imperial-week` consumir

Após a aluna escolher o tema, salve:

```bash
mkdir -p conteudo/inteligencia-[YYYY-WXX]
```

Crie `conteudo/inteligencia-[YYYY-WXX]/inteligencia.json`:

```json
{
  "data_varredura": "2026-05-11",
  "semana": "2026-W19",
  "nicho": "marketing premium feminino",
  "modo": "Completo",
  "janela": "última semana",
  "tema_escolhido": {
    "titulo": "Premium se prova pelo que recusa",
    "fonte": "lacuna identificada",
    "funcao_sugerida": "Posicionar",
    "etapa_sugerida": "Meio",
    "angulo_unico": "[1 frase concreta]"
  },
  "temas_em_alta": [
    { "tema": "...", "porque": "...", "funcao": "...", "angulo": "..." },
    ...
  ],
  "zeitgeists": [
    { "tipo": "filme", "nome": "...", "janela": "...", "angulo": "..." }
  ],
  "lacuna": {
    "tema": "...",
    "espaco": "...",
    "como_ocupa": "..."
  },
  "concorrencia": {
    "perfis": ["@perfil1", "@perfil2", "@perfil3"],
    "saturacao": "Alta",
    "todos_fazem": "...",
    "ninguem_faz": "...",
    "diferenciacao": "..."
  },
  "metrica_saude": {
    "saturacao_geral": "Alta",
    "espaco_editorial": "Lotado",
    "venda_direta_concorrentes": "Alto",
    "recomendacao_estrategica": "Posicionar com tese contra-corrente"
  }
}
```

### Etapa 10 — Próximo passo

```markdown
## ✓ Inteligência consolidada

**Tema escolhido:** "[tema]"
**Função sugerida:** [...]
**Salvo em:** `conteudo/inteligencia-[YYYY-WXX]/inteligencia.json`

### Próximo passo:
Roda `/imperial-week` — vou ler o JSON e já passar TODO o contexto da varredura
direto pro plano semanal. Você não precisa repetir nada.
```

---

## REGRAS DE OURO

1. **Não dependa de arquivos externos.** Use a conversa atual + WebSearch.

2. **5 temas, não 50.** Curadoria é o produto — não despeje tudo o que achou.

3. **Zeitgeist passa pelo filtro.** Só o que dialoga com tese E cliente. 5/5 ou descarta.

4. **Lacuna é ouro.** Se identificada, vira candidato #1 a tema.

5. **Análise de concorrência operacional, não psicográfica.** Foco em
   função/formato/tom — dados, não suposições.

6. **Saturação dos outros = espaço pra Reconectar.** Inverso também vale.

7. **WebSearch tem limites.** Máximo 8-10 queries por execução. Não desperdice.

8. **Filtro 10 (anti-frase-de-efeito)** aplicado aos temas sugeridos. Tema com cara
   de mentor IG ("destrava potencial", "alavanca vendas") = regenerar com cena concreta.

9. **Mini-checkpoint do tema** antes de finalizar. A aluna escolhe entre as opções
   apresentadas — não decida sozinho.

10. **Output estruturado em JSON.** Alimenta `/imperial-week` direto, sem retrabalho
    de entrevista.

11. **Entrevista única** — 4 itens em uma mensagem.

---

## REGRA DE OURO META

`imperial-intelligence` é o **olho do sistema**. Sem ela, a usuária opera com base
em percepção (que envelhece) ou memória (que distorce).

Critério de sucesso:
- A aluna sai com tema **escolhido** (não "vou pensar")
- O tema está conectado a algo em alta
- Tem 1 ângulo que NÃO é o que os concorrentes fazem
- JSON salvo alimenta `/imperial-week` automaticamente
- Tempo total: 5-15 min conforme o modo
