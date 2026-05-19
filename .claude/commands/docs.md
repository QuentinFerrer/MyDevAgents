---
description: Génère ou améliore la documentation du fichier, module ou projet spécifié
model: claude-sonnet-4-6
tools: Agent
---

Génère ou améliore la documentation de : $ARGUMENTS

Utilise l'agent `doc-writer` pour analyser le code et produire la documentation. Demande-lui de :
1. Lire le code existant et détecter les conventions de documentation du projet
2. Générer ce qui est pertinent : README, docstrings, ou documentation API selon le contexte
3. S'assurer que les exemples de code fonctionnent réellement

Si aucun argument n'est fourni, génère un README complet pour le projet courant.
