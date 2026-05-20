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
| `developer` | Opus 4.7 | Implémente features et corrige bugs dans n'importe quel langage |
| `code-reviewer` | Opus 4.7 | Review qualité, sécurité et performance du code |
| `test-writer` | Sonnet 4.6 | Rédige tests unitaires et d'intégration |
| `debugger` | Sonnet 4.6 | Débogue méthodiquement (hypothèse → cause racine → fix) |
| `architect` | Opus 4.7 | Conception système, trade-offs, ADRs |
| `devops` | Sonnet 4.6 | CI/CD, Docker, GitHub Actions, infra |
| `doc-writer` | Sonnet 4.6 | README, docstrings, documentation API |
| `security-auditor` | Opus 4.7 | Audit OWASP, secrets exposés, vulnérabilités |
| `data-scientist` | Opus 4.7 | ML/IA, PyTorch, LLMs, pipelines de données |
| `git` | Sonnet 4.6 | Workflow git complet : commits, branches, rebases, conflits |

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
    ├── format.py
    ├── log-session.py
    └── notify.py
```
