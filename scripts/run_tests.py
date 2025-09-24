#!/usr/bin/env python3
"""
Script de lancement de tous les tests du projet
"""

import sys
import os
import subprocess
from pathlib import Path

def run_command(command, description):
    """Exécute une commande et affiche le résultat"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - RÉUSSI")
            if result.stdout:
                print(f"📄 Sortie: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ {description} - ÉCHOUÉ")
            if result.stderr:
                print(f"📄 Erreur: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ {description} - ERREUR: {e}")
        return False

def check_python_version():
    """Vérifie la version de Python"""
    print("🐍 Vérification de la version Python...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Version trop ancienne")
        return False

def check_dependencies():
    """Vérifie les dépendances"""
    print("📦 Vérification des dépendances...")
    
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
        print(f"⚠️  Packages manquants: {', '.join(missing_packages)}")
        print("💡 Installez-les avec: pip install -r requirements.txt")
        return False
    
    return True

def run_unit_tests():
    """Lance les tests unitaires"""
    print("🧪 Lancement des tests unitaires...")
    
    test_file = Path('tests/test_generate_report.py')
    if not test_file.exists():
        print("❌ Fichier de tests manquant")
        return False
    
    return run_command(f"python {test_file}", "Tests unitaires")

def run_integration_tests():
    """Lance les tests d'intégration"""
    print("🔗 Lancement des tests d'intégration...")
    
    # Test du script principal
    return run_command("python scripts/generate_report.py", "Test du script principal")

def run_validation_tests():
    """Lance les tests de validation"""
    print("✅ Lancement des tests de validation...")
    
    return run_command("python scripts/validate_project.py", "Validation du projet")

def run_local_tests():
    """Lance les tests locaux"""
    print("🏠 Lancement des tests locaux...")
    
    return run_command("python scripts/test_local.py", "Tests locaux")

def run_demo():
    """Lance la démonstration"""
    print("🎬 Lancement de la démonstration...")
    
    return run_command("python scripts/demo.py", "Démonstration")

def generate_test_report(results):
    """Génère un rapport de tests"""
    print("\n" + "=" * 60)
    print("📊 RAPPORT DE TESTS")
    print("=" * 60)
    
    total_tests = len(results)
    passed_tests = sum(1 for result in results if result[1])
    
    print(f"🎯 Résultat global: {passed_tests}/{total_tests} tests réussis")
    print()
    
    for test_name, result in results:
        status = "✅ RÉUSSI" if result else "❌ ÉCHOUÉ"
        print(f"{test_name:30} {status}")
    
    print()
    if passed_tests == total_tests:
        print("🎉 TOUS LES TESTS SONT PASSÉS !")
        print("✅ Le projet est prêt pour le déploiement")
        return True
    else:
        print("⚠️  CERTAINS TESTS ONT ÉCHOUÉ")
        print("🔧 Vérifiez les erreurs ci-dessus avant le déploiement")
        return False

def main():
    """Fonction principale de tests"""
    print("🧪 SUITE DE TESTS COMPLÈTE")
    print("=" * 60)
    
    # Vérifications préliminaires
    print("🔍 Vérifications préliminaires...")
    
    if not check_python_version():
        print("❌ Version Python incompatible")
        return False
    
    if not check_dependencies():
        print("❌ Dépendances manquantes")
        return False
    
    print("✅ Vérifications préliminaires réussies")
    print()
    
    # Lancement des tests
    tests = [
        ("Tests unitaires", run_unit_tests),
        ("Tests d'intégration", run_integration_tests),
        ("Tests de validation", run_validation_tests),
        ("Tests locaux", run_local_tests),
        ("Démonstration", run_demo)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n🔧 {test_name}...")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Erreur inattendue: {e}")
            results.append((test_name, False))
    
    # Génération du rapport
    return generate_test_report(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
