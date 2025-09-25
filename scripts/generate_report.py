#!/usr/bin/env python3
"""
Script de génération automatique du rapport quotidien
Ce script est exécuté par GitHub Actions pour mettre à jour daily-report.md
"""

import os
import sys
from datetime import datetime, timezone, timedelta
import requests
import json
from pathlib import Path

def get_current_time_info():
    """Récupère les informations temporelles actuelles"""
    now = datetime.now(timezone.utc)
    
    # Calcul du nombre de jours depuis le 1er janvier 2000
    epoch_2000 = datetime(2000, 1, 1, tzinfo=timezone.utc)
    days_since_2000 = (now - epoch_2000).days
    
    # Calcul des secondes écoulées aujourd'hui
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    seconds_today = (now - start_of_day).total_seconds()
    
    return {
        'datetime': now,
        'timestamp': int(now.timestamp()),
        'weekday': now.strftime('%A'),
        'day_of_year': now.timetuple().tm_yday,
        'days_since_2000': days_since_2000,
        'seconds_today': int(seconds_today)
    }

def test_api_connection():
    """Teste la connexion à une API publique (exemple)"""
    try:
        # Test avec une API publique gratuite
        response = requests.get('https://httpbin.org/json', timeout=10)
        return {
            'status': 'success' if response.status_code == 200 else 'error',
            'response_time': response.elapsed.total_seconds(),
            'status_code': response.status_code
        }
    except Exception as e:
        return {
            'status': 'error',
            'response_time': None,
            'error': str(e)
        }

def load_update_history():
    """Charge l'historique des mises à jour depuis un fichier JSON"""
    history_file = Path('data/update_history.json')
    
    if history_file.exists():
        try:
            with open(history_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_update_history(history):
    """Sauvegarde l'historique des mises à jour"""
    history_file = Path('data/update_history.json')
    history_file.parent.mkdir(exist_ok=True)
    
    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

def get_next_execution_time(current_time):
    """Calcule la prochaine heure d'exécution (6h, 12h, 18h, 0h)"""
    execution_hours = [6, 12, 18, 0]
    current_hour = current_time.hour
    
    # Trouver la prochaine heure d'exécution
    for hour in execution_hours:
        if hour > current_hour:
            return current_time.replace(hour=hour, minute=0, second=0, microsecond=0)
    
    # Si aucune heure trouvée aujourd'hui, prendre 6h demain
    next_day = current_time + timedelta(days=1)
    return next_day.replace(hour=6, minute=0, second=0, microsecond=0)

def get_execution_number():
    """Détermine le numéro d'exécution de la journée (1-4)"""
    now = datetime.now(timezone.utc)
    execution_hours = [6, 12, 18, 0]
    
    for i, hour in enumerate(execution_hours):
        if now.hour >= hour:
            return i + 1
    return 1

def generate_report_content(time_info, api_info):
    """Génère le contenu du rapport Markdown"""
    
    # Chargement de l'historique
    history = load_update_history()
    
    # Déterminer le numéro d'exécution
    exec_number = get_execution_number()
    
    # Ajout de la nouvelle entrée
    new_entry = {
        'date': time_info['datetime'].strftime('%Y-%m-%d'),
        'time': time_info['datetime'].strftime('%H:%M:%S'),
        'execution_number': exec_number,
        'status': 'success',
        'details': f"Rapport généré avec succès (Exécution #{exec_number}/4) - API: {api_info['status']}"
    }
    history.insert(0, new_entry)  # Ajouter au début
    
    # Limiter l'historique aux 20 dernières entrées (5 jours x 4 exécutions)
    history = history[:20]
    save_update_history(history)
    
    # Calcul de la prochaine exécution
    next_execution = get_next_execution_time(time_info['datetime'])
    
    # Génération du contenu Markdown
    content = f"""# 📊 Rapport Automatique Multi-Quotidien

> **Dernière mise à jour :** {time_info['datetime'].strftime('%Y-%m-%d %H:%M:%S')} UTC  
> **Exécution :** #{exec_number}/4 de la journée

## 📅 Informations Générales

- **Date :** {time_info['datetime'].strftime('%Y-%m-%d')}
- **Heure :** {time_info['datetime'].strftime('%H:%M:%S')} UTC
- **Exécution du jour :** {exec_number}/4
- **Statut :** ✅ Généré automatiquement

## 🌍 Données du Jour

### Informations Système
- **Timestamp Unix :** {time_info['timestamp']}
- **Jour de la semaine :** {time_info['weekday']}
- **Numéro du jour dans l'année :** {time_info['day_of_year']}

### Statistiques
- **Nombre de jours depuis le 1er janvier 2000 :** {time_info['days_since_2000']:,}
- **Nombre de secondes écoulées aujourd'hui :** {time_info['seconds_today']:,}

## 📈 Données Externes

### API Publique
- **Statut de l'API :** {'✅ Connecté' if api_info['status'] == 'success' else '❌ Erreur'}
- **Temps de réponse :** {f"{api_info['response_time']:.3f}s" if api_info['response_time'] else 'N/A'}
- **Code de statut :** {api_info.get('status_code', 'N/A')}

## 🔄 Historique des Mises à Jour

| Date | Heure | Exécution | Statut | Détails |
|------|-------|-----------|--------|---------|"""

    # Ajout de l'historique
    for entry in history:
        status_emoji = "✅" if entry['status'] == 'success' else "❌"
        exec_num = entry.get('execution_number', 'N/A')
        content += f"\n| {entry['date']} | {entry['time']} | #{exec_num}/4 | {status_emoji} | {entry['details']} |"

    content += f"""

## 📊 Statistiques du Projet

- **Total de mises à jour :** {len(history)}
- **Dernière exécution :** {time_info['datetime'].strftime('%Y-%m-%d %H:%M:%S')} UTC
- **Prochaine exécution :** {next_execution.strftime('%Y-%m-%d %H:%M:%S')} UTC
- **Fréquence :** 4 fois par jour (6h, 12h, 18h, 0h UTC)

---

*Ce document est mis à jour automatiquement 4 fois par jour via GitHub Actions.*
*Dernière génération : {time_info['datetime'].strftime('%Y-%m-%d %H:%M:%S')} UTC*
"""

    return content

def main():
    """Fonction principale"""
    print("🚀 Début de la génération du rapport quotidien...")
    
    try:
        # Récupération des informations temporelles
        print("📅 Récupération des informations temporelles...")
        time_info = get_current_time_info()
        
        # Test de l'API
        print("🌐 Test de connexion API...")
        api_info = test_api_connection()
        
        # Génération du contenu
        print("📝 Génération du contenu du rapport...")
        content = generate_report_content(time_info, api_info)
        
        # Écriture du fichier
        print("💾 Sauvegarde du rapport...")
        with open('daily-report.md', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Rapport généré avec succès !")
        print(f"📊 Fichier mis à jour : daily-report.md")
        print(f"🕐 Timestamp : {time_info['datetime'].strftime('%Y-%m-%d %H:%M:%S')} UTC")
        
    except Exception as e:
        print(f"❌ Erreur lors de la génération : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
