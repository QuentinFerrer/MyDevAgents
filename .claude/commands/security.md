---
description: Lance un audit de sécurité sur le fichier, dossier ou projet spécifié
model: claude-sonnet-4-6
tools: Agent
---

Lance un audit de sécurité complet sur : $ARGUMENTS

Utilise l'agent `security-auditor` pour analyser le code. Demande-lui de :
1. Scanner tous les fichiers du périmètre spécifié
2. Chercher les vulnérabilités OWASP Top 10, secrets exposés et dépendances vulnérables
3. Produire un rapport structuré par sévérité (Critique → Basse)

Si aucun argument n'est fourni, audite l'ensemble du projet courant.
