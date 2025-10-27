# Auto-Update GitHub Project

Ce projet met à jour automatiquement un fichier Markdown (`daily-report.md`) 4 fois par jour grâce à un workflow GitHub Actions programmé dans `.github/workflows/auto-update.yml`. Il interroge des API listées dans `config/project_config.json`, logge chaque exécution dans `data/update_history.json`, et gère l’historique complet des mises à jour automatiques.

## Utilisation rapide

1. **Clonage**
   ```bash
   git clone https://github.com/michel-DC/Auto-update-GitHub.git
   cd auto-update-github-project
   ```
2. **Dépendances**
   - Requiert Python 3.11+
   - Installer avec :
     ```bash
     pip install requests python-dateutil
     ```
3. **Exécution locale**
   ```bash
   python scripts/generate_report.py
   ```
4. **Modification de l’horaire**
   - Tous les créneaux sont configurés via la clé `schedule` du fichier workflow (cron 6h, 12h, 18h, 0h UTC par défaut).

5. **Configuration**
   - Les endpoints API et les paramètres de projet se modifient depuis `config/project_config.json`.
   - Historique des exécutions : `data/update_history.json`.

## Fonctionnement technique

- Le script Python principal est `scripts/generate_report.py`
- Toute l’archive des exécutions (date, succès/échec, détail API) est centralisée dans `data/update_history.json`.
- Le rapport Markdown (`daily-report.md`) est écrasé lors de chaque exécution.
- Le workflow utilise la permission "write".
- Structure du projet :
  ```
  .github/workflows/auto-update.yml
  scripts/generate_report.py
  data/update_history.json
  daily-report.md
  config/project_config.json
  ```

## Questions fréquentes

- **Logs d’exécution** : visibles dans l’onglet Actions GitHub.
- **Configuration des API** : dans `config/project_config.json`.
- **Test local** : lancer le script Python, vérifiez la création/mise à jour de `daily-report.md` et l’historique dans `data/update_history.json`.
- **Dépannage** : consultez les logs Actions, vérifiez les dépendances Python, inspectez la validité du JSON de configuration.

## Licence

MIT — voir `LICENSE`.

Dernière mise à jour : voir log dans `data/update_history.json`.
