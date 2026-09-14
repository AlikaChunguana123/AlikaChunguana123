# Varredura de tendências — protocolo operacional

Como executar varredura de mercado em 5-7 minutos sem se perder em volume.

---

## PROTOCOLO PADRÃO (5-7 min)

### Passo 1 — Carregar config (10s)
Ler `contexto/intelligence-config.md`:
- Lista de sites
- Lista de concorrentes Instagram
- Janela temporal
- Idioma de busca

### Passo 2 — Queries-base (60s pra montar 6 queries)

Pra um nicho de "marketing premium feminino", as queries seriam:

```
1. "marketing premium feminino" tendências [mês]
2. "empresária digital" "[ano]" novidade
3. site:[blog_referencia_1] OR site:[blog_referencia_2]
4. "Instagram empresária" 2026
5. "[oferta principal]" como fazer
6. "[problema central do cliente]" solução
```

Pra outros nichos (advogada de família, terapeuta, designer), substituir vocabulário-chave.

### Passo 3 — Executar 6 buscas em paralelo (~2 min)

Use `WebSearch` pra cada query. Recolher os 5 primeiros resultados de cada (não mais).

**Total esperado:** 30 resultados brutos.

### Passo 4 — Filtrar (1-2 min)

Aplicar filtros em ordem:

#### Filtro 1 — Data
Descartar tudo > 30 dias (a menos que análise de longo prazo seja explícita).

#### Filtro 2 — Fonte
Descartar:
- Sites sem credibilidade
- Sites com SEO inflado mas conteúdo raso
- Listicles Buzzfeed-style
- "Top 10 tendências que vão mudar tudo" (genéricos)

#### Filtro 3 — Relevância
Descartar resultados desconectados de:
- `01-empresa.md` (nicho)
- `03-cliente-ideal.md` (audiência)

#### Filtro 4 — Originalidade
Se 5+ fontes dizem a mesma coisa, agrupar como 1 tema.

**Saída esperada após filtros:** 8-15 resultados qualificados.

### Passo 5 — Sintetizar em 5 temas (2 min)

Agrupar os 8-15 qualificados em 5 temas. Cada tema responde:

1. O QUE é o tema?
2. POR QUE está em alta?
3. HÁ QUANTO TEMPO?
4. PARA QUEM IMPORTA?
5. QUE ÂNGULO É ÓBVIO? (pra evitar)
6. QUE ÂNGULO É AUTORAL? (pra explorar)

---

## QUERIES POR TIPO DE NICHO

Adaptar as queries-padrão ao nicho específico:

### Nicho — Marketing/Posicionamento Feminino
- "marketing premium feminino" tendências
- "empresária digital" 2026
- "posicionamento digital" novidade
- "criadora de conteúdo" método
- "Instagram empresária" novidade

### Nicho — Advocacia (especialização)
- "[especialização]" 2026 jurisprudência
- "novo CPC" [especialização]
- "advogada [especialização]" Instagram
- "honorários advocatícios" tendência
- "[temp_central_juridico]" decisão

### Nicho — Terapia/Psicologia
- "psicologia" tendência [ano]
- "terapia online" novidade
- "saúde mental" debate
- "ICP-11" mudança
- "psicoterapia [linha]" novo estudo

### Nicho — Design/Branding
- "design tendências" [ano]
- "branding premium" 2026
- "tipografia" lançamento
- "AI design" novidade
- "Adobe lança" 2026

### Nicho — Coaching/Mentoria
- "coaching" mudança regulamentação
- "mentoria executiva" tendência
- "ICF" novidade [ano]
- "negócios femininos" método

### Nicho — Beleza/Estética
- "estética avançada" tendência [ano]
- "Anvisa" liberação procedimento
- "skincare" lançamento
- "[procedimento_central]" novidade

### Nicho — Educação/Curso Online
- "infoproduto" tendência [ano]
- "curso online" formato emergente
- "EAD" novidade
- "Hotmart Kiwify" mudança 2026

### Nicho — Saúde Holística/Bem-estar
- "saúde feminina" estudo [ano]
- "wellness" tendência 2026
- "nutrição funcional" novidade
- "yoga" prática emergente

> Quando a usuária não tem nicho na lista acima, **derivar queries do `01-empresa.md`**:
> usar palavras-chave do posicionamento + tese central + nome do produto principal.

---

## FONTES POR CATEGORIA

### Tier 1 — Sempre buscar
- Blogs de referência do nicho (cadastrados em `intelligence-config.md`)
- Sites oficiais de eventos/regulamentação (OAB, CFM, ICF, etc.)
- Magazines do segmento (Forbes Brasil, Exame Diversidade, B9, etc.)

### Tier 2 — Buscar se Tier 1 escasso
- LinkedIn pulse (artigos longos com credibilidade)
- Substack/Newsletters de referência
- Medium curated

### Tier 3 — Buscar com cautela
- Twitter/X (saturado, mas pode ter sinais)
- Reddit (nichos específicos têm comunidades fortes)

### Não buscar
- Buzzfeed e similares
- Sites de SEO inflado ("17 dicas que vão mudar...")
- Sites com paywall sem amostra
- Conteúdo de marca disfarçado de imparcial

---

## QUANDO ENCONTRAR ALGO INESPERADO

Cenários comuns:

### Cenário A — Não há nada em alta
Algumas semanas o nicho é morno. Output:
> "Nicho está em pausa essa semana. Sem tendências claras. Tema sugerido: aprofundar
> evergreen [tema da `01-empresa.md`]."

### Cenário B — Tendência viral mas conflita com `05-rejeicao.md`
Filtrar e registrar:
> "Tendência X está em alta no nicho mas conflita com sua rejeição (motivo). Descartado.
> Outras 4 tendências válidas abaixo."

### Cenário C — Polêmica/crise no nicho
Atenção redobrada. Não usar como tendência genérica. Output:
> "Há polêmica/crise no nicho ([resumo]). Decida se quer abordar — depende da postura
> da marca. Não recomendo usar como tema sem decisão consciente."

### Cenário D — Tema repetido das últimas 4 semanas
Verificar `conteudo/intelligence/` (histórico). Se você já abordou o tema 2+ vezes nas
últimas 4 semanas:
> "Tema X já apareceu nas últimas semanas. Recomendo NÃO repetir — ou abordar pelo
> ângulo Y (alternativo)."

---

## REGRA DE OURO

**Curadoria > volume.** 5 temas bem identificados valem mais que 30 superficiais.

Tempo total da varredura: 5-7 min. Mais que isso, vira procrastinação disfarçada.
