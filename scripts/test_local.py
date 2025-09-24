#!/usr/bin/env python3
"""
Script de test local pour vérifier le bon fonctionnement
du générateur de rapport avant le déploiement
"""

import sys
import os
from pathlib import Path

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))

def test_imports():
    """Test des imports nécessaires"""
    print("🔍 Test des imports...")
    
    try:
        import requests
        print("✅ requests importé avec succès")
    except ImportError as e:
        print(f"❌ Erreur import requests: {e}")
        return False
    
    try:
        from datetime import datetime, timezone
        print("✅ datetime importé avec succès")
    except ImportError as e:
        print(f"❌ Erreur import datetime: {e}")
        return False
    
    try:
        import json
        print("✅ json importé avec succès")
    except ImportError as e:
        print(f"❌ Erreur import json: {e}")
        return False
    
    return True

def test_script_execution():
    """Test d'exécution du script principal"""
    print("\n🚀 Test d'exécution du script principal...")
    
    try:
        # Import et exécution du script principal
        from generate_report import main
        main()
        print("✅ Script exécuté avec succès")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution: {e}")
        return False

def test_file_creation():
    """Vérification de la création des fichiers"""
    print("\n📁 Vérification des fichiers créés...")
    
    files_to_check = [
        'daily-report.md',
        'data/update_history.json'
    ]
    
    all_good = True
    
    for file_path in files_to_check:
        if Path(file_path).exists():
            print(f"✅ {file_path} créé avec succès")
        else:
            print(f"❌ {file_path} manquant")
            all_good = False
    
    return all_good

def test_file_content():
    """Vérification du contenu des fichiers"""
    print("\n📄 Vérification du contenu...")
    
    # Vérifier daily-report.md
    if Path('daily-report.md').exists():
        with open('daily-report.md', 'r', encoding='utf-8') as f:
            content = f.read()
            
        required_sections = [
            '# 📊 Rapport Quotidien Automatique',
            '## 📅 Informations Générales',
            '## 🌍 Données du Jour',
            '## 📈 Données Externes',
            '## 🔄 Historique des Mises à Jour'
        ]
        
        for section in required_sections:
            if section in content:
                print(f"✅ Section '{section}' trouvée")
            else:
                print(f"❌ Section '{section}' manquante")
                return False
    
    # Vérifier update_history.json
    if Path('data/update_history.json').exists():
        try:
            import json
            with open('data/update_history.json', 'r', encoding='utf-8') as f:
                history = json.load(f)
            
            if isinstance(history, list) and len(history) > 0:
                print("✅ Historique JSON valide avec des entrées")
            else:
                print("❌ Historique JSON vide ou invalide")
                return False
        except Exception as e:
            print(f"❌ Erreur lecture JSON: {e}")
            return False
    
    return True

def main():
    """Fonction principale de test"""
    print("🧪 Début des tests locaux...")
    print("=" * 50)
    
    tests = [
        ("Imports", test_imports),
        ("Exécution script", test_script_execution),
        ("Création fichiers", test_file_creation),
        ("Contenu fichiers", test_file_content)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n🔬 Test: {test_name}")
        print("-" * 30)
        
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Erreur inattendue: {e}")
            results.append((test_name, False))
    
    # Résumé des tests
    print("\n" + "=" * 50)
    print("📊 RÉSUMÉ DES TESTS")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSÉ" if result else "❌ ÉCHOUÉ"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 Résultat: {passed}/{total} tests passés")
    
    if passed == total:
        print("🎉 Tous les tests sont passés ! Le projet est prêt pour GitHub.")
        return 0
    else:
        print("⚠️  Certains tests ont échoué. Vérifiez les erreurs ci-dessus.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
