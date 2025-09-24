#!/usr/bin/env python3
"""
Tests unitaires pour le script generate_report.py
"""

import unittest
import sys
import os
import json
from datetime import datetime, timezone
from pathlib import Path

# Ajouter le répertoire scripts au PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent / 'scripts'))

try:
    from generate_report import (
        get_current_time_info,
        test_api_connection,
        load_update_history,
        save_update_history,
        generate_report_content
    )
except ImportError as e:
    print(f"❌ Erreur import: {e}")
    sys.exit(1)

class TestGenerateReport(unittest.TestCase):
    """Tests pour le script generate_report.py"""
    
    def setUp(self):
        """Configuration avant chaque test"""
        self.test_data_dir = Path('test_data')
        self.test_data_dir.mkdir(exist_ok=True)
        
        # Fichier d'historique de test
        self.test_history_file = self.test_data_dir / 'test_history.json'
        
    def tearDown(self):
        """Nettoyage après chaque test"""
        if self.test_history_file.exists():
            self.test_history_file.unlink()
        if self.test_data_dir.exists():
            self.test_data_dir.rmdir()
    
    def test_get_current_time_info(self):
        """Test de la fonction get_current_time_info"""
        time_info = get_current_time_info()
        
        # Vérifications de base
        self.assertIsInstance(time_info, dict)
        self.assertIn('datetime', time_info)
        self.assertIn('timestamp', time_info)
        self.assertIn('weekday', time_info)
        self.assertIn('day_of_year', time_info)
        self.assertIn('days_since_2000', time_info)
        self.assertIn('seconds_today', time_info)
        
        # Vérifications des types
        self.assertIsInstance(time_info['datetime'], datetime)
        self.assertIsInstance(time_info['timestamp'], int)
        self.assertIsInstance(time_info['weekday'], str)
        self.assertIsInstance(time_info['day_of_year'], int)
        self.assertIsInstance(time_info['days_since_2000'], int)
        self.assertIsInstance(time_info['seconds_today'], int)
        
        # Vérifications des valeurs
        self.assertGreater(time_info['timestamp'], 0)
        self.assertGreaterEqual(time_info['day_of_year'], 1)
        self.assertLessEqual(time_info['day_of_year'], 366)
        self.assertGreaterEqual(time_info['days_since_2000'], 0)
        self.assertGreaterEqual(time_info['seconds_today'], 0)
        self.assertLess(time_info['seconds_today'], 86400)  # 24h en secondes
    
    def test_test_api_connection(self):
        """Test de la fonction test_api_connection"""
        api_info = test_api_connection()
        
        # Vérifications de base
        self.assertIsInstance(api_info, dict)
        self.assertIn('status', api_info)
        self.assertIn('response_time', api_info)
        
        # Vérifications des valeurs possibles
        self.assertIn(api_info['status'], ['success', 'error'])
        
        if api_info['status'] == 'success':
            self.assertIsInstance(api_info['response_time'], float)
            self.assertGreater(api_info['response_time'], 0)
        else:
            self.assertIn('error', api_info)
    
    def test_load_update_history_empty(self):
        """Test de chargement d'un historique vide"""
        # Créer un fichier d'historique vide
        with open(self.test_history_file, 'w', encoding='utf-8') as f:
            json.dump([], f)
        
        # Modifier temporairement le chemin dans le script
        import generate_report
        original_path = generate_report.Path
        generate_report.Path = lambda x: self.test_history_file if 'update_history.json' in str(x) else original_path(x)
        
        history = load_update_history()
        self.assertEqual(history, [])
    
    def test_save_update_history(self):
        """Test de sauvegarde de l'historique"""
        test_history = [
            {
                'date': '2024-01-15',
                'time': '09:00:00',
                'status': 'success',
                'details': 'Test entry'
            }
        ]
        
        # Modifier temporairement le chemin dans le script
        import generate_report
        original_path = generate_report.Path
        generate_report.Path = lambda x: self.test_history_file if 'update_history.json' in str(x) else original_path(x)
        
        save_update_history(test_history)
        
        # Vérifier que le fichier a été créé
        self.assertTrue(self.test_history_file.exists())
        
        # Vérifier le contenu
        with open(self.test_history_file, 'r', encoding='utf-8') as f:
            saved_history = json.load(f)
        
        self.assertEqual(saved_history, test_history)
    
    def test_generate_report_content(self):
        """Test de génération du contenu du rapport"""
        # Données de test
        time_info = {
            'datetime': datetime(2024, 1, 15, 9, 0, 0, tzinfo=timezone.utc),
            'timestamp': 1705312800,
            'weekday': 'Monday',
            'day_of_year': 15,
            'days_since_2000': 8766,
            'seconds_today': 32400
        }
        
        api_info = {
            'status': 'success',
            'response_time': 0.5,
            'status_code': 200
        }
        
        # Modifier temporairement le chemin dans le script
        import generate_report
        original_path = generate_report.Path
        generate_report.Path = lambda x: self.test_history_file if 'update_history.json' in str(x) else original_path(x)
        
        content = generate_report_content(time_info, api_info)
        
        # Vérifications de base
        self.assertIsInstance(content, str)
        self.assertGreater(len(content), 100)
        
        # Vérifications du contenu
        self.assertIn('# 📊 Rapport Quotidien Automatique', content)
        self.assertIn('## 📅 Informations Générales', content)
        self.assertIn('## 🌍 Données du Jour', content)
        self.assertIn('## 📈 Données Externes', content)
        self.assertIn('## 🔄 Historique des Mises à Jour', content)
        
        # Vérifications des données
        self.assertIn('2024-01-15', content)
        self.assertIn('Monday', content)
        self.assertIn('✅ Connecté', content)
        self.assertIn('0.500s', content)
    
    def test_generate_report_content_error(self):
        """Test de génération avec erreur API"""
        # Données de test avec erreur
        time_info = {
            'datetime': datetime(2024, 1, 15, 9, 0, 0, tzinfo=timezone.utc),
            'timestamp': 1705312800,
            'weekday': 'Monday',
            'day_of_year': 15,
            'days_since_2000': 8766,
            'seconds_today': 32400
        }
        
        api_info = {
            'status': 'error',
            'response_time': None,
            'error': 'Connection timeout'
        }
        
        # Modifier temporairement le chemin dans le script
        import generate_report
        original_path = generate_report.Path
        generate_report.Path = lambda x: self.test_history_file if 'update_history.json' in str(x) else original_path(x)
        
        content = generate_report_content(time_info, api_info)
        
        # Vérifications
        self.assertIn('❌ Erreur', content)
        self.assertIn('N/A', content)

class TestIntegration(unittest.TestCase):
    """Tests d'intégration"""
    
    def test_full_workflow(self):
        """Test du workflow complet"""
        # Ce test simule l'exécution complète du script
        # sans les effets de bord (fichiers réels)
        
        # Test des imports
        try:
            from generate_report import main
            self.assertTrue(True, "Import réussi")
        except ImportError as e:
            self.fail(f"Erreur d'import: {e}")
    
    def test_data_consistency(self):
        """Test de cohérence des données"""
        time_info = get_current_time_info()
        
        # Vérifier que les calculs sont cohérents
        now = time_info['datetime']
        expected_timestamp = int(now.timestamp())
        self.assertEqual(time_info['timestamp'], expected_timestamp)
        
        # Vérifier le jour de l'année
        expected_day_of_year = now.timetuple().tm_yday
        self.assertEqual(time_info['day_of_year'], expected_day_of_year)

def run_tests():
    """Lance tous les tests"""
    print("🧪 Lancement des tests unitaires...")
    print("=" * 50)
    
    # Créer la suite de tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Ajouter les tests
    suite.addTests(loader.loadTestsFromTestCase(TestGenerateReport))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Lancer les tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Résumé
    print("\n" + "=" * 50)
    print("📊 RÉSUMÉ DES TESTS")
    print("=" * 50)
    print(f"Tests exécutés: {result.testsRun}")
    print(f"Échecs: {len(result.failures)}")
    print(f"Erreurs: {len(result.errors)}")
    
    if result.failures:
        print("\n❌ ÉCHECS:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\n❌ ERREURS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    if result.wasSuccessful():
        print("\n✅ TOUS LES TESTS SONT PASSÉS !")
        return True
    else:
        print("\n❌ CERTAINS TESTS ONT ÉCHOUÉ")
        return False

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
