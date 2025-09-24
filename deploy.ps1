# Script de déploiement PowerShell pour le projet Auto-Update GitHub
# Usage: .\deploy.ps1

Write-Host "🚀 DÉPLOIEMENT DU PROJET AUTO-UPDATE GITHUB" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green

# Vérification des prérequis
Write-Host "`n🔍 Vérification des prérequis..." -ForegroundColor Yellow

# Vérifier Git
try {
    $gitVersion = git --version
    Write-Host "✅ Git installé: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git n'est pas installé" -ForegroundColor Red
    exit 1
}

# Vérifier Python
try {
    $pythonVersion = python --version
    Write-Host "✅ Python installé: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python n'est pas installé" -ForegroundColor Red
    exit 1
}

# Vérifier pip
try {
    $pipVersion = pip --version
    Write-Host "✅ pip installé: $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ pip n'est pas installé" -ForegroundColor Red
    exit 1
}

# Installation des dépendances
Write-Host "`n📦 Installation des dépendances..." -ForegroundColor Yellow
pip install -r requirements.txt
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Dépendances installées" -ForegroundColor Green
} else {
    Write-Host "❌ Erreur installation dépendances" -ForegroundColor Red
    exit 1
}

# Validation du projet
Write-Host "`n🧪 Validation du projet..." -ForegroundColor Yellow
python scripts/validate_project.py
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Projet validé" -ForegroundColor Green
} else {
    Write-Host "❌ Projet invalide - Vérifiez les erreurs" -ForegroundColor Red
    exit 1
}

# Test local
Write-Host "`n🔬 Test local du script..." -ForegroundColor Yellow
python scripts/test_local.py
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Tests locaux passés" -ForegroundColor Green
} else {
    Write-Host "❌ Tests locaux échoués" -ForegroundColor Red
    exit 1
}

# Configuration Git
Write-Host "`n⚙️  Configuration Git..." -ForegroundColor Yellow
git config user.name "Auto-Update Bot" 2>$null
git config user.email "action@github.com" 2>$null
Write-Host "✅ Git configuré" -ForegroundColor Green

# Ajout des fichiers
Write-Host "`n📁 Ajout des fichiers..." -ForegroundColor Yellow
git add .
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Fichiers ajoutés" -ForegroundColor Green
} else {
    Write-Host "❌ Erreur ajout fichiers" -ForegroundColor Red
    exit 1
}

# Commit initial
Write-Host "`n💾 Commit initial..." -ForegroundColor Yellow
$commitMessage = @"
🤖 Initial commit: Auto-update GitHub project

- Workflow GitHub Actions configuré
- Script Python de génération de rapport
- Documentation complète
- Tests et validation inclus
- Configuration pour mise à jour quotidienne à 9h UTC
"@

git commit -m $commitMessage
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Commit créé" -ForegroundColor Green
} else {
    Write-Host "❌ Erreur commit" -ForegroundColor Red
    exit 1
}

# Instructions finales
Write-Host "`n🎉 DÉPLOIEMENT TERMINÉ !" -ForegroundColor Green
Write-Host "========================" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Prochaines étapes:" -ForegroundColor Cyan
Write-Host "1. Créer un repository sur GitHub" -ForegroundColor White
Write-Host "2. Ajouter le remote: git remote add origin <votre-repo-url>" -ForegroundColor White
Write-Host "3. Pusher: git push -u origin main" -ForegroundColor White
Write-Host "4. Aller dans Settings > Actions > General" -ForegroundColor White
Write-Host "5. Activer 'Read and write permissions'" -ForegroundColor White
Write-Host "6. Activer 'Allow GitHub Actions to create and approve pull requests'" -ForegroundColor White
Write-Host "7. Tester manuellement dans l'onglet Actions" -ForegroundColor White
Write-Host ""
Write-Host "🔧 Configuration optionnelle:" -ForegroundColor Cyan
Write-Host "- Modifier l'horaire dans .github/workflows/auto-update.yml" -ForegroundColor White
Write-Host "- Personnaliser le contenu dans scripts/generate_report.py" -ForegroundColor White
Write-Host "- Ajouter des APIs dans le script" -ForegroundColor White
Write-Host ""
Write-Host "📚 Documentation:" -ForegroundColor Cyan
Write-Host "- README.md: Documentation complète" -ForegroundColor White
Write-Host "- scripts/demo.py: Démonstration des fonctionnalités" -ForegroundColor White
Write-Host "- scripts/validate_project.py: Validation du projet" -ForegroundColor White
Write-Host ""
Write-Host "🎯 Le projet sera exécuté automatiquement tous les jours à 9h UTC !" -ForegroundColor Green
