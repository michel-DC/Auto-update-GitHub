#!/usr/bin/env python3
"""
Vérification finale du projet Auto-Update GitHub
Script de validation complète avant déploiement
"""

import os
import sys
from pathlib import Path
import json

def print_banner():
    """Affiche la bannière de vérification finale"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                    🔍 VÉRIFICATION FINALE                   ║
║                                                              ║
║  Validation complète du projet Auto-Update GitHub           ║
║  avant déploiement sur GitHub                               ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)

def check_required_files():
    """Vérifie que tous les fichiers requis sont présents"""
    print("📁 Vérification des fichiers requis...")
    
    required_files = {
        # Core files
        '.github/workflows/auto-update.yml': 'Workflow GitHub Actions',
        'scripts/generate_report.py': 'Script principal',
        'daily-report.md': 'Document à mettre à jour',
        'README.md': 'Documentation principale',
        
        # Configuration
        'requirements.txt': 'Dépendances Python',
        'pyproject.toml': 'Configuration du projet',
        '.gitignore': 'Fichiers à ignorer',
        '.gitattributes': 'Attributs Git',
        '.editorconfig': 'Configuration éditeur',
        
        # Data
        'data/update_history.json': 'Historique des mises à jour',
        'config/project_config.json': 'Configuration du projet',
        'config/timezone_config.py': 'Configuration des fuseaux horaires',
        
        # Scripts
        'scripts/test_local.py': 'Tests locaux',
        'scripts/validate_project.py': 'Validation du projet',
        'scripts/setup_project.py': 'Configuration du projet',
        'scripts/run_tests.py': 'Lancement des tests',
        'scripts/demo.py': 'Démonstration',
        
        # Tests
        'tests/__init__.py': 'Module de tests',
        'tests/test_generate_report.py': 'Tests unitaires',
        'tests/test_config.py': 'Configuration des tests',
        'tests/README.md': 'Documentation des tests',
        
        # Documentation
        'DEVELOPER.md': 'Guide développeur',
        'CONTRIBUTING.md': 'Guide de contribution',
        'SECURITY.md': 'Politique de sécurité',
        'SUPPORT.md': 'Guide de support',
        'AUTHORS.md': 'Auteurs et contributeurs',
        'CHANGELOG.md': 'Historique des versions',
        'CODE_OF_CONDUCT.md': 'Code de conduite',
        'LICENSE': 'Licence du projet',
        
        # Deployment
        'deploy.ps1': 'Script de déploiement Windows',
        'deploy.sh': 'Script de déploiement Linux/Mac',
        
        # VS Code
        '.vscode/settings.json': 'Configuration VS Code',
        '.vscode/extensions.json': 'Extensions VS Code',
        '.vscode/tasks.json': 'Tâches VS Code',
        '.vscode/launch.json': 'Lancements VS Code',
        
        # GitHub
        'FUNDING.yml': 'Configuration de financement',
    }
    
    missing_files = []
    present_files = []
    
    for file_path, description in required_files.items():
        if Path(file_path).exists():
            present_files.append((file_path, description))
            print(f"✅ {file_path}")
        else:
            missing_files.append((file_path, description))
            print(f"❌ {file_path} - MANQUANT")
    
    print(f"\n📊 Résultat: {len(present_files)}/{len(required_files)} fichiers présents")
    
    if missing_files:
        print("\n⚠️  Fichiers manquants:")
        for file_path, description in missing_files:
            print(f"   - {file_path}: {description}")
        return False
    
    return True

def check_file_structure():
    """Vérifie la structure des répertoires"""
    print("\n🏗️  Vérification de la structure...")
    
    required_dirs = [
        '.github',
        '.github/workflows',
        '.vscode',
        'scripts',
        'tests',
        'config',
        'data'
    ]
    
    all_good = True
    
    for dir_path in required_dirs:
        if Path(dir_path).exists() and Path(dir_path).is_dir():
            print(f"✅ {dir_path}/")
        else:
            print(f"❌ {dir_path}/ - MANQUANT")
            all_good = False
    
    return all_good

def check_file_contents():
    """Vérifie le contenu de fichiers critiques"""
    print("\n📄 Vérification du contenu des fichiers...")
    
    # Vérifier le workflow GitHub Actions
    workflow_file = Path('.github/workflows/auto-update.yml')
    if workflow_file.exists():
        with open(workflow_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        required_elements = [
            'name:',
            'schedule:',
            'cron:',
            'python scripts/generate_report.py',
            'git commit',
            'git push'
        ]
        
        for element in required_elements:
            if element in content:
                print(f"✅ Workflow: {element}")
            else:
                print(f"❌ Workflow: {element} - MANQUANT")
                return False
    
    # Vérifier le script principal
    script_file = Path('scripts/generate_report.py')
    if script_file.exists():
        with open(script_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        required_functions = [
            'def get_current_time_info',
            'def test_api_connection',
            'def generate_report_content',
            'def main'
        ]
        
        for func in required_functions:
            if func in content:
                print(f"✅ Script: {func}")
            else:
                print(f"❌ Script: {func} - MANQUANT")
                return False
    
    # Vérifier la configuration
    config_file = Path('config/project_config.json')
    if config_file.exists():
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            required_keys = ['project_name', 'version', 'timezone', 'execution_hour']
            for key in required_keys:
                if key in config:
                    print(f"✅ Config: {key}")
                else:
                    print(f"❌ Config: {key} - MANQUANT")
                    return False
        except Exception as e:
            print(f"❌ Config: Erreur JSON - {e}")
            return False
    
    return True

def check_git_status():
    """Vérifie le statut Git"""
    print("\n🔧 Vérification du statut Git...")
    
    # Vérifier si on est dans un repo Git
    if not Path('.git').exists():
        print("⚠️  Pas encore un repository Git")
        print("💡 Exécutez: git init")
        return False
    
    print("✅ Repository Git initialisé")
    return True

def check_python_dependencies():
    """Vérifie les dépendances Python"""
    print("\n🐍 Vérification des dépendances Python...")
    
    required_packages = ['requests', 'dateutil']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - MANQUANT")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n💡 Installez les packages manquants:")
        print(f"   pip install {' '.join(missing_packages)}")
        return False
    
    return True

def estimate_project_size():
    """Estime la taille du projet"""
    print("\n📊 Statistiques du projet...")
    
    # Compter les fichiers
    python_files = list(Path('.').rglob('*.py'))
    md_files = list(Path('.').rglob('*.md'))
    yml_files = list(Path('.').rglob('*.yml'))
    json_files = list(Path('.').rglob('*.json'))
    
    print(f"📄 Fichiers Python: {len(python_files)}")
    print(f"📄 Fichiers Markdown: {len(md_files)}")
    print(f"📄 Fichiers YAML: {len(yml_files)}")
    print(f"📄 Fichiers JSON: {len(json_files)}")
    
    # Compter les lignes de code
    total_lines = 0
    for py_file in python_files:
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                lines = len(f.readlines())
                total_lines += lines
        except:
            pass
    
    print(f"📝 Lignes de code Python: ~{total_lines}")
    
    # Taille des fichiers
    total_size = 0
    for file_path in Path('.').rglob('*'):
        if file_path.is_file():
            total_size += file_path.stat().st_size
    
    print(f"💾 Taille totale: ~{total_size / 1024:.1f} KB")

def generate_deployment_checklist():
    """Génère une checklist de déploiement"""
    print("\n📋 CHECKLIST DE DÉPLOIEMENT")
    print("=" * 50)
    
    checklist = [
        "Créer un nouveau repository sur GitHub",
        "Configurer le nom du repository",
        "Ajouter une description au repository",
        "Configurer le repository comme public ou privé",
        "Initialiser Git localement (git init)",
        "Ajouter le remote GitHub (git remote add origin <url>)",
        "Ajouter tous les fichiers (git add .)",
        "Faire le commit initial (git commit -m \"Initial commit\")",
        "Pusher vers GitHub (git push -u origin main)",
        "Aller dans Settings > Actions > General",
        "Activer 'Read and write permissions'",
        "Activer 'Allow GitHub Actions to create and approve pull requests'",
        "Tester manuellement le workflow dans l'onglet Actions",
        "Vérifier que le rapport est généré",
        "Attendre l'exécution automatique demain à 9h UTC",
        "Configurer les notifications si nécessaire",
        "Personnaliser le contenu selon vos besoins",
        "Documenter vos modifications personnelles"
    ]
    
    for i, item in enumerate(checklist, 1):
        print(f"{i:2d}. [ ] {item}")

def main():
    """Fonction principale de vérification finale"""
    print_banner()
    
    checks = [
        ("Fichiers requis", check_required_files),
        ("Structure des répertoires", check_file_structure),
        ("Contenu des fichiers", check_file_contents),
        ("Statut Git", check_git_status),
        ("Dépendances Python", check_python_dependencies)
    ]
    
    results = []
    
    for check_name, check_func in checks:
        print(f"\n🔍 {check_name}...")
        try:
            result = check_func()
            results.append((check_name, result))
        except Exception as e:
            print(f"❌ Erreur: {e}")
            results.append((check_name, False))
    
    # Statistiques du projet
    estimate_project_size()
    
    # Résumé final
    print("\n" + "=" * 60)
    print("🎯 RÉSUMÉ DE LA VÉRIFICATION FINALE")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"📊 Vérifications: {passed}/{total} réussies")
    print()
    
    for check_name, result in results:
        status = "✅ RÉUSSI" if result else "❌ ÉCHOUÉ"
        print(f"{check_name:30} {status}")
    
    if passed == total:
        print("\n🎉 PROJET VALIDÉ - PRÊT POUR LE DÉPLOIEMENT !")
        print("=" * 60)
        generate_deployment_checklist()
        print("\n🚀 Bon déploiement !")
        return True
    else:
        print("\n⚠️  PROJET INCOMPLET")
        print("🔧 Corrigez les erreurs ci-dessus avant le déploiement")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
