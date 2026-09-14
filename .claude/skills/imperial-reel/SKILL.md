---
name: imperial-reel
description: |
  Skill canônica de roteiro de reel do sistema Imperium. Skill de COPY pura — gera
  roteiro completo (hook nos 2 primeiros segundos + 3 atos com timestamps + B-roll
  + texto na tela + CTA) + legenda + hashtags + stories de apoio + teleprompter
  texto. Entrevista única no início, 2 checkpoints (hook + roteiro completo) antes
  de finalizar. Formatos: talking-head, B-roll narrado, POV, trio, narração+texto.
  Durações: 15s, 30s, 45s, 60s, 90s. Triggers: "/imperial-reel", "roteiro de reel",
  "reel sobre [tema]", "preciso de reel", "reel de venda", "reel pra atrair".
allowed-tools: Read, Write, Glob, Grep, WebSearch, WebFetch, Bash
---

# Imperial Reel

Roteiro de reel autoral, na voz da marca. Skill de copy pura (não gera PNG).

> Os primeiros 2 segundos definem se o algoritmo entrega — e se a pessoa fica.

---

## QUANDO USAR

Use proativamente quando:
- Usuária pede `/imperial-reel`, "roteiro de reel", "reel sobre [X]"
- Quer transformar uma frase ou ideia em peça audiovisual

NÃO use quando:
- Pede só uma frase (use `/imperial-post`)
- Pede carrossel (use `/imperial-carousel`)

---

## FLUXO DE EXECUÇÃO

### Etapa 1 — Entrevista única (6 perguntas em uma mensagem)

Use o que a usuária já mencionou. Pergunte só o que falta:

> "Pra esse reel, preciso de 6 coisas (responde numa mensagem só):
>
> 1. **Tema** — sobre o que é?
> 2. **Função** — Posicionar (postura) / Atrair (alcance) / Conversão (vender) /
>    Reconectar (intimidade)?
> 3. **Formato** — talking-head (você fala direto) / b-roll (voz off + cortes) /
>    POV (primeira pessoa) / trio (3 cenas curtas) / narração+texto (voz baixa +
>    tipografia grande)?
> 4. **Duração-alvo** — 15s / 30s / 45s / 60s / 90s?
> 5. **Sobre você** — 2 frases (negócio + voz/palavras-marca/vetadas)
> 6. **CTA preferido** — opcional. Se não souber, sugiro 2-3 baseados na função."

**Se a usuária deu tema mas não definiu duração**, sugira baseado na função:
- Atrair: 15-30s
- Posicionar: 30-45s
- Conversão: 30-60s
- Reconectar: 45-90s

### Etapa 2 — Gerar 3 hooks alternativos

**Sempre ofereça 3 opções de hook antes do roteiro completo.** Reel é audiovisual —
quem grava precisa escolher o que sai melhor na boca dela.

```markdown
## 3 hooks sugeridos pro reel:

### Hook A — [Padrão A — tese-absoluta / pattern interrupt / dor reconhecida / etc]
"[hook A]"

### Hook B — [Padrão B]
"[hook B]"

### Hook C — [Padrão C]
"[hook C]"

Qual usar? (ou peço outras 3)
```

#### Padrões de hook por função (ver `references/hooks.md` completo)

**POSICIONAR:**
- Tese-absoluta: "[X] não é [comum]. É [refinado]."
- Negativa de identidade: "[Profissional] não [verbo comum]. [Profissional] [verbo refinado]."
- Anti-conselho: "O conselho que mais te dão é o que mais [verbo negativo]."
- Diferença qualitativa: "Existe uma diferença enorme entre [A] e [B]."

**ATRAIR:**
- Listicle teaser: "[N] [coisas] que toda [perfil] [verbo] — eu já [verbo + 1]."
- Mito vs verdade: "Você foi ensinada a [X]. Mas [verdade nova]."
- Pergunta hook: "Por que você ainda não [resultado] mesmo [fazendo coisa certa]?"

**CONVERSÃO:**
- Promessa específica: "Em [tempo], [resultado] — sem [dor comum]."
- Última chamada factual: "[Oferta] fecha [data]. [Vagas restantes]."
- Dor reconhecida: "[Frase exata que cliente diz no DM]."

**RECONECTAR:**
- Tempo + virada: "Demorei [N anos] pra entender que [verdade]."
- Confissão admitida: "Eu também já [ação vergonhosa]."
- Cena específica: "Foi [evento concreto] que mudou [coisa]."

#### Critérios do hook (4 testes obrigatórios)

Todo hook precisa passar em:
1. ✅ Cabe em 2.5-3s falados (8-12 palavras)
2. ✅ Cria gap (informação, curiosidade, identificação ou tensão)
3. ✅ Promete algo
4. ✅ Não funciona pra qualquer marca (precisa do nicho/voz da usuária)

Se algum dos 3 hooks falha em 1+ testes, regenerar ANTES de mostrar à aluna.

### Etapa 3 — CHECKPOINT A: aluna escolhe o hook

Aguarde a aluna escolher (ou pedir outras 3, ou pedir pra você escolher). Só avance
pra Etapa 4 depois da escolha.

### Etapa 4 — Gerar roteiro completo + legenda + stories + teleprompter

Gere TUDO de uma vez antes do checkpoint B:

```markdown
# REEL: [Tema]

**Função:** [Posicionar/Atrair/Conversão/Reconectar]
**Formato:** [...]
**Duração-alvo:** [Xs]

---

## ATO 1 — HOOK (0-3s)

**FALA:** "[hook escolhido]"
**VISUAL:** [descrição da imagem nos primeiros 3s]
**TEXTO NA TELA:** "[overlay opcional — complementa, não duplica a fala]"
**NOTA:** [corte rápido, ângulo fechado, expressão, etc]

---

## ATO 2 — DESENVOLVIMENTO (3-Xs)

| Tempo | Fala | Visual / B-roll | Texto na tela |
|---|---|---|---|
| 3-7s | "[fala]" | [visual] | [overlay] |
| 7-12s | "[fala]" | [visual] | [overlay] |
| ... | ... | ... | ... |

---

## ATO 3 — CTA (Xs-final)

**FALA:** "[CTA específico]"
**VISUAL:** [imagem que reforça o CTA]
**TEXTO NA TELA:** "[CTA visual — palavra-código, link, etc]"

---

## NOTAS TÉCNICAS

- **Ritmo:** rápido / médio / contemplativo
- **Iluminação:** editorial frontal / luz natural / chave + suave
- **Ângulo:** frontal / 3/4 / fechado / aberto
- **Áudio:** voz limpa / com música discreta / silêncio nas pausas

---

## LEGENDA DO POST

[Hook 1-2 linhas → arco 3-5 linhas → CTA 1-2 linhas]

## HASHTAGS

[8-12 em uma linha]

---

## STORIES DE APOIO (3-5)

1. Aquecimento (1 dia antes): [...]
2. Teaser: [...]
3. Reel publicado: [...]
4. Aprofundamento: [...]
5. CTA reforço: [...]

---

## TELEPROMPTER (pra colar no celular durante gravação)

[Falas isoladas em ordem, separadas por ///]

[FALA 1]
[texto curto]

///

[FALA 2]
[texto curto]

///

[...]
```

### Curva por função (timing)

Distribuição entre os 3 atos varia por função:

| Função | Hook | Desenvolvimento | CTA |
|---|---|---|---|
| Posicionar | 10% | 60% | 30% |
| Atrair | 15% | 70% | 15% |
| Conversão | 8% | 75% | 17% |
| Reconectar | 5% | 80% | 15% |

### Etapa 5 — Validação automática pelos 7 filtros

Ver `references/filtros.md`. Aplicar TODOS antes do checkpoint:

1. **Palavras vetadas** (universais + da marca específica)
2. **Clichês AI-flavored** ("Vamos lá!", "Espero que isso ajude!")
3. **CTAs proibidos** ("comenta aí", "marca alguém", "salva pra ver depois")
4. **Timing por cena** (~3 palavras/seg — cena 4s = max 12 palavras; cena 7s = max 21)
5. **B-roll factível** (só o que dá pra filmar com celular em casa/escritório)
6. **Filtro 10 — anti-frase-de-efeito vazia** (ver `filtros.md` — CRÍTICO)
7. **Teste de falabilidade** — cada fala em 1 respiração, sem palavras travadas em
   sequência ("multifacetada", "paradigma", duplas consonantes feias)

Se qualquer filtro falha, regenere o trecho ANTES de mostrar à aluna.

### Etapa 6 — CHECKPOINT B: aprovar roteiro completo

**Mostre TUDO em markdown legível e peça aprovação antes de finalizar.**

```markdown
## Reel pronto: [Tema]

**Função:** [...]  ·  **Formato:** [...]  ·  **Duração:** [Xs]  ·  **Hook escolhido:** [A/B/C]

---

[Roteiro completo dos 3 atos]
[Notas técnicas]
[Legenda + hashtags]
[Stories de apoio]
[Teleprompter]

---

**A copy passa? Algo pra ajustar?**

- **"aprova"** → fechado, salvo em `conteudo/reels/[YYYY-MM-DD]-[slug]/`
- **"troca o hook"** → pega outra opção das 3 (ou gero novas)
- **"regenera ato 2"** → refaz só o desenvolvimento, mantém hook+CTA
- **"mais punch"** / "mais reflexivo"** → recalibra tom
- **"corta pra 15s"** / "estende pra 45s"** → refaz duração
- **"B-roll mais simples"** → alternativas factíveis
- **"CTA mais direto"** / "mais suave"** → reformulo CTA
- **"troca formato pra [X]"** → reaplica em outro formato
```

**Só depois que a usuária aprovar, salve o pacote final.**

### Etapa 7 — Salvar pacote (opcional)

Se a usuária pediu pra salvar:

```bash
mkdir -p conteudo/reels/[YYYY-MM-DD]-[slug-tema]
```

Salvar 2 arquivos:
- `roteiro.md` — pacote completo (3 atos + notas + legenda + stories)
- `teleprompter.md` — só as falas em ordem com `///`, pra colar no celular

---

## REGRAS DE OURO

1. **Não dependa de arquivos externos.** Use a conversa atual.

2. **Hook é não-negociável.** Sempre 3 alternativas. Sempre passa nos 4 testes.

3. **Texto na tela complementa, não duplica.** Não transcreva a fala — adiciona
   camada extra (palavra-chave em destaque, número, frase-resumo).

4. **B-roll realista.** Só o que dá pra filmar com celular. Sem drones, sem
   time-lapses complexos, sem locações inviáveis.

5. **CTA dito E mostrado.** Reforço duplo (fala + texto na tela).

6. **Voz preservada.** Palavra-marca aparece ao menos 1x no roteiro.

7. **Tempos viáveis.** Não cabe 200 palavras em 30s. Limite ~3 palavras/segundo.

8. **Filtro 10 (anti-frase-de-efeito) é CRÍTICO.** Reels são percebidos PELA fala —
   frase vazia se ouvida ainda mais.

9. **Teste de falabilidade.** Cada fala lida mentalmente em voz alta antes de
   aprovar. Se trava na boca, refaz.

10. **2 checkpoints obrigatórios:**
    - **Checkpoint A** após gerar 3 hooks → aluna escolhe
    - **Checkpoint B** após gerar roteiro completo → aluna aprova

11. **Iteração granular.** "Regenera ato 2" sem refazer hook nem CTA. "Troca hook"
    sem refazer roteiro inteiro.

12. **Teleprompter sempre incluso.** Falas isoladas, marcação `///`, fonte simples
    pra leitura no celular durante gravação.

13. **Entrevista é única.** Pergunte os 6 itens numa mensagem só no início. Não
    pergunte de novo nos checkpoints.

---

## REGRA DE OURO META

Reel é **fala calibrada**, não texto adaptado. Toda copy gerada passa pelo teste:
**"isso é falável em 1 respiração?"**. Se não, refaz.

Lê em voz alta mentalmente cada fala antes de aprovar.

Diferente das outras skills, esta NÃO gera PNG. O entregável é texto puro —
roteiro estruturado + teleprompter pra usar na gravação real.
