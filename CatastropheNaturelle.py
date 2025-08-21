import random

class CatastropheNaturelle:
    def __init__(self, nom, impact_environnemental, frequence, duree_recuperation=None):
        """
        - nom : Nom de la catastrophe.
        - impact_environnemental : Dictionnaire {élément : impact (coefficient de réduction)}.
        - frequence : Probabilité d'occurrence.
        - duree_recuperation : Temps en cycles avant que certains éléments se rétablissent.
        """
        self.nom = nom
        self.impact_environnemental = impact_environnemental
        self.frequence = frequence
        self.duree_recuperation = duree_recuperation if duree_recuperation else {}

    def declencher(self, ecosysteme):
        print(f"\n⚠️ Catastrophe en cours : {self.nom} ⚠️")
        for element, impact in self.impact_environnemental.items():
            if element in ecosysteme:
                ecosysteme[element] *= impact  # Applique un coefficient de réduction
                ecosysteme[element] = max(0, round(ecosysteme[element], 2))  # Évite les valeurs négatives
                print(f"🔻 {element.capitalize()} réduit à {ecosysteme[element]}")

        # Planifier la récupération si applicable
        for element, cycles in self.duree_recuperation.items():
            if element in ecosysteme:
                print(f"🔄 {element.capitalize()} commencera à se rétablir dans {cycles} cycles.")
                ecosysteme[f"recup_{element}"] = cycles  # Ajoute un compteur de récupération

class EruptionVolcanique(CatastropheNaturelle):
    def __init__(self):
        super().__init__(
            nom="Éruption Volcanique",
            impact_environnemental={"végétation": 0.2, "faune": 0.5, "population": 0.7, "température": 0.9},
            frequence=0.01,
            duree_recuperation={"température": 5, "végétation": 10}  # La température et la végétation récupèrent avec le temps
        )

class Seisme(CatastropheNaturelle):
    def __init__(self):
        super().__init__(
            nom="Séisme",
            impact_environnemental={"population": 0.8, "faune": 0.9, "infrastructures": 0.5},
            frequence=0.02,
            duree_recuperation={"infrastructures": 15}  # Les infrastructures mettent du temps à être reconstruites
        )

class Tempete(CatastropheNaturelle):
    def __init__(self):
        super().__init__(
            nom="Tempête",
            impact_environnemental={"végétation": 0.7, "faune": 0.85, "population": 0.95},
            frequence=0.05,
            duree_recuperation={"végétation": 5}  # La végétation récupère rapidement
        )

class IncendieForet(CatastropheNaturelle):
    def __init__(self):
        super().__init__(
            nom="Incendie de Forêt",
            impact_environnemental={"végétation": 0.3, "faune": 0.6},
            frequence=0.03,
            duree_recuperation={"végétation": 8}  # La forêt repousse lentement
        )

def declencher_evenements_aleatoires(ecosysteme):
    """
    Vérifie si une catastrophe doit être déclenchée en fonction des probabilités.
    """
    catastrophes = [EruptionVolcanique(), Seisme(), Tempete(), IncendieForet()]
    
    for catastrophe in catastrophes:
        if random.random() < catastrophe.frequence:
            catastrophe.declencher(ecosysteme)

def recuperation_ecosysteme(ecosysteme):
    """
    Gère la récupération des éléments touchés après une catastrophe.
    """
    elements_a_recuperer = [key for key in ecosysteme if key.startswith("recup_")]
    
    for key in elements_a_recuperer:
        element = key.replace("recup_", "")
        if ecosysteme[key] > 0:
            ecosysteme[key] -= 1  # Diminue le temps de récupération
            if ecosysteme[key] == 0:
                print(f"✅ {element.capitalize()} a retrouvé son état normal !")
                ecosysteme[element] = min(ecosysteme[element] * 1.5, 100)  # Récupération progressive
                del ecosysteme[key]  # Supprime le compteur de récupération

def afficher_ecosysteme(ecosysteme):
    """
    Affiche l'état actuel de l'écosystème.
    """
    print("\n📊 État actuel de l'écosystème :")
    for key, value in ecosysteme.items():
        if not key.startswith("recup_"):  # Ne pas afficher les compteurs de récupération
            print(f"{key.capitalize()} : {value}")

# 🌍 Exemple de simulation
ecosysteme = {"végétation": 100, "faune": 100, "population": 100, "température": 20, "infrastructures": 100}

for cycle in range(1, 31):  # Simuler 30 jours
    print(f"\n🌿 Jour {cycle} 🌿")
    declencher_evenements_aleatoires(ecosysteme)
    recuperation_ecosysteme(ecosysteme)
    afficher_ecosysteme(ecosysteme)
    print("-" * 40)
