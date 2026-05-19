---
description: Génère des tests unitaires et d'intégration pour le fichier spécifié
model: claude-sonnet-4-6
tools: Agent
---

Génère des tests complets pour : $ARGUMENTS

Utilise l'agent `test-writer` pour analyser le code et rédiger les tests. Demande-lui de :
1. Identifier le framework de test utilisé dans le projet
2. Couvrir happy path, edge cases et cas d'erreur
3. Créer le fichier de test dans le bon dossier selon les conventions du projet
4. Lancer les tests pour vérifier qu'ils passent

Si aucun argument n'est fourni, demande quel fichier ou module tester.
