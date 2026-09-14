# Imperium Skills

Sistema de 8 skills do Imperium Treinamentos pra Claude Code.

Operam o seu Instagram premium feminino: do passaporte de identidade até carrossel,
reel, post-frase, post-notícia verificada, intelligence de mercado e planejamento semanal.

---

## Pré-requisito

- Claude Code instalado em `claude.ai/download`
- macOS, Windows (com WSL ou Git Bash) ou Linux

## Instalação em 3 passos

### 1. Baixe o pacote

Você recebeu `imperium-skills.zip` no e-mail de pré-workshop (ou na área de membros).

### 2. Descompacte em `~/.claude/skills/`

**Mac / Linux:**
```bash
mkdir -p ~/.claude/skills && \
unzip -o ~/Downloads/imperium-skills.zip -d ~/.claude/skills/ && \
echo "✓ 8 Imperium Skills instaladas"
```

**Windows (Git Bash):**
```bash
mkdir -p ~/.claude/skills && \
unzip -o /c/Users/$USER/Downloads/imperium-skills.zip -d ~/.claude/skills/ && \
echo "✓ 8 Imperium Skills instaladas"
```

**Windows (PowerShell):**
```powershell
$skillsPath = "$env:USERPROFILE\.claude\skills"
New-Item -ItemType Directory -Force -Path $skillsPath
Expand-Archive -Force "$env:USERPROFILE\Downloads\imperium-skills.zip" -DestinationPath $skillsPath
Write-Host "✓ 8 Imperium Skills instaladas"
```

### 3. Reabra o Claude Code

Feche e abra novamente. As 8 skills aparecem prontas pra uso.

---

## Skills incluídas

| Comando | Skill | Função |
|---|---|---|
| `/passaporte-imperial` | Passaporte Imperial | Onboarding — preenche os 8 arquivos de contexto |
| `/imperial-carousel` | Imperial Carousel | Carrossel canônico — 4 funções, 3 estruturas |
| `/imperial-reel` | Imperial Reel | Roteiro audiovisual — 5 formatos, hooks calibrados |
| `/imperial-week` | Imperial Week | Orquestrador semanal — 6 templates de mix |
| `/imperial-intelligence` | Imperial Intelligence | Inteligência de mercado — varredura + concorrência |
| `/imperial-post` | Imperial Post | Post-frase única — 5 tipos visuais |
| `/youtube-transcricao-carrossel` | YouTube → Carrossel | Pipeline completo: vídeo do YouTube → transcrição → resumo + ideias no Notion → carrosséis prontos |
| `/imperial-news` | Imperial News | Notícia verificada do SEU nicho → card 3:4 ou reel de 7s com sua identidade — com filtro anti-notícia-reciclada |

---

## Primeira execução — sequência recomendada

Após instalar:

1. **`/passaporte-imperial`** — preenche seu contexto editorial (15-45 min). Sem isso,
   nenhuma outra skill funciona direito.

2. **`/imperial-intelligence`** — primeira varredura de mercado (5-15 min). Você só
   precisa configurar uma vez (sites, concorrentes).

3. **`/imperial-week`** — primeiro plano semanal (10-15 min).

4. **`/imperial-carousel`** ou **`/imperial-reel`** — primeiro conteúdo detalhado.

---

## Atualização

Quando uma versão nova das skills sair:

1. Baixe o novo `imperium-skills.zip`
2. Execute o comando de instalação novamente
3. As skills serão sobrescritas (seu `contexto/` no projeto NÃO é afetado — fica em
   pastas separadas)

---

## Suporte

- **Workshop CCC**: cria-com-claude.imperium.com.br
- **Área de membros**: imperium.com.br/membros
- **DM Bianca**: @biancafreitas

---

*Imperium Treinamentos · MMXXVI*
