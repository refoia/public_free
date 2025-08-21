# Script Python pour calculer la consommation d'essence et le coût d'entretien
# Porsche 992 TechArt GTstreet R

def calculer_consommation_essence(km_annuel, conso_moyenne=13.0, prix_carburant=1.8):
    """
    Calcule la consommation annuelle d'essence et son coût.
    :param km_annuel: Kilométrage annuel (en km)
    :param conso_moyenne: Consommation moyenne en L/100 km (défaut: 13.0 L/100 km)
    :param prix_carburant: Prix du litre de SP98 (en €, défaut: 1.8 €/L)
    :return: Tuple (litres consommés, coût annuel en €)
    """
    litres_consommes = (km_annuel / 100) * conso_moyenne
    cout_carburant = litres_consommes * prix_carburant
    return litres_consommes, cout_carburant

def calculer_cout_entretien(km_annuel, cout_revision=3000, cout_pneus=1500, km_pneus=15000):
    """
    Calcule le coût d'entretien annuel (révisions + pneus).
    :param km_annuel: Kilométrage annuel (en km)
    :param cout_revision: Coût annuel moyen d'une révision (en €, défaut: 3000 €)
    :param cout_pneus: Coût d'un jeu de pneus (en €, défaut: 1500 €)
    :param km_pneus: Durée de vie moyenne des pneus (en km, défaut: 15000 km)
    :return: Coût total d'entretien annuel (en €)
    """
    # Une révision par an
    cout_entretien = cout_revision
    # Remplacement des pneus si nécessaire
    if km_annuel >= km_pneus:
        cout_entretien += cout_pneus * (km_annuel // km_pneus)
    return cout_entretien

def main():
    print("=== Calculateur de coûts pour Porsche 992 TechArt GTstreet R ===")
    
    # Saisie des paramètres par l'utilisateur
     
    try:
        km_annuel = float(input("Entrez le kilométrage annuel (en km) : "))
        prix_carburant = float(input("Entrez le prix du litre de SP98 (en €, ex. 1.8) : "))
        conso_moyenne = float(input("Entrez la consommation moyenne (en L/100 km, ex. 13.0) : "))
        cout_revision = float(input("Entrez le coût annuel moyen d'une révision (en €, ex. 3000) : "))
        cout_pneus = float(input("Entrez le coût d'un jeu de pneus (en €, ex. 1500) : "))
        km_pneus = float(input("Entrez la durée de vie des pneus (en km, ex. 15000) : "))
    except ValueError:
        print("Erreur : Veuillez entrer des valeurs numériques valides.")
        return

    # Calculs
    litres, cout_carburant = calculer_consommation_essence(km_annuel, conso_moyenne, prix_carburant)
    cout_entretien = calculer_cout_entretien(km_annuel, cout_revision, cout_pneus, km_pneus)
    
    # Affichage des résultats
    print("\n=== Résultats ===")
    print(f"Consommation annuelle : {litres:.2f} litres")
    print(f"Coût du carburant : {cout_carburant:.2f} €")
    print(f"Coût d'entretien (révisions + pneus) : {cout_entretien:.2f} €")
    print(f"Coût total annuel (carburant + entretien) : {cout_carburant + cout_entretien:.2f} €")

if __name__ == "__main__":
    main()