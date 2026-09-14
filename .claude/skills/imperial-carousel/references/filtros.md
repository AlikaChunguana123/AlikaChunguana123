# Filtros automáticos — anti-IA, anti-clichê, validação de output

Toda copy gerada passa por essa lista ANTES de mostrar à usuária. Se viola, regenerar.

---

## FILTRO 1 — Palavras vetadas pela própria marca

**Fonte:** `contexto/05-rejeicao.md` da aluna específica.

Carregar a lista de palavras vetadas e fazer **busca case-insensitive em TODA a copy**
(slides + legenda + stories). Se uma única palavra vetada aparece, regenerar o trecho.

Lista padrão da Bianca/Castle (referência):
- "potencializar"
- "alavancar"
- "decola"
- "destrava" / "destravar"
- "MARCA 3 AMIGAS"
- "faturamento de 7 dígitos"
- "mindset milionário"
- "linda" / "amiga" / "querida" (infantilização)
- "potencial" (vago)

---

## FILTRO 2 — Clichês AI-flavored (universal, vale pra todas)

Frases tipicamente geradas por IA que sinalizam falta de personalização. Bloquear:

### Construções genéricas
- "Em um mundo onde..."
- "Você já parou pra pensar..."
- "A verdade é que..."
- "Se você é como a maioria..."
- "No final das contas..."

### Verbos esvaziados
- "potencializar"
- "alavancar"
- "transformar" (em sentido vago — usar só se o contexto traz transformação concreta)
- "evoluir" (em sentido vago)
- "desbloquear"
- "destravar"

### Adjetivos vazios
- "incrível"
- "impressionante"
- "transformador"
- "revolucionário"
- "ultrarrápido"
- "exclusivo" (a menos que prove)

### Promessas vagas
- "transforme sua vida"
- "mude para sempre"
- "alcance seus sonhos"
- "viva o seu propósito"
- "torne-se a melhor versão de você"

### Calls genéricos
- "comenta aí"
- "marca alguém que precisa ver"
- "deixa o like"
- "salva pra ver depois"
- "compartilha com aquela amiga"

**Substituições aceitáveis:**

| Genérico | Específico |
|---|---|
| "comenta aí" | "comenta [palavra-código] que mando o link no DM" |
| "marca alguém" | (cortar — não pedir ação se não for específica) |
| "deixa o like" | (cortar — like é consequência, não pedido) |
| "salva pra ver depois" | "salva — aplica no [evento específico futuro]" |

---

## FILTRO 3 — Padrões anti-IA estruturais

### "Listas paralelas perfeitas"
IA tende a fazer 3 itens com EXATAMENTE a mesma estrutura sintática:
- "Aprender a [verbo]"
- "Aprender a [verbo]"
- "Aprender a [verbo]"

**Como detectar:** se 3+ itens consecutivos abrem com a MESMA palavra ou MESMO verbo,
quebrar a paralela. Variar estrutura.

### Travessões dentro de travessões
"X — que é Y — porque Z — então W". Editar pra frases mais limpas.

### Excesso de "não é apenas X. É Y."
Esse padrão (negação binária) é poderoso, mas IA usa demais. Limite: 1-2 vezes por
carrossel inteiro. Mais que isso, vira fórmula reconhecível.

### Frases-resposta-de-Claude que viraram clichê
- "Vamos lá!" (nunca usar — não é fala humana real)
- "Espero que isso ajude!" (nunca)
- "Em resumo,..." (cortar — não resumir, declarar)
- "Por fim,..." (cortar)
- "É importante notar que..." (cortar)
- "Ao mesmo tempo..." (cortar)
- "Por outro lado..." (cortar — usar contraste sem essa muleta)

---

## FILTRO 4 — Coerência com posicionamento

Cruzar copy gerada com `01-empresa.md`:

- A **tese de mercado** declarada no posicionamento aparece (explícita ou implícita) no
  carrossel?
- O **nicho específico** está representado? Não basta dizer "empreendedoras" — se a aluna
  é "advogada de família", aparecer "advogada", "família", "direito".
- O **tom de exigência** (se é parte do DNA) está preservado? Ou virou tom acessível
  demais?

---

## FILTRO 5 — Coerência com cliente ideal

Cruzar com `03-cliente-ideal.md`:

- A **dor principal** (frase real registrada) aparece em algum slide ou na legenda?
- A **linguagem dela** (DMs reais) foi usada em pelo menos um slide?
- As **objeções comuns** foram quebradas (se função = Conversão)?

---

## FILTRO 6 — Filtro de prova / autoridade

Em `04-diferenciais.md` há credenciais e depoimentos. Se o carrossel é de função Conversão:

- Pelo menos 1 número/credencial concreto aparece?
- Slide de prova social usa depoimento REAL com nome (não inventado)?
- O método/framework próprio é nomeado quando aplicável?

---

## FILTRO 7 — CTA específico

Cruzar com `06-ofertas.md` pela etapa de funil declarada nos inputs:

| Etapa | CTA esperado |
|---|---|
| Topo | Lead magnet — link específico |
| Meio | Workshop / mini-curso — comando específico ("comente CCC") |
| Fundo | Vagas / lote / urgência factual + ação clara |
| Pós-conversão | Aplicação / agendamento de mentoria |

Se o CTA gerado é genérico ("acesse o link na bio", "comenta aí"), regerar.

---

## FILTRO 8 — Densidade textual por slide

Cada slide tem limite de palavras (lê estética visual):

| Função do slide | Headline | Body | Total slide |
|---|---|---|---|
| Capa | 8-15 palavras | — | <30 palavras |
| Setup / Reframe | 8-12 | 30-50 | <70 palavras |
| Aplicação | 6-12 | 25-40 | <60 palavras |
| Tese-virada | 6-10 | 20-30 | <50 palavras |
| CTA | 5-10 | 15-25 | <40 palavras |

Se um slide passa o limite, cortar até caber. Texto apertado mata o ar editorial.

---

## FILTRO 10 — Anti-frase-de-efeito vazia (CRÍTICO)

Frases bonitas que **não dizem nada concreto** — soam como mentor de Instagram, não como
mentora real. Mais perigosas que clichês AI porque DISFARÇAM melhor.

### Padrões a detectar e regenerar

**Padrão A — "X é Y, não Z" abstrato:**
- ❌ "Premium não é preço alto. É tese."
- ❌ "Não é estratégia. É postura."
- ❌ "Não é gestão. É escolha."

Quando a oposição é entre ABSTRAÇÕES (tese vs preço, postura vs estratégia), o padrão fica
vazio. A leitora aprende NADA novo — só ouve uma "filosofia" sem aplicação.

**Substituir por cena concreta:**
- ✅ "Cliente premium chega decidida. Quem decidiu foi você."
- ✅ "Você cobra alto e ouve 'cabe parcelar?'"

**Padrão B — "Se prova pelas [coisas]" / "Se constrói pelo [conceito]":**
- ❌ "Premium se prova pelas ausências, não pelas presenças."
- ❌ "A autoridade se constrói pelo silêncio."
- ❌ "A marca se constrói pela coerência."

Soa bonito, mas é tautológico. Quem está lendo não consegue agir com isso.

**Substituir por ação concreta:**
- ✅ "A marca premium se constrói pelo que recusa."
- ✅ "Cliente que pede desconto não comprou a tese. Comprou o preço."

**Padrão C — Verbos abstratos:**
- ❌ "descalibra a leitura"
- ❌ "consequência da clareza"
- ❌ "categoria sem leilão"
- ❌ "destrava o posicionamento"
- ❌ "transforma o jogo"

Verbos que não têm ação verificável. Não é falável em uma conversa real.

**Substituir por verbos concretos:**
- ✅ "cobra antes de precisar" (verbo: cobrar; agente: você; tempo: antes)
- ✅ "para de pesquisar concorrente" (ação observável)

**Padrão D — "Toda [coisa] se [verbo abstrato]":**
- ❌ "Toda marca premium se reconhece pelo silêncio."
- ❌ "Toda autoridade se conquista pela paciência."

Generalização vazia + verbo intransitivo. Não dá pra usar.

### Teste de cena concreta

Aplique mentalmente a TODA frase de headline ou body antes de aprovar:

1. **Tem CENA?** (algo que dá pra filmar — cliente perguntando, você decidindo, fila se formando)
2. **Tem VERBO TRANSITIVO?** (decidir algo, recusar alguém, perguntar X)
3. **Tem PESSOA ou OBJETO ESPECÍFICO?** (cliente premium, "cabe parcelar?", Hermès, R$X)
4. **A frase funciona FORA do carrossel?** (alguém ouviria em uma conversa real)

Se 2+ respostas são NÃO, regenerar.

### Lista de frases-radar (alta probabilidade de serem vazias)

Detecte estes padrões e questione antes de aprovar:
- "se prova por"
- "se constrói por"
- "se reconhece por"
- "consequência de"
- "decisão de tese"
- "leitura adulta" (já é jargão)
- "filtra quem"
- "ressignifica"
- "ancora"
- "sustenta o número"
- "antes do número"
- "vira referência"
- "vira categoria"
- "ninguém disputa"
- "não tem leilão"

**Override manual:** se a usuária pediu EXPLICITAMENTE um desses (ex: "uso 'leitura adulta'
como minha frase-marca"), respeite. Mas no padrão, regenerar.

---

## FILTRO 9 — Consistência de voz entre slides

Lê 3 amostras reais em `02-voz-e-tom.md`. Compara com cada slide gerado:

- Está usando contrações dela? (pra/para, tá/está)
- Está usando pronome certo? (você/vocês)
- Está usando travessões/parênteses no padrão dela?
- Tem pelo menos 1 palavra-marca em algum slide?

Se inconsistente em 2+ slides, regenerar.

---

## ROTINA DE VALIDAÇÃO

Pseudo-código mental antes de mostrar:

```
1. Pra cada slide:
     verificar palavras vetadas (filtro 1, 2)
     verificar densidade (filtro 8)
     verificar coerência de voz (filtro 9)
2. No carrossel inteiro:
     verificar coerência posicionamento (filtro 4)
     verificar uso de cliente real (filtro 5)
     verificar prova/autoridade se Conversão (filtro 6)
     verificar CTA específico (filtro 7)
     verificar padrões anti-IA estruturais (filtro 3)
3. Se algum filtro falhou:
     regerar trecho ou slide
     revalidar
4. Se 2 ciclos de regeneração não resolvem:
     parar
     mostrar à usuária com flag: "esse trecho continua batendo no filtro X.
     Quer reescrever manualmente ou flexibilizar a regra?"
```

---

## REGRA DE OURO

O filtro existe pra **proteger a voz da aluna**, não pra ser ditatorial. Se a usuária
EXPLICITAMENTE quer usar uma palavra vetada (ex: "uso 'destrava' propositalmente como
ironia"), respeite. O filtro tem override manual.

Mas no padrão: aplicar com rigor. É a diferença entre "Claude operando minha marca" e
"Claude escrevendo genérico".
