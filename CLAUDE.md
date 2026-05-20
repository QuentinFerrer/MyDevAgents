# MyDevAgents

Boîte à outils Claude Code réutilisable : agents spécialisés, slash commands et hooks prêts à l'emploi.

## Utilisation

Copie le dossier `.claude/` à la racine de n'importe quel projet pour bénéficier immédiatement de tous les agents, commands et hooks.

```bash
cp -r .claude/ /ton/projet/
```

## Agents disponibles (`/agents`)

| Agent | Modèle | Rôle |
|-------|--------|------|
| `developer` | Sonnet 4.6 | Implémente features et corrige bugs dans n'importe quel langage |
| `code-reviewer` | Sonnet 4.6 | Review qualité, sécurité et performance du code |
| `test-writer` | Sonnet 4.6 | Rédige tests unitaires et d'intégration |
| `debugger` | Sonnet 4.6 | Débogue méthodiquement (hypothèse → cause racine → fix) |
| `architect` | Sonnet 4.6 | Conception système, trade-offs, ADRs |
| `devops` | Sonnet 4.6 | CI/CD, Docker, GitHub Actions, infra |
| `doc-writer` | Haiku 4.5 | README, docstrings, documentation API |
| `security-auditor` | Sonnet 4.6 | Audit OWASP, secrets exposés, vulnérabilités |
| `data-scientist` | Sonnet 4.6 | ML/IA, PyTorch, LLMs, pipelines de données |
| `git` | Haiku 4.5 | Workflow git complet : commits, branches, rebases, conflits |

> Pour les tâches complexes (audit critique, architecture distribuée, ML avancé), les agents concernés suggèrent de passer sur Opus via `/model claude-opus-4-7`.

## Slash commands disponibles (`/`)

| Commande | Description |
|----------|-------------|
| `/review [fichier]` | Lance une code review |
| `/test [fichier]` | Génère des tests |
| `/explain [fichier]` | Explique le code en français |
| `/commit` | Message de commit Conventional Commits |
| `/pr` | Description de Pull Request |
| `/security [fichier]` | Audit de sécurité |
| `/docs [fichier]` | Génère ou améliore la documentation |
| `/refactor [fichier]` | Propose un refactoring |

## Hooks automatiques

- **Auto-format** : après chaque `Write`/`Edit`, formate le fichier (`black`, `prettier`, `gofmt`, `rustfmt`)
- **README auto-update** : quand un fichier sensible est modifié (`requirements.txt`, `package.json`, `Dockerfile`, `.gitignore`, etc.), Claude reçoit un rappel automatique et met le README à jour si nécessaire
- **Log sessions** : chaque fin de session est loggée dans `.claude/logs/sessions.log`
- **Notification desktop** : alerte quand Claude termine (Windows/macOS/Linux)

### Prérequis pour le format automatique

Installe les formatteurs pour les langages que tu utilises :

```bash
pip install black          # Python
npm install -g prettier    # JS/TS/JSON/CSS/HTML
```

Go et Rust incluent `gofmt` et `rustfmt` nativement.

## Structure

```
.claude/
├── settings.json          # Configuration des hooks
├── agents/                # Agents spécialisés (10)
├── commands/              # Slash commands (8)
└── hooks/                 # Scripts Python cross-platform
    ├── format.py          # Auto-format après Write/Edit
    ├── readme-check.py    # Rappel README quand fichier sensible modifié
    ├── log-session.py     # Log des sessions
    └── notify.py          # Notification desktop
```
