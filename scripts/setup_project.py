#!/usr/bin/env python3
"""
Script de configuration initiale du projet
Crée la structure nécessaire et configure l'environnement
"""

import os
import sys
from pathlib import Path
import json

def create_directory_structure():
    """Crée la structure de répertoires nécessaire"""
    print("📁 Création de la structure de répertoires...")
    
    directories = [
        '.github/workflows',
        'scripts',
        'data',
        'config'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Créé: {directory}")

def create_initial_data_files():
    """Crée les fichiers de données initiaux"""
    print("\n📄 Création des fichiers de données initiaux...")
    
    # Fichier d'historique vide
    history_file = Path('data/update_history.json')
    if not history_file.exists():
        with open(history_file, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=2)
        print("✅ Créé: data/update_history.json")
    
    # Fichier de configuration
    config_file = Path('config/project_config.json')
    if not config_file.exists():
        config = {
            "project_name": "Auto-Update GitHub Project",
            "version": "1.0.0",
            "timezone": "UTC",
            "execution_hour": 9,
            "api_endpoints": [
                "https://httpbin.org/json"
            ],
            "features": {
                "auto_update": True,
                "api_testing": True,
                "history_tracking": True
            }
        }
        
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        print("✅ Créé: config/project_config.json")

def check_dependencies():
    """Vérifie et installe les dépendances"""
    print("\n📦 Vérification des dépendances...")
    
    required_packages = ['requests', 'python-dateutil']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package} installé")
        except ImportError:
            print(f"❌ {package} manquant")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Packages manquants: {', '.join(missing_packages)}")
        print("💡 Installez-les avec: pip install -r requirements.txt")
        return False
    
    return True

def create_git_hooks():
    """Crée les hooks Git pour la validation"""
    print("\n🔗 Configuration des hooks Git...")
    
    # Hook pre-commit pour tester le script
    pre_commit_hook = Path('.git/hooks/pre-commit')
    if not pre_commit_hook.exists():
        hook_content = """#!/bin/bash
# Hook pre-commit pour tester le script de génération
echo "🧪 Test du script de génération..."
python scripts/test_local.py
if [ $? -ne 0 ]; then
    echo "❌ Tests échoués, commit annulé"
    exit 1
fi
echo "✅ Tests passés, commit autorisé"
"""
        
        with open(pre_commit_hook, 'w') as f:
            f.write(hook_content)
        
        # Rendre le hook exécutable (Unix/Linux/Mac)
        if os.name != 'nt':  # Pas Windows
            os.chmod(pre_commit_hook, 0o755)
        
        print("✅ Hook pre-commit créé")

def validate_github_actions():
    """Valide la configuration GitHub Actions"""
    print("\n🔍 Validation de la configuration GitHub Actions...")
    
    workflow_file = Path('.github/workflows/auto-update.yml')
    if not workflow_file.exists():
        print("❌ Fichier workflow manquant")
        return False
    
    # Vérifications basiques
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    required_elements = [
        'name:',
        'on:',
        'schedule:',
        'cron:',
        'jobs:',
        'python scripts/generate_report.py'
    ]
    
    for element in required_elements:
        if element in content:
            print(f"✅ Trouvé: {element}")
        else:
            print(f"❌ Manquant: {element}")
            return False
    
    return True

def create_documentation_links():
    """Crée des liens vers la documentation"""
    print("\n📚 Liens vers la documentation...")
    
    docs = {
        'README.md': 'Documentation principale',
        'daily-report.md': 'Rapport généré automatiquement',
        'scripts/test_local.py': 'Tests locaux',
        'config/timezone_config.py': 'Configuration des fuseaux horaires'
    }
    
    for file_path, description in docs.items():
        if Path(file_path).exists():
            print(f"✅ {file_path}: {description}")
        else:
            print(f"❌ {file_path}: Manquant")

def main():
    """Fonction principale de configuration"""
    print("🚀 Configuration du projet Auto-Update GitHub")
    print("=" * 50)
    
    steps = [
        ("Structure de répertoires", create_directory_structure),
        ("Fichiers de données", create_initial_data_files),
        ("Dépendances", check_dependencies),
        ("Hooks Git", create_git_hooks),
        ("GitHub Actions", validate_github_actions),
        ("Documentation", create_documentation_links)
    ]
    
    results = []
    
    for step_name, step_func in steps:
        print(f"\n🔧 {step_name}...")
        try:
            result = step_func()
            results.append((step_name, result))
        except Exception as e:
            print(f"❌ Erreur: {e}")
            results.append((step_name, False))
    
    # Résumé
    print("\n" + "=" * 50)
    print("📊 RÉSUMÉ DE LA CONFIGURATION")
    print("=" * 50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for step_name, result in results:
        status = "✅ RÉUSSI" if result else "❌ ÉCHOUÉ"
        print(f"{step_name}: {status}")
    
    print(f"\n🎯 Configuration: {passed}/{total} étapes réussies")
    
    if passed == total:
        print("\n🎉 Configuration terminée avec succès !")
        print("\n📋 Prochaines étapes:")
        print("1. Commitez et pushez vers GitHub")
        print("2. Activez les Actions dans les paramètres du repository")
        print("3. Testez manuellement le workflow")
        print("4. Vérifiez l'exécution automatique demain à 9h UTC")
        return 0
    else:
        print("\n⚠️  Configuration incomplète. Vérifiez les erreurs ci-dessus.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
