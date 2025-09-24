#!/usr/bin/env python3
"""
Configuration des tests pour le projet Auto-Update GitHub
"""

import os
import sys
from pathlib import Path

# Configuration des tests
TEST_CONFIG = {
    'test_data_dir': 'test_data',
    'test_history_file': 'test_data/test_history.json',
    'test_report_file': 'test_data/test_report.md',
    'mock_api_responses': True,
    'test_timezone': 'UTC',
    'test_execution_hour': 9
}

# Configuration des APIs de test
TEST_APIS = {
    'httpbin': {
        'url': 'https://httpbin.org/json',
        'timeout': 5,
        'expected_status': 200
    },
    'github': {
        'url': 'https://api.github.com/zen',
        'timeout': 5,
        'expected_status': 200
    }
}

# Configuration des données de test
TEST_DATA = {
    'sample_time_info': {
        'datetime': '2024-01-15T09:00:00Z',
        'timestamp': 1705312800,
        'weekday': 'Monday',
        'day_of_year': 15,
        'days_since_2000': 8766,
        'seconds_today': 32400
    },
    'sample_api_info': {
        'status': 'success',
        'response_time': 0.5,
        'status_code': 200
    },
    'sample_history': [
        {
            'date': '2024-01-15',
            'time': '09:00:00',
            'status': 'success',
            'details': 'Test entry'
        }
    ]
}

# Configuration des environnements de test
TEST_ENVIRONMENTS = {
    'local': {
        'python_path': sys.executable,
        'working_dir': Path.cwd(),
        'test_mode': True
    },
    'github_actions': {
        'python_path': '/usr/bin/python3',
        'working_dir': '/github/workspace',
        'test_mode': False
    }
}

def get_test_config():
    """Retourne la configuration de test"""
    return TEST_CONFIG

def get_test_apis():
    """Retourne la configuration des APIs de test"""
    return TEST_APIS

def get_test_data():
    """Retourne les données de test"""
    return TEST_DATA

def get_test_environment():
    """Détermine l'environnement de test actuel"""
    if os.getenv('GITHUB_ACTIONS') == 'true':
        return 'github_actions'
    else:
        return 'local'

def setup_test_environment():
    """Configure l'environnement de test"""
    env = get_test_environment()
    config = TEST_ENVIRONMENTS[env]
    
    # Créer le répertoire de test
    test_dir = Path(TEST_CONFIG['test_data_dir'])
    test_dir.mkdir(exist_ok=True)
    
    # Configurer les variables d'environnement
    os.environ['TEST_MODE'] = 'true'
    os.environ['TEST_DATA_DIR'] = str(test_dir)
    
    return config

def cleanup_test_environment():
    """Nettoie l'environnement de test"""
    test_dir = Path(TEST_CONFIG['test_data_dir'])
    if test_dir.exists():
        import shutil
        shutil.rmtree(test_dir)
    
    # Nettoyer les variables d'environnement
    if 'TEST_MODE' in os.environ:
        del os.environ['TEST_MODE']
    if 'TEST_DATA_DIR' in os.environ:
        del os.environ['TEST_DATA_DIR']

if __name__ == "__main__":
    print("🧪 Configuration des tests")
    print("=" * 40)
    print(f"Environnement: {get_test_environment()}")
    print(f"Configuration: {get_test_config()}")
    print(f"APIs de test: {list(get_test_apis().keys())}")
    print(f"Données de test: {list(get_test_data().keys())}")
