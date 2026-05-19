---
description: Explique le code pointé en argument en français, avec contexte et logique
model: claude-sonnet-4-6
tools: Read, Grep, Glob
---

Explique clairement en français le code suivant : $ARGUMENTS

Couvre :
- Ce que ce code fait (résultat observable)
- Comment il fonctionne (mécanisme interne)
- Pourquoi ce design a été choisi (si déductible du contexte)
- Les points non-évidents ou surprenants
- Les dépendances importantes

Adapte le niveau de détail à la complexité. Si c'est un fichier entier, commence par une vue d'ensemble puis détaille les parties clés. Si c'est une fonction, explique ligne par ligne si nécessaire.
