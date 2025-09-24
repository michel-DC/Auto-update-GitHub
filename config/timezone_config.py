"""
Configuration des fuseaux horaires pour le projet
Permet de personnaliser l'heure d'exécution selon votre localisation
"""

# Fuseaux horaires supportés
TIMEZONES = {
    'UTC': 'UTC',
    'Europe/Paris': 'Europe/Paris',
    'America/New_York': 'America/New_York',
    'America/Los_Angeles': 'America/Los_Angeles',
    'Asia/Tokyo': 'Asia/Tokyo',
    'Australia/Sydney': 'Australia/Sydney'
}

# Configuration par défaut
DEFAULT_TIMEZONE = 'UTC'
DEFAULT_HOUR = 9  # Heure d'exécution (24h format)

# Correspondance des heures UTC vers les fuseaux locaux
# Format: 'fuseau_local': 'heure_UTC_correspondante'
TIMEZONE_OFFSETS = {
    'Europe/Paris': 1,      # UTC+1 (UTC+2 en été)
    'America/New_York': -5, # UTC-5 (UTC-4 en été)
    'America/Los_Angeles': -8, # UTC-8 (UTC-7 en été)
    'Asia/Tokyo': 9,        # UTC+9
    'Australia/Sydney': 10, # UTC+10 (UTC+11 en été)
}

def get_utc_hour_for_timezone(timezone, local_hour=9):
    """
    Calcule l'heure UTC correspondante pour un fuseau horaire donné
    
    Args:
        timezone (str): Fuseau horaire (ex: 'Europe/Paris')
        local_hour (int): Heure locale souhaitée (0-23)
    
    Returns:
        int: Heure UTC correspondante
    """
    if timezone not in TIMEZONE_OFFSETS:
        return local_hour  # Par défaut, pas de conversion
    
    offset = TIMEZONE_OFFSETS[timezone]
    utc_hour = local_hour - offset
    
    # Gérer le débordement des heures
    if utc_hour < 0:
        utc_hour += 24
    elif utc_hour >= 24:
        utc_hour -= 24
    
    return utc_hour

def get_cron_expression(timezone='UTC', local_hour=9):
    """
    Génère l'expression cron pour un fuseau horaire donné
    
    Args:
        timezone (str): Fuseau horaire
        local_hour (int): Heure locale souhaitée
    
    Returns:
        str: Expression cron (format: 'minute hour * * *')
    """
    utc_hour = get_utc_hour_for_timezone(timezone, local_hour)
    return f'0 {utc_hour} * * *'

# Exemples d'utilisation
if __name__ == "__main__":
    print("🌍 Configuration des fuseaux horaires")
    print("=" * 40)
    
    for tz in TIMEZONES:
        utc_hour = get_utc_hour_for_timezone(tz, 9)
        cron = get_cron_expression(tz, 9)
        print(f"{tz:20} | 9h locale = {utc_hour:2d}h UTC | Cron: {cron}")
