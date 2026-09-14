---
name: passaporte-imperial
description: |
  Skill de onboarding do sistema Imperium. Conduz uma entrevista estruturada com a usuária
  pra preencher os 7 arquivos de `contexto/` + identidade visual, que servem de base pra
  TODAS as outras skills (imperial-carousel, imperial-reel, imperial-week,
  imperial-intelligence, imperial-post) operarem na voz dela. Use quando: a usuária acabou
  de abrir um projeto novo no Claude Code, ou quando quer atualizar uma camada específica
  do contexto. Triggers: "/passaporte-imperial", "configurar passaporte", "preencher contexto",
  "começar do zero", "atualizar minha voz", "atualizar cliente ideal", "passaporte imperial".
allowed-tools: Read, Write, Glob, Grep, Bash
---

# Passaporte Imperial

A skill de onboarding do sistema Imperium. Define quem a usuária é em sete arquivos de
contexto + um de identidade visual, antes de qualquer outra skill rodar.

> Sem passaporte, toda skill chuta. Com passaporte, toda skill opera.

---

## QUANDO USAR

Use proativamente quando:

- A usuária acabou de instalar Claude Code e abriu um projeto novo (a pasta `contexto/`
  está vazia ou inexistente)
- A usuária menciona "configurar passaporte", "/passaporte-imperial", "começar do zero",
  "preencher contexto"
- A usuária quer atualizar UM arquivo específico ("atualizar minha voz", "refazer cliente
  ideal")
- A usuária trouxe memória do ChatGPT (`contexto/memoria-importada.md` existe) e quer
  organizar isso nos sete blocos certos

**NÃO use** quando:

- A pasta `contexto/` já está completa E a usuária quer CRIAR conteúdo. Nesse caso, redirecione
  pra skill apropriada (`/imperial-carousel`, `/imperial-reel`, etc.)

---

## CHECKPOINT INICIAL — antes de qualquer pergunta

Faça três verificações silenciosas (sem perguntar à usuária ainda):

### 1. `contexto/memoria-importada.md` existe?

Se SIM, leia o arquivo inteiro. Use como matéria-prima — você já tem 60-80% do passaporte
respondido. **Não repita perguntas que ela já respondeu lá.** Use o conteúdo pra preencher
os arquivos diretamente, e só faça follow-up no que estiver vago ou faltando.

### 2. Quais dos 7 arquivos já existem em `contexto/`?

Use `Glob` em `contexto/*.md`. Liste o que existe vs o que falta.

### 3. Existe `contexto/05-identidade-visual.md`?

Se sim, identidade visual está capturada (não precisa repetir). Se não, vai ser a última
etapa do onboarding.

---

## ABERTURA — primeira mensagem à usuária

Use exatamente este tom (calibrado pra a marca premium-editorial-imperial):

> Antes de o Claude virar funcionário pleno do seu negócio, ele precisa te conhecer.
> Não é prompt bonito, é base de conhecimento de verdade.
>
> Vou te conduzir por **sete arquivos**. Cada um responde uma camada do que você é.
> No fim, qualquer skill que rodar (carrossel, reel, semana inteira) lê tudo isso antes
> de escrever uma única linha.
>
> Antes de começarmos, escolha o modo:
>
> **Express** — uma pergunta-chave por arquivo, ~15 minutos. Bom pra primeira passada.
>
> **Completo** — 4 a 6 perguntas por arquivo com follow-ups, ~45 minutos. Recomendado se
> você nunca articulou esses pontos por escrito.
>
> Qual?

Adapte se houver memória importada:

> Vi que você já trouxe a memória do ChatGPT (`memoria-importada.md`). Boa — vou usar
> ela como base e só te perguntar o que estiver faltando ou vago. Vai ser mais rápido.

---

## OS 8 ARQUIVOS DO PASSAPORTE

| # | Arquivo | O que captura | Skills que leem |
|---|---|---|---|
| 01 | `contexto/01-empresa.md` | Nome, nicho, posicionamento de mercado | todas |
| 02 | `contexto/02-voz-e-tom.md` | Como você fala. Palavras que usa, rejeita, ritmo | todas |
| 03 | `contexto/03-cliente-ideal.md` | Para quem você fala. Dor, desejo, DM | todas |
| 04 | `contexto/04-diferenciais.md` | O que só você entrega, com prova | carousel, reel, post |
| 05 | `contexto/05-rejeicao.md` | O que NUNCA pode aparecer no seu conteúdo | filtro de TODAS |
| 06 | `contexto/06-ofertas.md` | Produtos, preços, lotes, CTA por etapa de funil | reel, post, week |
| 07 | `contexto/07-historia.md` | Trajetória, viradas, manifesto pessoal | carousel (reconectar), post |
| 08 | `contexto/05-identidade-visual.md` | Paleta HEX, fontes, logo, estilo visual | carousel, post (design) |

> Nota sobre numeração: o arquivo de identidade visual mantém prefixo `05-` por compatibilidade
> com a skill `instagram-carousel` (que lê `05-identidade-visual.md`). Os arquivos textuais 04,
> 05, 06, 07 referem-se aos blocos do passaporte.

---

## EXECUÇÃO PASSO A PASSO

### Etapa 1 — Carregar referências internas

Leia, em ordem:

1. `references/perguntas.md` — banco de perguntas por arquivo, com follow-ups
2. `references/formato-arquivos.md` — template/estrutura de cada .md de contexto
3. `references/exemplo-bianca.md` — exemplo completo preenchido (use como referência de
   profundidade esperada; mostre à usuária se ela pedir "me dá um exemplo")

### Etapa 2 — Conduzir o passaporte, arquivo por arquivo

Para cada um dos 7 arquivos textuais (em ordem 01 → 07):

1. **Anuncie** qual arquivo está sendo construído. Tom curto, editorial:
   > "Arquivo 01 — A empresa. Quem você é no mercado."

2. **Faça as perguntas** do `perguntas.md`:
   - Modo express → só a pergunta-âncora (a primeira)
   - Modo completo → todas as perguntas + follow-ups conforme respostas

3. **Aprofunde respostas curtas**. Se a resposta tem menos de 30 palavras OU é genérica
   ("ajudo mulheres", "vendo curso de marketing"), faça follow-up. Não aceite vago.

4. **Cite material concreto**:
   - Se a usuária diz "tom direto", peça: "me dá uma frase que você escreveria nesse tom"
   - Se diz "cliente ideal é empreendedora", peça: "me conta de UMA cliente real"
   - Se diz "vendo mentoria", peça: "qual o nome, preço, transformação?"

5. **Quando tiver material rico**, escreva o arquivo seguindo `formato-arquivos.md`.

6. **Mostre o arquivo gerado**:
   > "Esse é o arquivo 01-empresa.md. Lê e me diz se ficou você. Algo pra ajustar antes de
   > eu salvar?"

7. **Aprovado**, salve em `contexto/[nome].md`. Use `Write` tool.

8. **Avance** pro próximo: "Próximo — Arquivo 02. Voz e tom."

### Etapa 3 — Identidade visual (último passo)

Depois dos 7 textuais, capture identidade visual em `contexto/05-identidade-visual.md`.

Pergunte:

1. **Paleta principal** — HEX exatos OU descrição ("dois roxos profundos + dourado terroso").
   Se vaga, peça referência: "tem alguma marca que tem o look que você quer?"

2. **Fontes** — Se ela tem brand guide, perfeito. Senão, pergunte tom desejado e sugira do
   Google Fonts (use a tabela de `references/formato-arquivos.md`).

3. **Logo** — Caminho do arquivo (ex: `contexto/fotos/logo.png`) OU usar inicial estilizada
   da marca.

4. **Estilo visual em uma palavra** — editorial, tech, caloroso, brutalista, minimalista,
   premium-quiet, pop-bold, etc.

Gere o arquivo seguindo o template de identidade.

### Etapa 4 — Fechamento

Mensagem final:

> Passaporte preenchido. Os 8 arquivos estão em `contexto/`.
>
> A partir de agora, qualquer skill lê tudo isso antes de escrever uma linha. Você não vai
> mais ouvir "me conta sobre seu cliente" — porque o sistema já sabe.
>
> Próximos comandos pra testar:
>
> — `/imperial-carousel Tema:[tema] Função:posicionar` — primeiro carrossel na sua voz
> — `/imperial-week Tema:[guarda-chuva]` — sete dias coordenados de uma vez
> — `/imperial-intelligence` — varrer o que está em alta no nicho
>
> Qual quer rodar agora?

---

## REGRAS DE CONDUÇÃO

1. **Nunca chute respostas.** Se a usuária der info vaga, faça follow-up até ter material
   concreto. "Resolvo dor X com método Y" não é resposta — é etiqueta de marketing.

2. **Use as palavras DELA.** Cole frases textuais no arquivo. Não traduza pra "linguagem
   profissional". A voz dela é o ativo.

3. **Sempre peça exemplos reais.** Frases reais, casos reais, clientes reais, mensagens
   reais de DM. Skills que leem o passaporte vão precisar disso.

4. **Tom de entrevista premium, não formulário.** É conversa de mentora-editora, não survey
   da SurveyMonkey. Comente as respostas brevemente antes de avançar.

5. **Atualização parcial é primeira-classe.** Se a usuária diz "atualizar só minha voz",
   leia o arquivo atual, identifique o que mudou, faça as perguntas relevantes e regrave
   apenas aquele arquivo. Não toque nos outros.

6. **Memória importada é matéria-prima, não resposta final.** Se houver
   `memoria-importada.md`, use ela pra acelerar — mas confira com a usuária ANTES de salvar
   um arquivo: "vi que você falou X no ChatGPT. Confirma que ainda é assim?"

7. **Seja exigente com diferenciais.** Em `04-diferenciais.md`, rejeite genericidades:
   "atendimento humanizado", "qualidade", "atenção aos detalhes". Pergunte: "o que VOCÊ
   entrega que dá pra provar? Tem cliente que disse isso textualmente?"

8. **Rejeição é tão importante quanto aceitação.** Em `05-rejeicao.md`, vá fundo: temas,
   palavras, formatos, gatilhos baratos, comparações. Filtro automático em todas as skills
   futuras.

---

## REGRA DE OURO

O Passaporte não é "questionário inicial". É a fundação.

Quanto mais rica a entrevista — quanto mais frases reais, mais exemplos concretos, mais
postura definida — mais rico fica TUDO que o sistema gera depois.

Não economize aqui. Vale gastar 45 minutos uma vez pra economizar 45 minutos por semana
nos próximos 5 anos.
