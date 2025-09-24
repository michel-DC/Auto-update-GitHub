# 🤝 Guide de Contribution

> **Comment contribuer au projet Auto-Update GitHub**

## 📋 Table des Matières

- [Code de Conduite](#code-de-conduite)
- [Processus de Contribution](#processus-de-contribution)
- [Standards de Code](#standards-de-code)
- [Tests](#tests)
- [Documentation](#documentation)
- [Déploiement](#déploiement)

## 📜 Code de Conduite

### Nos Engagements

Nous nous engageons à créer un environnement accueillant et inclusif pour tous les contributeurs, peu importe :

- L'âge, la taille, le handicap, l'ethnicité
- L'identité et l'expression de genre
- Le niveau d'expérience, la nationalité
- L'apparence personnelle, la race, la religion
- L'identité et l'orientation sexuelles

### Comportements Acceptables

- Utiliser un langage accueillant et inclusif
- Respecter les différents points de vue et expériences
- Accepter gracieusement les critiques constructives
- Se concentrer sur ce qui est le mieux pour la communauté
- Faire preuve d'empathie envers les autres membres

### Comportements Inacceptables

- L'utilisation de langage ou d'images sexualisés
- Le trolling, les commentaires insultants ou désobligeants
- Le harcèlement public ou privé
- La publication d'informations privées sans permission
- Toute conduite inappropriée dans un contexte professionnel

## 🚀 Processus de Contribution

### 1. Fork et Clone

```bash
# Fork le repository sur GitHub
# Puis cloner votre fork
git clone https://github.com/votre-username/auto-update-github-project.git
cd auto-update-github-project

# Ajouter le repository original comme remote
git remote add upstream https://github.com/original-username/auto-update-github-project.git
```

### 2. Configuration de l'Environnement

```bash
# Installer les dépendances
pip install -r requirements.txt

# Installer les dépendances de développement
pip install -r requirements-dev.txt

# Configurer le projet
python scripts/setup_project.py

# Lancer les tests
python scripts/run_tests.py
```

### 3. Créer une Branche

```bash
# Créer une branche pour votre fonctionnalité
git checkout -b feature/nom-de-votre-fonctionnalite

# Ou pour une correction de bug
git checkout -b fix/description-du-bug
```

### 4. Développement

- **Écrire du code** selon les standards du projet
- **Ajouter des tests** pour les nouvelles fonctionnalités
- **Mettre à jour la documentation** si nécessaire
- **Vérifier** que tous les tests passent

### 5. Tests et Validation

```bash
# Tests unitaires
python tests/test_generate_report.py

# Tests d'intégration
python scripts/test_local.py

# Validation complète
python scripts/validate_project.py

# Tests de performance
python scripts/run_tests.py
```

### 6. Commit et Push

```bash
# Ajouter les fichiers modifiés
git add .

# Commit avec un message descriptif
git commit -m "feat: ajouter nouvelle fonctionnalité X

- Description détaillée des changements
- Impact sur les utilisateurs
- Références aux issues si applicable"

# Push vers votre fork
git push origin feature/nom-de-votre-fonctionnalite
```

### 7. Pull Request

1. **Aller** sur GitHub et créer une Pull Request
2. **Remplir** le template de PR
3. **Attendre** la review des maintainers
4. **Appliquer** les suggestions si nécessaire
5. **Merger** après approbation

## 📝 Standards de Code

### Python

```python
# Utiliser des docstrings
def ma_fonction(param1: str, param2: int) -> bool:
    """
    Description de la fonction.

    Args:
        param1: Description du paramètre
        param2: Description du paramètre

    Returns:
        Description de la valeur de retour

    Raises:
        ValueError: Quand param1 est vide
    """
    # Implémentation
    pass
```

### Git

```bash
# Messages de commit selon Conventional Commits
feat: nouvelle fonctionnalité
fix: correction de bug
docs: mise à jour documentation
style: formatage, point-virgules manquants
refactor: refactoring du code
test: ajout de tests
chore: tâches de maintenance
```

### Structure des Fichiers

```
📁 scripts/
├── 📄 generate_report.py      # Script principal
├── 📄 test_local.py          # Tests locaux
├── 📄 validate_project.py    # Validation
└── 📄 setup_project.py       # Configuration

📁 tests/
├── 📄 test_generate_report.py # Tests unitaires
├── 📄 test_config.py         # Configuration tests
└── 📄 README.md              # Documentation tests
```

## 🧪 Tests

### Types de Tests

1. **Tests Unitaires** : Fonctions individuelles
2. **Tests d'Intégration** : Workflow complet
3. **Tests de Validation** : Structure du projet
4. **Tests de Performance** : Temps d'exécution

### Écrire des Tests

```python
import unittest
from scripts.generate_report import ma_fonction

class TestMaFonction(unittest.TestCase):
    def test_cas_normal(self):
        """Test du cas normal"""
        result = ma_fonction("test", 42)
        self.assertEqual(result, True)

    def test_cas_erreur(self):
        """Test du cas d'erreur"""
        with self.assertRaises(ValueError):
            ma_fonction("", 42)
```

### Lancer les Tests

```bash
# Tests unitaires
python -m unittest tests.test_generate_report

# Tests avec couverture
coverage run -m unittest tests.test_generate_report
coverage report

# Tests de performance
python scripts/run_tests.py
```

## 📚 Documentation

### Mise à Jour de la Documentation

- **README.md** : Guide utilisateur
- **DEVELOPER.md** : Guide développeur
- **CHANGELOG.md** : Historique des versions
- **Docstrings** : Documentation du code

### Format de Documentation

````markdown
# Titre Principal

> Description courte du projet

## Fonctionnalités

- ✅ Fonctionnalité 1
- ✅ Fonctionnalité 2

## Installation

```bash
# Commandes d'installation
```
````

## Utilisation

```python
# Exemples de code
```

````

## 🚀 Déploiement

### Processus de Déploiement

1. **Validation** : Tous les tests passent
2. **Review** : Code review par les maintainers
3. **Merge** : Merge dans la branche principale
4. **Release** : Création d'une release
5. **Déploiement** : Mise à jour automatique

### Création d'une Release

```bash
# Mise à jour du numéro de version
# Mise à jour du CHANGELOG.md
# Création d'un tag
git tag -a v1.1.0 -m "Release version 1.1.0"
git push origin v1.1.0
````

## 🐛 Signaler un Bug

### Template de Bug Report

```markdown
## Description

Description claire du problème

## Étapes pour Reproduire

1. Aller à '...'
2. Cliquer sur '...'
3. Voir l'erreur

## Comportement Attendu

Description du comportement attendu

## Comportement Actuel

Description du comportement actuel

## Environnement

- OS: [ex: Windows 10]
- Python: [ex: 3.11.0]
- Version: [ex: 1.0.0]

## Logs
```

Logs d'erreur si disponibles

```

```

## 💡 Proposer une Fonctionnalité

### Template de Feature Request

```markdown
## Description

Description claire de la fonctionnalité

## Problème Résolu

Description du problème que cette fonctionnalité résout

## Solution Proposée

Description de la solution proposée

## Alternatives

Description des alternatives considérées

## Contexte Additionnel

Tout autre contexte sur la fonctionnalité
```

## 📞 Support

### Obtenir de l'Aide

- **Issues GitHub** : Pour les bugs et fonctionnalités
- **Discussions** : Pour les questions générales
- **Email** : Pour les questions privées
- **Documentation** : README.md et DEVELOPER.md

### Ressources

- [Documentation Python](https://docs.python.org/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)

## 🎯 Roadmap

### Version 1.1.0

- [ ] Support de multiples APIs
- [ ] Notifications par email
- [ ] Interface web de configuration

### Version 1.2.0

- [ ] Support des bases de données
- [ ] Templates personnalisables
- [ ] Métriques avancées

### Version 2.0.0

- [ ] Interface graphique
- [ ] Support multi-repositories
- [ ] Intégration avec d'autres services

---

**🎉 Merci de contribuer au projet Auto-Update GitHub !**

Votre contribution aide à améliorer l'automatisation de la mise à jour de documents sur GitHub.
