"""
Module 01 — Exercice 02 : Prix TTC avec remise
Semaine : S1 (23–29 nov.)

Consigne :
1. Demande un prix hors taxes.
2. Applique une remise selon le montant :
   - moins de 100 € : pas de remise
   - de 100 à 500 € : 5 %
   - plus de 500 € : 10 %
3. Ajoute la TVA à 20 % et affiche le détail (HT, remise, TTC) avec 2 décimales.

Notions : if/elif/else, opérateurs, f-string avec :.2f

Pour lancer (depuis ce dossier, venv activé) : python exercice.py
"""

# Ton code ici
while True:
    try:
        choix_prix = float(input("Saisissez votre prix : "))
        break
    except ValueError:
        print("Saisissez un chiffre !")

if 100 <= choix_prix <= 500:
    montant_remise = choix_prix * 5 / 100
    prix_remise = choix_prix - montant_remise
    prix_ttc = prix_remise * 1.2
    print(
        f"Prix de base {choix_prix:.2f}, {prix_ttc:.2f} avec 5% {montant_remise:.2f} de remise et TVA incluse"
    )
elif choix_prix > 500:
    montant_remise = choix_prix * 10 / 100
    prix_remise = choix_prix - montant_remise
    prix_ttc = prix_remise * 1.2
    print(
        f"Prix de base {choix_prix:.2f}, {prix_ttc:.2f} avec 10% {montant_remise:.2f} de remise et TVA incluse"
    )
else:
    prix_ttc = choix_prix * 1.2
    print(f"Prix de base {choix_prix:.2f}, {prix_ttc:.2f} sans remise et TVA incluse")
