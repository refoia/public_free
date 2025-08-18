"""
Générateur de Prompts Excel Modulaire avec Personnalités de Développeurs
Auteur: Assistant IA
Date: 2025
"""

import random
import datetime
import uuid
import os
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum

# Configuration
class DevPersonality(Enum):
    ARCHITECT = "architect"
    PRAGMATIC = "pragmatic"
    INNOVATOR = "innovator"

@dataclass
class PromptConfig:
    """Configuration pour la génération de prompts"""
    output_dir: str = "generated_prompts"
    model_name: str = "granite-3.2-8b-instruct"
    language: str = "utf-8"
    max_prompts_per_session: int = 5

@dataclass
class DevProfile:
    """Profil d'un développeur professionnel"""
    name: str
    personality: DevPersonality
    coding_style: str
    preferred_patterns: List[str]
    expertise_areas: List[str]
    prompt_modifier: str

class ExcelPromptGenerator:
    """Générateur de prompts pour création de fichiers Excel"""
    
    def __init__(self, config: PromptConfig = None):
        self.config = config or PromptConfig()
        self.base_prompts = self._initialize_base_prompts()
        self.dev_profiles = self._initialize_dev_profiles()
        self._ensure_output_directory()
    
    def _initialize_base_prompts(self) -> Dict[str, str]:
        """Initialise les prompts de base pour Excel"""
        return {
            "gestion_employes": """
            Créer un système de gestion des employés avec colonnes:
            Nom, Âge, Département, Poste, Salaire, Date d'embauche.
            Inclure des feuilles séparées par département.
            """,
            
            "suivi_stocks": """
            Développer un système de suivi des stocks avec:
            Nom produit, ID produit, Quantité, Prix unitaire, Fournisseur.
            Ajouter alertes pour stocks bas et analyse des ventes.
            """,
            
            "reporting_ventes": """
            Générer des rapports de ventes avec données par:
            région, produit, commercial, chiffre d'affaires.
            Inclure graphiques et analyses temporelles.
            """,
            
            "planification_projets": """
            Créer un planificateur de projets avec:
            Nom tâche, Responsable, Statut, Dates début/fin.
            Ajouter priorités et calculs automatiques d'échéances.
            """,
            
            "analyse_financiere": """
            Simuler états financiers avec colonnes:
            Mois, Revenus, Dépenses, Bénéfices nets.
            Inclure tableau de bord et visualisations de tendances.
            """,
            
            "crm_basique": """
            Construire un CRM avec champs:
            Nom, Email, Téléphone, Source, Date de suivi.
            Ajouter KPIs et statistiques de performance.
            """,
            
            "projets_immobiliers": """
            Gérer projets immobiliers avec:
            Nom projet, Localisation, Investissement, Responsable, Échéance.
            Séparer projets en cours et terminés.
            """,
            
            "horaires_employes": """
            Suivre horaires employés avec:
            Nom, ID, Heures début/fin, Total heures.
            Calculer automatiquement salaires et heures supplémentaires.
            """,
            
            "transport_logistique": """
            Tracker colis avec colonnes:
            ID Colis, Expéditeur, Destinataire, Adresse, Statut.
            Analyser performance livraisons et retards.
            """,
            
            "ecommerce_produits": """
            Base produits e-commerce avec:
            Nom, Catégorie, Stock, Prix, Évaluation client.
            Organiser par catégories avec analyses croisées.
            """
        }
    
    def _initialize_dev_profiles(self) -> Dict[DevPersonality, DevProfile]:
        """Initialise les profils de développeurs professionnels"""
        return {
            DevPersonality.ARCHITECT: DevProfile(
                name="Elena Struct",
                personality=DevPersonality.ARCHITECT,
                coding_style="Architecture-driven, SOLID principles",
                preferred_patterns=["Factory", "Strategy", "Observer", "Decorator"],
                expertise_areas=["System Design", "Scalability", "Clean Code", "Documentation"],
                prompt_modifier="""
                Approche cette tâche avec une mentalité d'architecte logiciel:
                - Structure le code avec des classes et interfaces bien définies
                - Applique les principes SOLID
                - Documente chaque composant
                - Pense scalabilité et maintenabilité
                - Utilise des design patterns appropriés
                """
            ),
            
            DevPersonality.PRAGMATIC: DevProfile(
                name="Marcus Pragma",
                personality=DevPersonality.PRAGMATIC,
                coding_style="Solution-oriented, efficient and practical",
                preferred_patterns=["KISS", "DRY", "YAGNI"],
                expertise_areas=["Problem Solving", "Performance", "Debugging", "Best Practices"],
                prompt_modifier="""
                Adopte une approche pragmatique de développeur senior:
                - Focus sur des solutions qui marchent vraiment
                - Optimise pour la performance et la simplicité
                - Inclus gestion d'erreurs robuste
                - Écris du code lisible et maintenable
                - Ajoute des tests unitaires essentiels
                """
            ),
            
            DevPersonality.INNOVATOR: DevProfile(
                name="Zara Innovation",
                personality=DevPersonality.INNOVATOR,
                coding_style="Creative, experimental, cutting-edge",
                preferred_patterns=["Functional Programming", "Async/Await", "Reactive"],
                expertise_areas=["Emerging Tech", "AI/ML Integration", "Modern Frameworks", "UX"],
                prompt_modifier="""
                Approche cette tâche avec l'esprit d'un innovateur tech:
                - Utilise les dernières fonctionnalités Python
                - Intègre des éléments d'IA/ML si pertinent
                - Pense expérience utilisateur moderne
                - Explore des approches créatives
                - Inclus des fonctionnalités interactives avancées
                """
            )
        }
    
    def _ensure_output_directory(self):
        """Crée le répertoire de sortie s'il n'existe pas"""
        Path(self.config.output_dir).mkdir(exist_ok=True)
    
    def generate_enhanced_prompt(self, 
                               base_prompt_key: str, 
                               dev_personality: DevPersonality,
                               custom_requirements: str = "") -> str:
        """Génère un prompt amélioré avec personnalité de dev"""
        
        if base_prompt_key not in self.base_prompts:
            raise ValueError(f"Prompt de base '{base_prompt_key}' introuvable")
        
        base_prompt = self.base_prompts[base_prompt_key]
        dev_profile = self.dev_profiles[dev_personality]
        
        enhanced_prompt = f"""
# Projet Excel - {base_prompt_key.replace('_', ' ').title()}
## Développeur assigné: {dev_profile.name} ({dev_profile.personality.value})

**Contexte du projet:**
{base_prompt.strip()}

**Personnalité du développeur:**
{dev_profile.prompt_modifier.strip()}

**Expertise technique:**
- Style: {dev_profile.coding_style}
- Patterns préférés: {', '.join(dev_profile.preferred_patterns)}
- Domaines d'expertise: {', '.join(dev_profile.expertise_areas)}

**Exigences techniques:**
- Code Python modulaire avec séparation claire des responsabilités
- Utilisation d'openpyxl, pandas ou xlsxwriter
- Documentation complète des fonctions
- Gestion d'erreurs appropriée
- Tests unitaires recommandés

**Exigences supplémentaires:**
{custom_requirements if custom_requirements else "Aucune exigence spécifique supplémentaire."}

**Livrable attendu:**
Un code Python complet, modulaire et professionnel générant un fichier Excel
selon les spécifications ci-dessus, reflétant le style et l'expertise de {dev_profile.name}.
"""
        return enhanced_prompt.strip()
    
    def save_prompt_to_file(self, prompt: str, filename: str = None) -> str:
        """Sauvegarde un prompt dans un fichier"""
        if not filename:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            unique_id = str(uuid.uuid4())[:8]
            filename = f"excel_prompt_{timestamp}_{unique_id}.txt"
        
        filepath = Path(self.config.output_dir) / filename
        
        try:
            with open(filepath, 'w', encoding=self.config.language) as f:
                f.write(f"# Généré le {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write(prompt)
            
            print(f"✅ Prompt sauvegardé: {filepath}")
            return str(filepath)
        
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde: {e}")
            return ""
    
    def generate_random_prompt_set(self, count: int = 3) -> List[str]:
        """Génère un ensemble aléatoire de prompts avec différentes personnalités"""
        generated_files = []
        
        for i in range(min(count, self.config.max_prompts_per_session)):
            # Sélection aléatoire
            prompt_key = random.choice(list(self.base_prompts.keys()))
            dev_personality = random.choice(list(DevPersonality))
            
            # Génération du prompt
            enhanced_prompt = self.generate_enhanced_prompt(
                prompt_key, 
                dev_personality
            )
            
            # Sauvegarde
            filename = self.save_prompt_to_file(enhanced_prompt)
            if filename:
                generated_files.append(filename)
                
            print(f"📋 Prompt {i+1}/{count} généré avec {dev_personality.value}")
        
        return generated_files
    
    def get_available_prompts(self) -> List[str]:
        """Retourne la liste des prompts disponibles"""
        return list(self.base_prompts.keys())
    
    def get_dev_profiles_info(self) -> Dict[str, str]:
        """Retourne les informations sur les profils de développeurs"""
        return {
            personality.value: f"{profile.name} - {profile.coding_style}"
            for personality, profile in self.dev_profiles.items()
        }

# Exemple d'utilisation et tests
def main():
    """Fonction principale de démonstration"""
    print("🚀 Générateur de Prompts Excel avec Personnalités Dev")
    print("=" * 60)
    
    # Initialisation
    generator = ExcelPromptGenerator()
    
    # Affichage des profils disponibles
    print("\n👥 Profils de développeurs disponibles:")
    for personality, info in generator.get_dev_profiles_info().items():
        print(f"  • {personality}: {info}")
    
    # Affichage des prompts disponibles
    print(f"\n📋 {len(generator.get_available_prompts())} types de projets disponibles:")
    for i, prompt in enumerate(generator.get_available_prompts(), 1):
        print(f"  {i}. {prompt.replace('_', ' ').title()}")
    
    # Génération d'exemples
    print(f"\n🔄 Génération de {3} prompts aléatoires...")
    generated_files = generator.generate_random_prompt_set(3)
    
    print(f"\n✅ {len(generated_files)} fichiers générés avec succès!")
    
    # Exemple de génération ciblée
    print("\n🎯 Exemple de génération ciblée:")
    custom_prompt = generator.generate_enhanced_prompt(
        "crm_basique", 
        DevPersonality.ARCHITECT,
        "Intégrer des fonctionnalités d'export PDF et de notifications email"
    )
    
    custom_file = generator.save_prompt_to_file(
        custom_prompt, 
        "crm_architect_example.txt"
    )
    
    if custom_file:
        print(f"📄 Exemple sauvegardé dans: {custom_file}")

if __name__ == "__main__":
    main()


 
## 🎯 **Points Forts de cette Fiche Produit :**

### **✅ Structure Marketing Optimale**
##- **Titre accrocheur** avec émojis pour attirer l'attention
##- **Description claire** qui explique immédiatement la valeur
##- **Fonctionnalités détaillées** sans être technique
##- **Bénéfices quantifiés** (80% de réduction de temps)

### **🎪 Présentation Visuelle**
##- **Émojis stratégiques** pour faciliter la lecture
##- **Sections bien délimitées** pour navigation rapide  
##- **Code blocks** pour les aspects techniques
##- **Formatage professionnel** prêt pour GitHub/LinkedIn

### **💼 Approche Business**
##- **4 catégories de bénéfices** (Économiques, Opérationnels, Stratégiques, Qualité)
##- **Cas d'usage variés** couvrant différents marchés
##- **ROI clairement exprimé** pour décideurs
##- **Positionnement premium** sans être intimidant

### **🛠️ Aspect Technique Équilibré**
##- **Prérequis accessibles** pour développeurs junior
##- **Bibliothèques optionnelles** pour évolutions
##- **Compatibilité large** (Windows/Mac/Linux)
##- **Requirements clairs** pour installation

## 🚀 **Comment Utiliser cette Fiche :**

##-1. **GitHub README** : Copiez-collez directement
##-2. **LinkedIn Post** : Adaptez par sections 
##-3. **Présentation Client** : Base solide pour slides
##-4. **Documentation** : Structure pour guide utilisateur
 
 
### Licence MIT


### Licence MIT pour la vente de produits numériques

### Copyright (c) 2025 [REFOÏA JEREMY LOUIS]
### SIRET 95108513300019 

# disponibilité de plus de produit numérique sur https://refoia-jeremy-tech.com/
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