"""
Module 01 — Exercice 03 : Nombre mystère
Semaine : S2 (30 nov. – 6 déc.)

Consigne :
1. L'ordinateur choisit un nombre entre 1 et 100.
2. L'utilisateur propose des nombres ; le programme répond « plus grand » ou « plus petit ».
3. À la fin, affiche le nombre d'essais.
4. Propose de rejouer ou de quitter.

Notions : import random, while, break, compteur

Indice :
Regarde random.randint dans la documentation.

Pour lancer (depuis ce dossier, venv activé) : python exercice.py
"""

# Ton code ici
import random

while True:
    nombre_essai = 0
    nombre_aleatoire = random.randint(1, 100)

    while True:
        try:
            choix_nombre = int(input("Saisissez votre nombre : "))
        except ValueError:
            print("Saisissez un nombre entier !")
            continue

        nombre_essai += 1

        if choix_nombre < nombre_aleatoire:
            print(f"{choix_nombre} est plus petit que le nombre mystère")
        elif choix_nombre > nombre_aleatoire:
            print(f"{choix_nombre} est plus grand que le nombre mystère")
        else:
            print(f"Gagné ! le nombre mystère était bien : {nombre_aleatoire}")
            print(f"Tentative(s) : {nombre_essai}")
            break

    while True:
        relance_partie = input("Rejouez ? (oui/non) : ").strip().lower()
        if relance_partie == "oui" or relance_partie == "non":
            break
        print("Choisissez entre oui et non seulement")

    if relance_partie == "non":
        print("Merci d'avoir joué, au revoir !")
        break
