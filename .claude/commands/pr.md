---
description: Génère un titre et une description de Pull Request pour la branche courante
model: claude-sonnet-4-6
tools: Bash
---

Génère une description de Pull Request pour la branche courante.

Étapes :
1. Lance `git branch --show-current` pour identifier la branche
2. Lance `git log main..HEAD --oneline` (ou `master` si `main` n'existe pas) pour lister les commits
3. Lance `git diff main...HEAD --stat` pour voir les fichiers modifiés

Produis :

**Titre** : court et descriptif, < 70 caractères, format `type: description`

**Description Markdown** :
```markdown
## Résumé
- Bullet points des changements principaux

## Motivation
Pourquoi ces changements sont nécessaires.

## Comment tester
Étapes manuelles pour valider.

## Notes
Breaking changes, migrations, dépendances à mettre à jour (si applicable).
```

Contexte additionnel : $ARGUMENTS
