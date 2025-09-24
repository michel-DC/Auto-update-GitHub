#!/usr/bin/env python3
"""
Script de validation complète du projet
Vérifie que tous les fichiers sont présents et correctement configurés
"""

import os
import sys
import json
import yaml
from pathlib import Path
from datetime import datetime

def validate_file_structure():
    """Valide la structure des fichiers du projet"""
    print("📁 Validation de la structure des fichiers...")
    
    required_files = {
        '.github/workflows/auto-update.yml': 'Workflow GitHub Actions',
        'scripts/generate_report.py': 'Script principal de génération',
        'scripts/test_local.py': 'Script de test local',
        'scripts/setup_project.py': 'Script de configuration',
        'scripts/demo.py': 'Script de démonstration',
        'scripts/validate_project.py': 'Script de validation',
        'data/update_history.json': 'Fichier d\'historique',
        'config/project_config.json': 'Configuration du projet',
        'config/timezone_config.py': 'Configuration des fuseaux horaires',
        'daily-report.md': 'Rapport généré automatiquement',
        'README.md': 'Documentation principale',
        'requirements.txt': 'Dépendances Python',
        '.gitignore': 'Fichiers à ignorer'
    }
    
    missing_files = []
    present_files = []
    
    for file_path, description in required_files.items():
        if Path(file_path).exists():
            present_files.append((file_path, description))
            print(f"✅ {file_path}: {description}")
        else:
            missing_files.append((file_path, description))
            print(f"❌ {file_path}: {description} - MANQUANT")
    
    return len(missing_files) == 0, missing_files, present_files

def validate_github_workflow():
    """Valide la configuration du workflow GitHub Actions"""
    print("\n⚙️  Validation du workflow GitHub Actions...")
    
    workflow_file = Path('.github/workflows/auto-update.yml')
    if not workflow_file.exists():
        print("❌ Fichier workflow manquant")
        return False
    
    try:
        with open(workflow_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifications essentielles
        checks = [
            ('name:', 'Nom du workflow'),
            ('on:', 'Déclencheurs'),
            ('schedule:', 'Planification'),
            ('cron:', 'Expression cron'),
            ('jobs:', 'Jobs définis'),
            ('python scripts/generate_report.py', 'Exécution du script'),
            ('git config', 'Configuration Git'),
            ('git commit', 'Commit automatique'),
            ('git push', 'Push automatique')
        ]
        
        all_good = True
        for check, description in checks:
            if check in content:
                print(f"✅ {description}")
            else:
                print(f"❌ {description} - MANQUANT")
                all_good = False
        
        return all_good
        
    except Exception as e:
        print(f"❌ Erreur lecture workflow: {e}")
        return False

def validate_python_script():
    """Valide le script Python principal"""
    print("\n🐍 Validation du script Python...")
    
    script_file = Path('scripts/generate_report.py')
    if not script_file.exists():
        print("❌ Script principal manquant")
        return False
    
    try:
        with open(script_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifications du script
        checks = [
            ('import requests', 'Import requests'),
            ('import json', 'Import json'),
            ('from datetime import', 'Import datetime'),
            ('def get_current_time_info', 'Fonction temps'),
            ('def test_api_connection', 'Fonction API'),
            ('def generate_report_content', 'Fonction génération'),
            ('def main', 'Fonction principale'),
            ('if __name__ == "__main__"', 'Point d\'entrée')
        ]
        
        all_good = True
        for check, description in checks:
            if check in content:
                print(f"✅ {description}")
            else:
                print(f"❌ {description} - MANQUANT")
                all_good = False
        
        return all_good
        
    except Exception as e:
        print(f"❌ Erreur lecture script: {e}")
        return False

def validate_configuration():
    """Valide les fichiers de configuration"""
    print("\n⚙️  Validation de la configuration...")
    
    # Validation project_config.json
    config_file = Path('config/project_config.json')
    if config_file.exists():
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            required_keys = ['project_name', 'version', 'timezone', 'execution_hour']
            for key in required_keys:
                if key in config:
                    print(f"✅ Configuration: {key}")
                else:
                    print(f"❌ Configuration: {key} - MANQUANT")
                    return False
        except Exception as e:
            print(f"❌ Erreur lecture config: {e}")
            return False
    else:
        print("❌ Fichier de configuration manquant")
        return False
    
    # Validation requirements.txt
    req_file = Path('requirements.txt')
    if req_file.exists():
        with open(req_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'requests' in content and 'python-dateutil' in content:
            print("✅ Dépendances Python")
        else:
            print("❌ Dépendances Python - INCOMPLÈTES")
            return False
    else:
        print("❌ Fichier requirements.txt manquant")
        return False
    
    return True

def validate_documentation():
    """Valide la documentation"""
    print("\n📚 Validation de la documentation...")
    
    readme_file = Path('README.md')
    if not readme_file.exists():
        print("❌ README.md manquant")
        return False
    
    with open(readme_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifications de la documentation
    checks = [
        ('# 🤖 Auto-Update GitHub Project', 'Titre principal'),
        ('## 📋 Fonctionnalités', 'Section fonctionnalités'),
        ('## 🚀 Installation', 'Section installation'),
        ('## ⚙️ Configuration', 'Section configuration'),
        ('## 📊 Contenu Généré', 'Section contenu'),
        ('## 🐛 Dépannage', 'Section dépannage')
    ]
    
    all_good = True
    for check, description in checks:
        if check in content:
            print(f"✅ {description}")
        else:
            print(f"❌ {description} - MANQUANT")
            all_good = False
    
    return all_good

def validate_data_files():
    """Valide les fichiers de données"""
    print("\n📊 Validation des fichiers de données...")
    
    # Validation update_history.json
    history_file = Path('data/update_history.json')
    if history_file.exists():
        try:
            with open(history_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
            
            if isinstance(history, list):
                print("✅ Historique JSON valide")
            else:
                print("❌ Historique JSON - FORMAT INVALIDE")
                return False
        except Exception as e:
            print(f"❌ Erreur lecture historique: {e}")
            return False
    else:
        print("❌ Fichier historique manquant")
        return False
    
    # Validation daily-report.md
    report_file = Path('daily-report.md')
    if report_file.exists():
        with open(report_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '# 📊 Rapport Quotidien Automatique' in content:
            print("✅ Rapport Markdown valide")
        else:
            print("❌ Rapport Markdown - FORMAT INVALIDE")
            return False
    else:
        print("❌ Fichier rapport manquant")
        return False
    
    return True

def generate_validation_report(results):
    """Génère un rapport de validation"""
    print("\n" + "=" * 60)
    print("📊 RAPPORT DE VALIDATION DU PROJET")
    print("=" * 60)
    
    total_checks = len(results)
    passed_checks = sum(1 for result in results if result[1])
    
    print(f"🎯 Résultat global: {passed_checks}/{total_checks} validations réussies")
    print()
    
    for check_name, result in results:
        status = "✅ RÉUSSI" if result else "❌ ÉCHOUÉ"
        print(f"{check_name:30} {status}")
    
    print()
    if passed_checks == total_checks:
        print("🎉 PROJET VALIDÉ - Prêt pour le déploiement !")
        print("\n📋 Prochaines étapes:")
        print("1. git add .")
        print("2. git commit -m 'Initial commit: Auto-update project'")
        print("3. git push origin main")
        print("4. Activer les Actions dans GitHub")
        return True
    else:
        print("⚠️  PROJET INCOMPLET - Vérifiez les erreurs ci-dessus")
        return False

def main():
    """Fonction principale de validation"""
    print("🔍 VALIDATION COMPLÈTE DU PROJET AUTO-UPDATE GITHUB")
    print("=" * 60)
    
    validations = [
        ("Structure des fichiers", validate_file_structure),
        ("Workflow GitHub Actions", validate_github_workflow),
        ("Script Python", validate_python_script),
        ("Configuration", validate_configuration),
        ("Documentation", validate_documentation),
        ("Fichiers de données", validate_data_files)
    ]
    
    results = []
    
    for validation_name, validation_func in validations:
        print(f"\n🔧 {validation_name}...")
        try:
            result = validation_func()
            results.append((validation_name, result))
        except Exception as e:
            print(f"❌ Erreur inattendue: {e}")
            results.append((validation_name, False))
    
    return generate_validation_report(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
