# Symfony Launcher 🚀

[English version below](#english) | [Version française](#français)

<a name="français"></a>
# Version Française 🇫🇷

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

---

<a name="english"></a>
# English Version 🇬🇧

A simple Python script to automate the startup of your Symfony development environment on Windows.

## 🔧 Features

- Automatically launches `npm run watch` in a PowerShell window
- Stops and restarts the Symfony server (`symfony server:stop` then `symfony server:start`) in another window
- Option to create a shortcut on your desktop to launch your environment with a single click

## 📋 Requirements

- Windows
- Python 3.x installed
- A functional Symfony project with npm configured

## 💻 Installation

1. Download the `symfony_launcher.py` file to your Symfony project (or anywhere on your computer)
2. Customize your project path if necessary (see Configuration)

## ⚙️ Configuration

Open the `symfony_launcher.py` file and modify the `get_project_path()` function to specify the full path to your Symfony project:

```python
def get_project_path():
    # ======================================================
    # CONFIGURATION: Define the path to your Symfony project here
    # Example: return "C:\\Users\\your_name\\projects\\my_symfony_project"
    # ======================================================
    # By default, the script uses the current directory
    return "C:\\path\\to\\your\\symfony\\project"
```

## 🚀 Usage

### Directly launch the environment

```bash
python symfony_launcher.py
```

### Create a shortcut on your desktop

```bash
python symfony_launcher.py install
```

This will create a `SymfonyStarter.bat` file on your desktop that you can launch with a single click.