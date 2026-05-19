---
description: Génère un message de commit au format Conventional Commits basé sur les changements actuels
model: claude-sonnet-4-6
tools: Bash
---

Génère un message de commit pour les changements actuels.

Étapes :
1. Lance `git diff --staged` pour voir ce qui est staged
2. Si rien n'est staged, lance `git diff HEAD` pour voir tous les changements
3. Analyse les changements et génère un message au format Conventional Commits :

```
type(scope): description courte en impératif

Corps optionnel si les changements sont complexes ou ont besoin d'explication.

BREAKING CHANGE: description si applicable
```

Types valides : `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`, `build`

Règles :
- Première ligne : 72 caractères max
- Description en minuscules, pas de point final
- Impératif ("add feature" pas "added feature")
- Scope optionnel : nom du module ou composant affecté

Contexte additionnel fourni : $ARGUMENTS

Propose le message sans l'appliquer. L'utilisateur validera avant de committer.
