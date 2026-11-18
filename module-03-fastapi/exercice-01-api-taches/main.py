"""
Module 03 — Exercice 01 : API de tâches
Semaine : S10 (25–31 janv.)

Consigne :
1. API CRUD de tâches : GET /taches, GET /taches/{id}, POST /taches,
   PUT /taches/{id}, DELETE /taches/{id}.
2. D'abord avec une liste en mémoire, puis avec SQLite.
3. Modèles Pydantic pour les données en entrée et en sortie.
4. 404 si la tâche n'existe pas.
5. Teste chaque route depuis http://127.0.0.1:8000/docs.
6. Dans index.html : affiche et ajoute des tâches avec fetch.
7. S11 : tests avec TestClient dans test_main.py.

Notions : FastAPI, @app.get/@app.post, Pydantic, HTTPException, CORSMiddleware, TestClient

Indice :
Si fetch est bloqué par le navigateur, c'est le CORS : regarde CORSMiddleware.

Pour lancer (depuis ce dossier, venv activé) : fastapi dev main.py
"""

# Ton code ici
