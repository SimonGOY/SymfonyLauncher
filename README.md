# Symfony Launcher 🚀

Un script Python simple pour automatiser le démarrage de votre environnement de développement Symfony sous Windows.

## 🔧 Fonctionnalités

- Lance automatiquement `npm run watch` dans une fenêtre PowerShell
- Arrête et redémarre le serveur Symfony (`symfony server:stop` puis `symfony server:start`) dans une autre fenêtre
- Possibilité de créer un raccourci sur votre bureau pour lancer votre environnement en un clic

## 📋 Prérequis

- Windows
- Python 3.x installé
- Un projet Symfony fonctionnel avec npm configuré

## 💻 Installation

1. Téléchargez le fichier `symfony_launcher.py` dans votre projet Symfony (ou n'importe où sur votre ordinateur)
2. Personnalisez le chemin de votre projet si nécessaire (voir Configuration)

## ⚙️ Configuration

Ouvrez le fichier `symfony_launcher.py` et modifiez la fonction `get_project_path()` pour spécifier le chemin complet vers votre projet Symfony :

```python
def get_project_path():
    # ======================================================
    # PARAMÉTRAGE : Définissez ici le chemin vers votre projet Symfony
    # Exemple: return "C:\\Users\\votre_nom\\projets\\mon_projet_symfony"
    # ======================================================
    # Par défaut, le script utilise le répertoire courant
    return "C:\\chemin\\vers\\votre\\projet\\symfony"
```

## 🚀 Utilisation

### Lancer directement l'environnement

```bash
python symfony_launcher.py
```

### Créer un raccourci sur le bureau

```bash
python symfony_launcher.py install
```

Cela créera un fichier `SymfonyStarter.bat` sur votre bureau que vous pourrez lancer d'un simple clic.
