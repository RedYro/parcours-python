"""
Module 01 — Exercice 01 : Convertisseur °C ↔ °F
Semaine : S1 (23–29 nov.)

Consigne :
1. Demande à l'utilisateur s'il veut convertir des °C en °F ou l'inverse.
2. Demande la température.
3. Affiche le résultat arrondi à 1 décimale.
4. Si la saisie n'est pas un nombre, redemande-la.

Notions : input(), float(), if/elif/else, f-string, round()

Indice :
La formule : °F = °C × 9/5 + 32. Pour « redemander », pense à une boucle
qui ne s'arrête que quand la saisie est valide.

Pour lancer (depuis ce dossier, venv activé) : python exercice.py
"""

# Ton code ici
while True:
    choix_temp = input("Tapez 1 pour convertir °C en °F, 2 pour convertir °F en °C : ")

    if choix_temp == "1":
        unite = "°F"
        print("Conversion °C en °F")
        break
    elif choix_temp == "2":
        unite = "°C"
        print("Conversion °F en °C")
        break
    else:
        print("Saisie inconnue, choisissez entre le chiffre 1 ou 2")

while True:
    try:
        choix_nombre_temp = float(input("Saisissez votre température : "))
        break
    except ValueError:
        print(
            "La saisie n'est pas valide, essayez avec un point à la place de la virgule"
        )

if choix_temp == "1":
    print(f"{round(choix_nombre_temp * 9 / 5 + 32, 1)} {unite}")
else:
    print(f"{round((choix_nombre_temp - 32) * 5 / 9, 1)} {unite}")
