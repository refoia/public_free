import folium
from geopy.distance import geodesic
from typing import List, Tuple, Optional
from dataclasses import dataclass
import webbrowser
import os

@dataclass
class Location:
    """Représente un lieu géographique avec ses métadonnées."""
    name: str
    latitude: float
    longitude: float
    description: str = ""
    visited: bool = False
    color: str = 'blue'  # Couleur par défaut pour les lieux non visités

    def get_coordinates(self) -> Tuple[float, float]:
        return (self.latitude, self.longitude)

class TravelMap:
    """Gère la carte interactive et les marqueurs."""
    def __init__(self, center_location: Location, zoom_start: int = 13):
        self.map = folium.Map(
            location=center_location.get_coordinates(),
            zoom_start=zoom_start,
            tiles='OpenStreetMap'  # Plusieurs options disponibles
        )
        self.locations = []
        self.path = None
        
    def add_location(self, location: Location) -> None:
        """Ajoute un lieu à la carte avec un marqueur personnalisé."""
        color = 'green' if location.visited else location.color
        icon = 'check' if location.visited else 'info-sign'
        
        popup_content = f"<b>{location.name}</b>"
        if location.description:
            popup_content += f"<br>{location.description}"
            
        folium.Marker(
            location=location.get_coordinates(),
            popup=popup_content,
            tooltip=location.name,
            icon=folium.Icon(color=color, icon=icon, prefix='fa')
        ).add_to(self.map)
        
        self.locations.append(location)
    
    def add_path(self, locations: List[Location], color: str = 'red') -> None:
        """Ajoute une ligne reliant les lieux visités dans l'ordre."""
        if len(locations) < 2:
            return
            
        points = [loc.get_coordinates() for loc in locations if loc.visited]
        if len(points) < 2:
            return
            
        self.path = folium.PolyLine(
            points,
            color=color,
            weight=2.5,
            opacity=1,
            tooltip="Parcours effectué"
        ).add_to(self.map)
    
    def save_and_open(self, file_name: str = 'travel_map.html') -> None:
        """Sauvegarde la carte et l'ouvre dans le navigateur par défaut."""
        self.map.save(file_name)
        webbrowser.open(f'file://{os.path.abspath(file_name)}')

class TravelTracker:
    """Gère la logique des déplacements et statistiques."""
    def __init__(self):
        self.locations: List[Location] = []
        self.visited_locations: List[Location] = []
    
    def add_location(self, location: Location, visited: bool = False) -> None:
        """Ajoute un lieu avec option de marquage comme visité."""
        if visited:
            location.visited = True
            location.color = 'green'
            self.visited_locations.append(location)
        self.locations.append(location)
    
    def mark_visited(self, location_name: str) -> None:
        """Marque un lieu comme visité."""
        for loc in self.locations:
            if loc.name.lower() == location_name.lower():
                loc.visited = True
                loc.color = 'green'
                if loc not in self.visited_locations:
                    self.visited_locations.append(loc)
                break
    
    def calculate_total_distance(self) -> float:
        """Calcule la distance totale parcourue entre les lieux visités."""
        if len(self.visited_locations) < 2:
            return 0.0
            
        total = 0.0
        for i in range(len(self.visited_locations)-1):
            start = self.visited_locations[i].get_coordinates()
            end = self.visited_locations[i+1].get_coordinates()
            total += geodesic(start, end).kilometers
            
        return round(total, 2)
    
    def get_visited_locations(self) -> List[Location]:
        """Retourne la liste des lieux visités dans l'ordre."""
        return self.visited_locations.copy()

def main():
    # Initialisation avec des données plus complètes
    cities = [
        Location("Paris", 48.8566, 2.3522, 
                "Capitale de la France", True),
        Location("Lyon", 45.7640, 4.8357, 
                "Ville gastronomique", True),
        Location("Marseille", 43.2965, 5.3698, 
                "Port méditerranéen", True),
        Location("Bordeaux", 44.8378, -0.5792, 
                "Capitale du vin", False),
        Location("Nice", 43.7102, 7.2620, 
                "Station balnéaire", False)
    ]
    
    # Initialisation des composants
    tracker = TravelTracker()
    for city in cities:
        tracker.add_location(city, city.visited)
    
    # Création de la carte
    travel_map = TravelMap(cities[0])  # Centrée sur Paris
    
    # Ajout des lieux et marquage
    for city in cities:
        travel_map.add_location(city)
    
    # Ajout du parcours entre les lieux visités
    travel_map.add_path(tracker.get_visited_locations())
    
    # Calcul des statistiques
    distance = tracker.calculate_total_distance()
    print(f"Distance totale parcourue: {distance} km")
    print(f"Lieux visités: {len(tracker.visited_locations)}/{len(cities)}")
    
    # Sauvegarde et affichage
    travel_map.save_and_open("voyage_france.html")

if __name__ == "__main__":
    main()
    
     
### Licence MIT


### Licence MIT pour la vente de produits numériques

### Copyright (c) 2025 [REFOÏA JEREMY LOUIS]
### SIRET 95108513300019 


### Autorisation est par la présente accordée, sans frais,
###à toute personne obtenant une copie de ce produit numérique
###et des fichiers de documentation associés (le "Produit"), 
###de traiter le Produit sans restriction, y compris,
###mais sans s'y limiter, les droits d'utiliser, de copier, de modifier,
###de fusionner, de publier, de distribuer, de sous-licencier et/ou de vendre des copies
###du Produit, et de permettre aux personnes à qui le Produit 
###est fourni de le faire, sous réserve des conditions suivantes :

###L'avis de copyright ci-dessus et cet avis d'autorisation 
###doivent être inclus dans toutes les copies ou parties substantielles du Produit.

###LE PRODUIT EST FOURNI "EN L'ÉTAT", SANS GARANTIE 
###D'AUCUNE SORTE, EXPRESSE OU IMPLICITE, Y COMPRIS,
###MAIS SANS S'Y LIMITER, LES GARANTIES DE QUALITÉ MARCHANDE, D'ADÉQUATION
###À UN USAGE PARTICULIER ET DE NON-CONTREFAÇON. 
###EN AUCUN CAS LES AUTEURS OU LES DÉTENTEURS DE DROITS D'AUTEUR NE SERONT RESPONSABLES DE TOUTE RÉCLAMATION,
###DOMMAGE OU AUTRE RESPONSABILITÉ, QU'IL S'AGISSE 
###D'UNE ACTION CONTRACTUELLE, DÉLICTUELLE OU AUTRE, DÉCOULANT DE,
###OU EN RELATION AVEC LE PRODUIT OU SON UTILISATION OU D'AUTRES TRANSACTIONS AVEC LE PRODUIT.

### Améliorations apportées :

###1. **Typage et documentation** :
   ### Utilisation de type hints pour une meilleure maintenabilité
   ### Docstrings complètes pour toutes les méthodes
   ### Utilisation de dataclass pour la classe Location

###2. **Fonctionnalités enrichies** :
   ### Gestion des lieux visités/non visités avec couleurs différentes
   ### Ajout de descriptions pour chaque lieu
   ### Traçage du parcours entre les lieux visités
   ### Ouverture automatique dans le navigateur
   ### Statistiques supplémentaires (nombre de lieux visités)

###3. **Meilleure organisation** :
   ### Séparation claire entre la logique métier (TravelTracker) et l'affichage (TravelMap)
   ### Méthodes plus spécialisées et atomiques
   ### Gestion des états plus robuste

###4. **Expérience utilisateur améliorée** :
   ### Popups plus informatifs avec HTML
   ### Tooltips pour les marqueurs
   ### Icônes Font Awesome
   ### Choix des fonds de carte

###5. **Robustesse accrue** :
   ### Vérification des préconditions
   ### Gestion des cas limites
   ### Copie des listes pour éviter les effets de bord

###Ce code offre maintenant une solution plus complète et professionnelle pour suivre et visualiser des déplacements géographiques.