# ===============================
# Calculateur Porsche 992 TechArt GTstreet R
# Consommation et coûts d'entretien
# ===============================

def calculer_consommation_essence(km_annuel, conso_moyenne=13.0, prix_carburant=1.8):
    """
    Calcule la consommation annuelle d'essence et son coût.
    """
    litres_consommes = (km_annuel / 100) * conso_moyenne
    cout_carburant = litres_consommes * prix_carburant
    return litres_consommes, cout_carburant


def calculer_cout_entretien(km_annuel, cout_revision=3000, cout_pneus=1500, km_pneus=15000):
    """
    Calcule le coût d'entretien annuel (révisions + pneus).
    """
    cout_entretien = cout_revision  # Une révision par an obligatoire
    # Ajout des pneus en fonction du kilométrage
    cout_entretien += cout_pneus * (km_annuel // km_pneus)
    return cout_entretien


def saisie_utilisateur(message, valeur_defaut, cast=float):
    """
    Demande une saisie utilisateur avec une valeur par défaut si rien n'est entré.
    """
    entree = input(f"{message} [{valeur_defaut}] : ")
    if entree.strip() == "":
        return valeur_defaut
    try:
        return cast(entree)
    except ValueError:
        print("⚠️ Entrée invalide, valeur par défaut utilisée.")
        return valeur_defaut


def main():
    print("\n===============================================")
    print("  Calculateur de coûts Porsche 992 TechArt GTstreet R")
    print("===============================================\n")

    while True:
        # Saisie des paramètres
        km_annuel = saisie_utilisateur("Kilométrage annuel (km)", 10000)
        prix_carburant = saisie_utilisateur("Prix du litre de SP98 (€)", 1.8)
        conso_moyenne = saisie_utilisateur("Consommation moyenne (L/100 km)", 13.0)
        cout_revision = saisie_utilisateur("Coût annuel d'une révision (€)", 3000)
        cout_pneus = saisie_utilisateur("Coût d'un jeu de pneus (€)", 1500)
        km_pneus = saisie_utilisateur("Durée de vie des pneus (km)", 15000)

        # Calculs
        litres, cout_carburant = calculer_consommation_essence(km_annuel, conso_moyenne, prix_carburant)
        cout_entretien = calculer_cout_entretien(km_annuel, cout_revision, cout_pneus, km_pneus)
        cout_total = cout_carburant + cout_entretien
        cout_km = cout_total / km_annuel if km_annuel > 0 else 0

        # Résultats formatés
        print("\n=== Résultats annuels ===")
        print(f"➡️  Consommation annuelle : {litres:,.2f} litres")
        print(f"➡️  Coût du carburant     : {cout_carburant:,.2f} €")
        print(f"➡️  Coût entretien        : {cout_entretien:,.2f} €")
        print("-------------------------------------------")
        print(f"💰 Coût total annuel      : {cout_total:,.2f} €")
        print(f"📊 Coût moyen par km      : {cout_km:.2f} €/km")

        # Relancer ?
        choix = input("\nVoulez-vous refaire un calcul ? (o/n) : ").lower()
        if choix != "o":
            print("\nMerci d'avoir utilisé le calculateur. 🚗💨")
            break


if __name__ == "__main__":
    main()
