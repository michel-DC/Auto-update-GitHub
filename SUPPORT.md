# 🆘 Guide de Support

> **Guide de support pour le projet Auto-Update GitHub**

## 📋 Table des Matières

- [Obtenir de l'Aide](#obtenir-de-laide)
- [Questions Fréquentes](#questions-fréquentes)
- [Résolution de Problèmes](#résolution-de-problèmes)
- [Contact](#contact)
- [Ressources](#ressources)

## 🆘 Obtenir de l'Aide

### Niveaux de Support

#### 🟢 Niveau 1 : Auto-Assistance

- **Documentation** : README.md, DEVELOPER.md
- **FAQ** : Questions fréquentes
- **Recherche** : Issues GitHub existantes
- **Temps de réponse** : Immédiat

#### 🟡 Niveau 2 : Communauté

- **Issues GitHub** : Pour les bugs et fonctionnalités
- **Discussions** : Pour les questions générales
- **Temps de réponse** : 24-48h

#### 🔴 Niveau 3 : Support Direct

- **Email** : Pour les problèmes critiques
- **Temps de réponse** : 48h maximum

## ❓ Questions Fréquentes

### 🔧 Configuration

**Q : Le workflow ne s'exécute pas automatiquement**
A : Vérifiez que :

- Les Actions sont activées dans Settings > Actions
- Les permissions sont configurées (Read and write)
- L'expression cron est correcte
- Le repository est public ou a des Actions activées

**Q : Erreur de permissions lors du push**
A : Vérifiez que :

- Le token GITHUB_TOKEN a les bonnes permissions
- Le workflow a la permission `contents: write`
- Le repository permet les Actions

**Q : Le script Python échoue**
A : Vérifiez que :

- Python 3.11+ est installé
- Les dépendances sont installées (`pip install -r requirements.txt`)
- Le script fonctionne localement

### 🐛 Problèmes Courants

**Q : Fichiers non mis à jour**
A : Vérifiez que :

- Le workflow s'exécute sans erreur
- Les logs dans l'onglet Actions
- Le script génère du contenu
- Les permissions Git sont correctes

**Q : APIs inaccessibles**
A : Vérifiez que :

- L'URL de l'API est correcte
- L'API est accessible depuis GitHub Actions
- Le timeout est suffisant
- Aucun firewall ne bloque l'accès

**Q : Historique non sauvegardé**
A : Vérifiez que :

- Le fichier `data/update_history.json` existe
- Les permissions d'écriture sont correctes
- Le script a accès au répertoire `data/`

## 🔧 Résolution de Problèmes

### Diagnostic Automatique

```bash
# Lancer le diagnostic complet
python scripts/validate_project.py

# Tests locaux
python scripts/test_local.py

# Test du script principal
python scripts/generate_report.py
```

### Vérifications Manuelles

#### 1. Vérifier la Configuration

```bash
# Vérifier la structure des fichiers
ls -la .github/workflows/
ls -la scripts/
ls -la data/

# Vérifier les permissions
ls -la daily-report.md
ls -la data/update_history.json
```

#### 2. Vérifier les Logs

```bash
# Voir les logs GitHub Actions
# Aller dans Repository > Actions > "Auto Update Daily Report"
# Cliquer sur la dernière exécution
# Voir les logs de chaque étape
```

#### 3. Tester Localement

```bash
# Installer les dépendances
pip install -r requirements.txt

# Tester le script
python scripts/generate_report.py

# Vérifier les fichiers générés
cat daily-report.md
cat data/update_history.json
```

### Solutions par Problème

#### Workflow ne s'exécute pas

```yaml
# Vérifier la syntaxe cron
schedule:
  - cron: "0 9 * * *" # 9h00 UTC tous les jours

# Vérifier les permissions
permissions:
  contents: write
```

#### Erreur de permissions

```bash
# Vérifier les settings GitHub
# Settings > Actions > General
# "Read and write permissions" : Activé
# "Allow GitHub Actions to create and approve pull requests" : Activé
```

#### Script Python échoue

```python
# Ajouter des logs de debug
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    logger.info("Début de l'exécution")
    # Votre code ici
    logger.info("Fin de l'exécution")
```

## 📞 Contact

### 🐛 Signaler un Bug

1. **Vérifier** que le bug n'existe pas déjà dans les Issues
2. **Créer** une nouvelle issue avec le template
3. **Inclure** :
   - Description du problème
   - Étapes pour reproduire
   - Logs d'erreur
   - Environnement (OS, Python, version)

### 💡 Proposer une Fonctionnalité

1. **Vérifier** que la fonctionnalité n'existe pas déjà
2. **Créer** une nouvelle issue avec le template
3. **Inclure** :
   - Description de la fonctionnalité
   - Cas d'usage
   - Impact sur les utilisateurs
   - Alternatives considérées

### 📧 Support Direct

- **Email** : support@example.com
- **Response Time** : 48h maximum
- **Urgence** : Pour les problèmes critiques uniquement

### 💬 Discussions Communautaires

- **GitHub Discussions** : Pour les questions générales
- **Issues** : Pour les bugs et fonctionnalités
- **Pull Requests** : Pour les contributions

## 📚 Ressources

### Documentation

- **README.md** : Guide utilisateur principal
- **DEVELOPER.md** : Guide développeur
- **CONTRIBUTING.md** : Guide de contribution
- **SECURITY.md** : Politique de sécurité

### Scripts Utiles

- **scripts/validate_project.py** : Validation complète
- **scripts/test_local.py** : Tests locaux
- **scripts/demo.py** : Démonstration
- **scripts/setup_project.py** : Configuration

### Liens Externes

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python Documentation](https://docs.python.org/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Cron Expression Guide](https://crontab.guru/)

## 🎯 Niveaux de Priorité

### 🔴 Critique (Response: 24h)

- Workflow ne s'exécute pas
- Erreurs de sécurité
- Données corrompues
- Accès refusé

### 🟡 Important (Response: 48h)

- Fonctionnalités manquantes
- Performance dégradée
- Erreurs de configuration
- Documentation manquante

### 🟢 Normal (Response: 72h)

- Améliorations
- Questions générales
- Suggestions
- Feedback

## 📊 Métriques de Support

### Temps de Réponse

- **Issues** : 24-48h
- **Discussions** : 48-72h
- **Email** : 48h maximum
- **Pull Requests** : 72h maximum

### Taux de Résolution

- **Niveau 1** : 80% résolus par auto-assistance
- **Niveau 2** : 15% résolus par la communauté
- **Niveau 3** : 5% nécessitent un support direct

## 🔄 Processus de Support

### 1. Réception

- **Tri** : Classification par priorité
- **Assignation** : Attribution à un mainteneur
- **Acknowledgment** : Confirmation de réception

### 2. Investigation

- **Reproduction** : Reproduire le problème
- **Diagnostic** : Identifier la cause
- **Solution** : Développer un fix

### 3. Résolution

- **Test** : Valider la solution
- **Déploiement** : Mettre à jour le code
- **Communication** : Informer l'utilisateur

### 4. Suivi

- **Vérification** : Confirmer la résolution
- **Documentation** : Mettre à jour la doc
- **Amélioration** : Prévenir les récurrences

---

**🆘 Nous sommes là pour vous aider !**

N'hésitez pas à nous contacter si vous avez des questions ou des problèmes. Notre objectif est de vous aider à réussir avec le projet Auto-Update GitHub.
