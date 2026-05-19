---
description: Propose et applique un refactoring du code spécifié en préservant le comportement
model: claude-sonnet-4-6
tools: Read, Grep, Glob, Write, Edit, Bash
---

Refactorise le code suivant : $ARGUMENTS

Processus obligatoire :
1. Lis le code cible et comprends-le complètement
2. Trouve les tests existants pour ce code
3. Identifie les améliorations possibles :
   - Nommage peu clair
   - Fonctions trop longues ou qui font trop de choses
   - Duplication évitable
   - Complexité accidentelle
4. **Propose les changements et attends une confirmation avant d'appliquer**
5. Après confirmation, applique et relance les tests pour vérifier que rien n'est cassé

Règles absolues :
- Préserver exactement le comportement observable — les tests doivent tous passer
- Ne pas ajouter de fonctionnalités pendant un refactoring
- Ne pas sur-abstraire — trois lignes similaires valent mieux qu'une abstraction prématurée
- Un refactoring à la fois, pas tout en même temps
