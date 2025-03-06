import subprocess
import os
import sys

def get_project_path():
    # ======================================================
    # PARAMÉTRAGE : Définissez ici le chemin vers votre projet Symfony
    # Exemple: return "C:\\Users\\votre_nom\\projets\\mon_projet_symfony"
    # ======================================================
    # Par défaut, le script utilise le répertoire courant
    return os.getcwd()

def run_symfony_project():
    project_path = get_project_path()
    
    # Changer le répertoire de travail vers le projet Symfony
    os.chdir(project_path)
    
    # Lancer les commandes dans des fenêtres PowerShell séparées
    subprocess.Popen(['start', 'powershell', '-NoExit', '-Command', 'npm run watch'], shell=True)
    subprocess.Popen(['start', 'powershell', '-NoExit', '-Command', 'symfony server:stop; symfony server:start'], shell=True)

def create_launcher():
    script_path = os.path.abspath(__file__)
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    shortcut_path = os.path.join(desktop_path, "SymfonyStarter.bat")
    
    with open(shortcut_path, "w") as f:
        f.write(f'@echo off\npython "{script_path}"\n')
    
    print(f"Lanceur créé sur le bureau: {shortcut_path}")

if __name__ == "__main__":
    # Si aucun argument n'est passé, exécuter les commandes Symfony
    if len(sys.argv) == 1:
        run_symfony_project()
    # Si l'argument "install" est passé, créer un lanceur sur le bureau
    elif len(sys.argv) == 2 and sys.argv[1] == "install":
        create_launcher()
    else:
        print("Usage:")
        print("  python symfony_launcher.py         - Lance l'environnement Symfony")
        print("  python symfony_launcher.py install - Crée un raccourci sur le bureau")
