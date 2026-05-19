---
description: Lance une code review sur le fichier ou dossier spécifié
model: claude-sonnet-4-6
tools: Agent, Bash
---

Lance une code review approfondie sur : $ARGUMENTS

Si aucun argument n'est fourni, utilise `git diff --name-only HEAD` pour identifier les fichiers modifiés et les reviewer.

Utilise l'agent `code-reviewer` pour effectuer l'analyse. Transmets-lui le chemin exact et demande un rapport complet avec sévérité, problème et suggestion pour chaque finding.
