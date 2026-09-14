# Filtros automáticos — anti-IA, anti-clichê, validação

Toda copy gerada (frase + legenda + hashtags) passa por essa lista ANTES de mostrar.
Se viola, regenerar.

---

## FILTRO 1 — Palavras vetadas pela própria marca

**Fonte:** `contexto/05-rejeicao.md` da aluna específica.

Carregar lista. Busca case-insensitive em TODA a copy. Se aparece, regerar.

---

## FILTRO 2 — Anti-clichê em frase de post

Posts simples têm pouco texto. Cada palavra pesa muito. Bloquear:

### Construções genéricas a evitar
- "A verdade é que..."
- "No final do dia..."
- "Você precisa entender que..."
- "Vou te falar uma coisa que ninguém fala..."
- "O segredo é..."
- "A chave está em..."

### Adjetivos vazios
- "Incrível"
- "Transformador"
- "Revolucionário"
- "Surpreendente"

### Promessas vagas
- "Mude sua vida"
- "Alcance seus sonhos"
- "Torne-se a melhor versão"
- "Liberte seu potencial"

### Frases-AI típicas
- "Não é apenas X. É Y." (uso ok 1x na semana, mas vira fórmula se repete)
- "Mais que [X], é [Y]." (mesma fórmula)
- "Se você [X], então [Y]." (estrutura condicional óbvia)

---

## FILTRO 3 — Densidade da frase

Pra cada tipo de post, há limite de palavras na frase principal:

| Tipo | Máximo de palavras na frase principal |
|---|---|
| Tweet-post | 20 (média 12-15) |
| Frase-quote | 15 (média 8-12) |
| Frase-do-reel | 12 (frase curta = retenção) |
| Print-DM | 25 (texto da mensagem) |
| Post-âncora | 18 (média 10-14) |

Acima do limite: cortar OU dividir em frase principal + frase de apoio.

---

## FILTRO 4 — Coerência com voz

Lê 3 amostras reais em `02-voz-e-tom.md`. Compara:

- Contrações coerentes (pra/para)?
- Pronome certo (você/vocês)?
- Aspas tipográficas (" ") quando aplicável?
- Travessões em (—) quando aplicável?
- Pelo menos 1 palavra-marca presente?

Posts simples têm pouco texto, então 1 palavra-marca em 12-15 palavras totais é suficiente.

---

## FILTRO 5 — Coerência com posicionamento

A frase está dizendo algo CONSISTENTE com `01-empresa.md`?

- A tese da marca aparece (explícita ou implícita)?
- O nicho está representado?
- A frase poderia funcionar pra qualquer marca? (se sim → genérica demais, refazer)

---

## FILTRO 6 — CTA da legenda

CTA na legenda precisa:

1. ✅ Verbo claro (comenta, manda, agenda, pega, salva)
2. ✅ Palavra-código ou link específico (CCC, CADERNO, biancafreitas.com.br/30dias)
3. ✅ Compatibilidade com etapa de funil

CTAs banidos em posts simples também:
- "Comenta aí"
- "Marca alguém"
- "Salva pra ver depois" (sem especificidade)
- "Like se gostou"

---

## FILTRO 7 — Hashtags coerentes

8-12 hashtags, escolhidas conforme:

1. **Nicho** (em `01-empresa.md`) — hashtags do segmento
2. **Tema** (do post específico)
3. **Marca** (#imperiumtreinamentos, #mentoriacastle, etc.)
4. **Público** (#empreendedorismofeminino, etc.)

NÃO usar:
- Hashtags genéricas demais (#instagram, #marketing)
- Hashtags inflacionadas (#fy, #foryou — Instagram não usa)
- Hashtags não-relacionadas pra "alcance"
- Mais de 12 (saturação visual + Instagram pode penalizar)

---

## FILTRO 8 — Frase repetida

Verificar `conteudo/posts/` (histórico). Se a frase OU variação muito próxima já apareceu
nas últimas 4 semanas, alertar:

> "Essa frase ('[X]') é muito próxima da que você usou em [data]. Quer:
> - Reformular?
> - Manter mesmo (variação intencional)?"

---

## FILTRO 9 — Tipo certo pro contexto

Validar se o tipo escolhido FAZ SENTIDO pra contexto:

| Cenário | Tipo recomendado | Tipo a evitar |
|---|---|---|
| Frase de reel publicado | Frase-do-reel | Tweet-post (perde gancho) |
| Manifesto de marca | Post-âncora | Tweet-post (perde peso) |
| DM real autorizada | Print-DM | Frase-quote (perde autenticidade) |
| Quote de autora | Frase-quote | Print-DM (não faz sentido) |
| Frase autoral curta tipo tweet | Tweet-post | Post-âncora (peso demais) |

Se o tipo escolhido não bate com o contexto, sugerir alternativa:

> "A frase parece quote autoral pesado. Sugiro post-âncora ao invés de tweet-post.
> Manter tweet-post mesmo?"

---

## FILTRO 10 — Identidade visual

Pós-render, verificar:

- Acento champagne contrasta com fundo? (se champagne sobre cream = baixa legibilidade)
- Logo está visível e no lugar?
- Texto não está cortado?
- Paleta exata da marca?

Se algo falha, ajustar antes de exportar.

---

## ROTINA DE VALIDAÇÃO

```
1. Validar a frase:
     filtro 1 (palavras vetadas)
     filtro 2 (clichês)
     filtro 3 (densidade)
     filtro 4 (voz)
     filtro 5 (posicionamento)
     filtro 8 (frase repetida)

2. Validar tipo:
     filtro 9 (tipo certo)

3. Validar legenda:
     filtro 1 + 2 (mesmos)
     filtro 6 (CTA)
     filtro 7 (hashtags)

4. Pós-render:
     filtro 10 (identidade visual)

5. Se algum filtro falhou:
     regerar trecho
     revalidar

6. Se 2 ciclos não resolvem:
     mostrar à usuária com flag
```

---

## REGRA DE OURO

Posts simples são frequentes — 2-4 por semana. Qualquer slip de qualidade aparece muito.

A skill é mais rigorosa em posts simples que em outras peças porque:
- A frase é o herói
- Pouco texto = cada palavra pesa
- Frequência alta = consistência crítica

Quando em dúvida: rejeitar e refazer.
