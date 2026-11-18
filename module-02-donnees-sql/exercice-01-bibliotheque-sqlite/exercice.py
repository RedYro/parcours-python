"""
Module 02 — Exercice 01 : Bibliothèque en SQLite
Semaine : S7 (4–10 janv.)

Consigne :
1. Reprends la bibliothèque du module 01 (copie les fichiers ici).
2. Remplace la sauvegarde JSON par une base bibliotheque.db avec deux tables :
   livres et emprunts.
3. Toutes les requêtes doivent être paramétrées avec ?.
4. Écris une requête avec JOIN : la liste des livres empruntés avec le nom
   de l'emprunteur.

Notions : sqlite3, connect, cursor, execute, commit, requêtes paramétrées, JOIN

Indice :
Jamais de f-string dans une requête SQL : c'est la porte ouverte aux injections.

Pour lancer (depuis ce dossier, venv activé) : python exercice.py
"""

# Ton code ici
