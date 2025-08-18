import pyttsx3
from docx import Document

def word_to_audio(word_file, audio_file):
    # Charger le fichier Word
    document = Document(word_file)
    full_text = ""
    for paragraph in document.paragraphs:
        full_text += paragraph.text + "\n"

    # Configurer le moteur de synthèse vocale
    engine = pyttsx3.init()
    engine.save_to_file(full_text, audio_file)
    engine.runAndWait()
    print(f"Audio saved as {audio_file}")

# Exemple d'utilisation
word_file = "chapitre.docx"
audio_file = "votre_audio.mp3"
word_to_audio(word_file, audio_file)
 
### 🎙️ **Titre du script : WordToAudio Converter**
### Convertisseur de documents Word (.docx) en fichiers audio (.mp3) via synthèse vocale.
 
### 📝 **Description générale**
### Ce script permet de transformer le contenu textuel d’un document Word en un fichier audio grâce à la synthèse vocale. Il est idéal pour créer des versions audio de documents écrits, facilitant ainsi l’accessibilité et la consommation de contenu en mobilité.
 

### ⚙️ **Fonctionnalités principales**
###- 📄 Lecture complète du contenu d’un fichier `.docx`
###- 🔊 Conversion du texte en audio avec la bibliothèque `pyttsx3`
###- 💾 Sauvegarde automatique du fichier audio au format `.mp3` ou `.wav`
###- 🖥️ Exécution simple via une fonction Python personnalisée
 
### ✅ **Bénéfices**
###- 🔉 Accessibilité accrue pour les personnes malvoyantes ou dyslexiques
###- 📚 Possibilité d’écouter des documents en déplacement
###- 🕒 Gain de temps pour la lecture de longs textes
###- 🧠 Apprentissage auditif facilité
###- 🛠️ Facile à intégrer dans des projets plus larges (applications, bots, etc.)
 

### 📌 **Cas d’usage**
###- Lecture de chapitres de livres ou cours en format audio
###- Génération de podcasts à partir de contenus écrits
###- Création de supports audio pour la formation ou l’e-learning
###- Lecture vocale de rapports ou documents professionnels
###- Outils d’assistance pour personnes en situation de handicap
 

### 🧰 **Prérequis techniques**
###- Python 3.x installé
###- Bibliothèques nécessaires :
###  pip install pyttsx3 python-docx
### - Fichier Word au format `.docx` (ex. : `chapitre.docx`)
###- Droits d’écriture dans le répertoire de sortie pour sauvegarder l’audio 
 
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