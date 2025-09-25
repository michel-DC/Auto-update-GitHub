# 🤖 Auto-Update GitHub Project

> **Projet automatisé de mise à jour quotidienne de documents sur GitHub**

Ce projet utilise **GitHub Actions** pour mettre à jour automatiquement un fichier Markdown 4 fois par jour (6h, 12h, 18h, 0h UTC). Il démontre comment automatiser la génération et la publication de contenu sur GitHub.

## 📋 Fonctionnalités

- ✅ **Mise à jour automatique 4 fois par jour** via GitHub Actions
- ✅ **Génération de contenu dynamique** avec données en temps réel
- ✅ **Historique des mises à jour** sauvegardé
- ✅ **Test de connectivité API** intégré
- ✅ **Statistiques temporelles** calculées automatiquement
- ✅ **Déclenchement manuel** possible

## 🏗️ Architecture du Projet

```
📁 Projet/
├── 📁 .github/
│   └── 📁 workflows/
│       └── 📄 auto-update.yml          # Workflow GitHub Actions
├── 📁 scripts/
│   └── 📄 generate_report.py           # Script de génération Python
├── 📁 data/
│   └── 📄 update_history.json          # Historique des mises à jour
├── 📄 daily-report.md                  # Document mis à jour automatiquement
├── 📄 README.md                        # Cette documentation
└── 📄 .gitignore                       # Fichiers à ignorer
```

## 🚀 Installation et Configuration

### 1. Cloner le Repository

```bash
git clone <votre-repo-url>
cd auto-update-github-project
```

### 2. Configuration GitHub Actions

Le workflow est déjà configuré dans `.github/workflows/auto-update.yml`. Il s'exécute :

- **Automatiquement** : 4 fois par jour (6h, 12h, 18h, 0h UTC)
- **Manuellement** : Via l'onglet "Actions" de GitHub

### 3. Permissions Requises

Le repository doit avoir les permissions suivantes :

- ✅ **Actions** : Activées
- ✅ **Workflow permissions** : "Read and write permissions"
- ✅ **Allow GitHub Actions to create and approve pull requests** : Activé

## ⚙️ Configuration Avancée

### Modifier l'Horaire d'Exécution

Éditez le fichier `.github/workflows/auto-update.yml` :

```yaml
schedule:
  - cron: "0 6 * * *" # 6h00 UTC
  - cron: "0 12 * * *" # 12h00 UTC
  - cron: "0 18 * * *" # 18h00 UTC
  - cron: "0 0 * * *" # 0h00 UTC (minuit)
```

**Exemples de cron :**

- `'0 6 * * *'` : 6h00 UTC tous les jours
- `'0 12 * * *'` : 12h00 UTC tous les jours
- `'0 18 * * *'` : 18h00 UTC tous les jours
- `'0 0 * * *'` : 0h00 UTC tous les jours (minuit)

### Personnaliser le Contenu

Modifiez le script `scripts/generate_report.py` pour :

- Ajouter de nouvelles données
- Intégrer d'autres APIs
- Modifier le format du rapport
- Ajouter des calculs personnalisés

### Ajouter des Variables d'Environnement

Dans `.github/workflows/auto-update.yml` :

```yaml
- name: Generate daily report
  run: |
    python scripts/generate_report.py
  env:
    API_KEY: ${{ secrets.MY_API_KEY }}
    CUSTOM_VAR: "valeur"
```

## 📊 Contenu Généré

Le script génère automatiquement :

### Informations Temporelles

- Date et heure actuelles
- Timestamp Unix
- Jour de la semaine
- Numéro du jour dans l'année
- Statistiques calculées

### Données Externes

- Test de connectivité API
- Temps de réponse
- Statut des services

### Historique

- Journal des mises à jour
- Statistiques du projet
- Métadonnées d'exécution

## 🔧 Développement Local

### Prérequis

- Python 3.11+
- pip

### Installation des Dépendances

```bash
pip install requests python-dateutil
```

### Test Local

```bash
python scripts/generate_report.py
```

### Structure des Données

Le fichier `data/update_history.json` contient :

```json
[
  {
    "date": "2024-01-15",
    "time": "09:00:00",
    "status": "success",
    "details": "Rapport généré avec succès - API: success"
  }
]
```

## 🐛 Dépannage

### Problèmes Courants

#### 1. Workflow ne s'exécute pas

- ✅ Vérifier que les Actions sont activées
- ✅ Vérifier les permissions du repository
- ✅ Vérifier la syntaxe du cron

#### 2. Erreur de permissions

- ✅ Aller dans Settings > Actions > General
- ✅ Sélectionner "Read and write permissions"
- ✅ Activer "Allow GitHub Actions to create and approve pull requests"

#### 3. Script Python échoue

- ✅ Vérifier les dépendances dans le workflow
- ✅ Tester le script localement
- ✅ Vérifier les logs dans l'onglet Actions

### Logs et Monitoring

1. **Voir les logs** : Repository > Actions > "Auto Update Daily Report"
2. **Statut des exécutions** : Onglet "Actions" de GitHub
3. **Historique des commits** : Onglet "Commits" du repository

## 📈 Personnalisation Avancée

### Ajouter des APIs Externes

```python
def fetch_weather_data():
    """Récupère les données météo"""
    try:
        response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Paris&appid=YOUR_API_KEY')
        return response.json()
    except Exception as e:
        return {'error': str(e)}
```

### Intégrer des Bases de Données

```python
import sqlite3

def get_database_stats():
    """Récupère les statistiques de la base de données"""
    conn = sqlite3.connect('data/app.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]
    conn.close()
    return count
```

### Ajouter des Notifications

```yaml
- name: Send notification
  if: failure()
  uses: 8398a7/action-slack@v3
  with:
    status: failure
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

## 📚 Ressources Utiles

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Cron Expression Guide](https://crontab.guru/)
- [Python Requests Library](https://requests.readthedocs.io/)
- [Markdown Guide](https://www.markdownguide.org/)

## 🤝 Contribution

1. Fork le repository
2. Créer une branche feature (`git checkout -b feature/amazing-feature`)
3. Commit les changements (`git commit -m 'Add amazing feature'`)
4. Push vers la branche (`git push origin feature/amazing-feature`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🆘 Support

Si vous rencontrez des problèmes :

1. 📖 Consultez cette documentation
2. 🔍 Vérifiez les [Issues](https://github.com/votre-username/auto-update-github-project/issues)
3. 💬 Ouvrez une nouvelle issue avec :
   - Description du problème
   - Logs d'erreur
   - Configuration utilisée

---

**🎉 Félicitations !** Votre projet d'auto-mise à jour est maintenant configuré et prêt à fonctionner automatiquement !

_Dernière mise à jour de cette documentation : $(date)_
