# 🧪 Tests du Projet Auto-Update GitHub

> **Documentation des tests pour le projet Auto-Update GitHub**

## 📋 Vue d'Ensemble

Ce répertoire contient tous les tests pour le projet Auto-Update GitHub, incluant :

- Tests unitaires
- Tests d'intégration
- Tests de validation
- Tests de configuration

## 🏗️ Structure des Tests

```
📁 tests/
├── 📄 __init__.py              # Module de tests
├── 📄 test_generate_report.py  # Tests unitaires du script principal
├── 📄 test_config.py          # Configuration des tests
└── 📄 README.md               # Cette documentation
```

## 🚀 Lancement des Tests

### Tests Complets

```bash
# Lancer tous les tests
python scripts/run_tests.py

# Tests unitaires uniquement
python tests/test_generate_report.py

# Tests de validation
python scripts/validate_project.py

# Tests locaux
python scripts/test_local.py
```

### Tests Spécifiques

```bash
# Test d'une fonction spécifique
python -m unittest tests.test_generate_report.TestGenerateReport.test_get_current_time_info

# Test avec verbose
python -m unittest -v tests.test_generate_report

# Test avec couverture
python -m coverage run -m unittest tests.test_generate_report
python -m coverage report
```

## 🔧 Configuration des Tests

### Variables d'Environnement

```bash
# Mode test
export TEST_MODE=true

# Répertoire de test
export TEST_DATA_DIR=test_data

# APIs de test
export MOCK_API_RESPONSES=true
```

### Configuration Python

```python
# tests/test_config.py
TEST_CONFIG = {
    'test_data_dir': 'test_data',
    'mock_api_responses': True,
    'test_timezone': 'UTC'
}
```

## 📊 Types de Tests

### 1. Tests Unitaires

**Fichier** : `test_generate_report.py`

**Fonctions testées** :

- `get_current_time_info()` : Informations temporelles
- `test_api_connection()` : Test d'API
- `load_update_history()` : Chargement historique
- `save_update_history()` : Sauvegarde historique
- `generate_report_content()` : Génération contenu

**Exemple** :

```python
def test_get_current_time_info(self):
    time_info = get_current_time_info()
    self.assertIsInstance(time_info, dict)
    self.assertIn('timestamp', time_info)
```

### 2. Tests d'Intégration

**Fichier** : `scripts/test_local.py`

**Fonctionnalités testées** :

- Imports des modules
- Exécution du script principal
- Création des fichiers
- Validation du contenu

### 3. Tests de Validation

**Fichier** : `scripts/validate_project.py`

**Éléments validés** :

- Structure des fichiers
- Configuration GitHub Actions
- Scripts Python
- Documentation
- Fichiers de données

### 4. Tests de Configuration

**Fichier** : `tests/test_config.py`

**Configuration testée** :

- Variables d'environnement
- Fichiers de configuration
- APIs de test
- Données de test

## 🐛 Débogage des Tests

### Problèmes Courants

#### 1. Import Errors

```python
# Solution : Ajouter le répertoire au PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent / 'scripts'))
```

#### 2. Fichiers de Test Manquants

```python
# Solution : Créer les répertoires de test
test_dir = Path('test_data')
test_dir.mkdir(exist_ok=True)
```

#### 3. APIs de Test Inaccessibles

```python
# Solution : Utiliser des mocks
if TEST_CONFIG['mock_api_responses']:
    return mock_api_response()
```

### Logs de Test

```python
import logging

# Configuration des logs
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_function():
    logger.debug("Début du test")
    # Votre test ici
    logger.debug("Fin du test")
```

## 📈 Métriques de Test

### Couverture de Code

```bash
# Installation de coverage
pip install coverage

# Lancement avec couverture
coverage run -m unittest tests.test_generate_report
coverage report
coverage html  # Génère un rapport HTML
```

### Performance des Tests

```python
import time

def test_performance():
    start_time = time.time()
    # Votre test ici
    end_time = time.time()
    print(f"Temps d'exécution: {end_time - start_time:.2f}s")
```

## 🔄 Tests Automatisés

### GitHub Actions

```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: python scripts/run_tests.py
```

### Tests Locaux

```bash
# Script de test automatique
#!/bin/bash
python scripts/run_tests.py
if [ $? -eq 0 ]; then
    echo "✅ Tests passés"
else
    echo "❌ Tests échoués"
    exit 1
fi
```

## 📚 Bonnes Pratiques

### 1. Isolation des Tests

```python
def setUp(self):
    """Configuration avant chaque test"""
    self.test_data_dir = Path('test_data')
    self.test_data_dir.mkdir(exist_ok=True)

def tearDown(self):
    """Nettoyage après chaque test"""
    if self.test_data_dir.exists():
        shutil.rmtree(self.test_data_dir)
```

### 2. Tests Déterministes

```python
def test_deterministic(self):
    """Test déterministe avec données fixes"""
    fixed_data = {'date': '2024-01-15', 'time': '09:00:00'}
    result = process_data(fixed_data)
    self.assertEqual(result, expected_result)
```

### 3. Tests de Performance

```python
def test_performance(self):
    """Test de performance"""
    start_time = time.time()
    result = expensive_operation()
    end_time = time.time()

    self.assertLess(end_time - start_time, 1.0)  # Moins d'1 seconde
    self.assertIsNotNone(result)
```

## 🎯 Objectifs de Test

### Couverture Cible

- **Tests unitaires** : 90%+ de couverture
- **Tests d'intégration** : Tous les workflows
- **Tests de validation** : Tous les composants
- **Tests de performance** : Temps d'exécution < 30s

### Critères de Qualité

- ✅ Tous les tests passent
- ✅ Couverture de code > 90%
- ✅ Temps d'exécution < 30s
- ✅ Pas de warnings
- ✅ Documentation à jour

---

**🎯 Objectif** : Maintenir une suite de tests robuste et complète pour garantir la qualité du projet Auto-Update GitHub.
