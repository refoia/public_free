#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Calculateur de consommation d'essence et de coût d'entretien
pour une Porsche 992 TechArt GTstreet R (ou tout autre véhicule).

Fonctionnalités :
- Demande à l'utilisateur les paramètres nécessaires.
- Calcule le carburant consommé et son prix.
- Calcule le coût d'entretien proportionnel aux kilomètres parcourus.
- Affiche les résultats avec deux décimales.
"""

def calculer_cout_essence(distance_km: float,
                          consommation_l_100km: float,
                          prix_litre_eur: float) -> float:
    """
    Retourne le coût total du carburant pour la distance indiquée.

    :param distance_km: distance parcourue en kilomètres.
    :param consommation_l_100km: consommation moyenne (L/100 ; ex. 12.5).
    :param prix_litre_eur: prix du litre d'essence en euros.
    :return: coût en euros.
    """
    # litres consommés = (distance / 100) × consommation
    litres = (distance_km / 100.0) * consommation_l_100km
    return litres * prix_litre_eur


def calculer_cout_entretien(kilometres_parcourus: float,
                            cout_annuel_eur: float,
                            km_par_an: float) -> float:
    """
    Retourne le coût d'entretien proportionnel aux kilomètres parcourus.

    :param kilometres_parcourus: total de kilomètres effectués.
    :param cout_annuel_eur: coût d'entretien estimé sur une année.
    :param km_par_an: nombre de kilomètres parcourus en moyenne chaque année.
    :return: coût d'entretien en euros.
    """
    if km_par_an <= 0:
        # Pas de kilométrage annuel renseigné → on renvoie 0 (ou on pourrait lever une exception)
        return 0.0
    proportion = kilometres_parcourus / km_par_an
    return proportion * cout_annuel_eur


def demander_float(message: str) -> float:
    """
    Demande à l'utilisateur un nombre réel et répète tant que l'entrée n'est pas valide.
    """
    while True:
        try:
            valeur = float(input(message).replace(',', '.'))  # accepte la virgule française
            return valeur
        except ValueError:
            print("⚠️  Entrée invalide ; veuillez saisir un nombre.")


def main():
    print("\n=== Calculateur de consommation d'essence et d'entretien ===\n")

    # Entrées utilisateur
    distance = demander_float("Distance parcourue (km) : ")
    consommation = demander_float("Consommation moyenne (L/100 km) : ")
    prix_essence = demander_float("Prix du litre d'essence (€/L) : ")
    km_totaux = demander_float("Kilomètres totaux parcourus sur le véhicule : ")
    cout_entretien_annuel = demander_float("Coût d'entretien annuel estimé (€/an) : ")
    km_par_an = demander_float("Kilométrage moyen annuel (km/an) : ")

    # Calculs
    cout_essence = calculer_cout = calculer_cout_essence(distance, consommation, prix_essence)
    cout_entretien = calculer_cout_entretien(km_totaux, cout_entretien_annuel, km_par_an)

    # Résultats
    print("\n--- Résultats ---")
    print(f"Coût total d'essence : {cout_essence:.2f} €")
    print(f"Coût d'entretien estimé : {cout_entretien:.2f} €")
    print("\nMerci d'avoir utilisé le calculateur !")


if __name__ == "__main__":
    main()