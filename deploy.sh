#!/bin/bash

# Script de déploiement pour le projet Auto-Update GitHub
# Usage: ./deploy.sh

echo "🚀 DÉPLOIEMENT DU PROJET AUTO-UPDATE GITHUB"
echo "=========================================="

# Vérification des prérequis
echo "🔍 Vérification des prérequis..."

# Vérifier Git
if ! command -v git &> /dev/null; then
    echo "❌ Git n'est pas installé"
    exit 1
fi
echo "✅ Git installé"

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 n'est pas installé"
    exit 1
fi
echo "✅ Python3 installé"

# Vérifier pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 n'est pas installé"
    exit 1
fi
echo "✅ pip3 installé"

# Installation des dépendances
echo ""
echo "📦 Installation des dépendances..."
pip3 install -r requirements.txt
if [ $? -eq 0 ]; then
    echo "✅ Dépendances installées"
else
    echo "❌ Erreur installation dépendances"
    exit 1
fi

# Validation du projet
echo ""
echo "🧪 Validation du projet..."
python3 scripts/validate_project.py
if [ $? -eq 0 ]; then
    echo "✅ Projet validé"
else
    echo "❌ Projet invalide - Vérifiez les erreurs"
    exit 1
fi

# Test local
echo ""
echo "🔬 Test local du script..."
python3 scripts/test_local.py
if [ $? -eq 0 ]; then
    echo "✅ Tests locaux passés"
else
    echo "❌ Tests locaux échoués"
    exit 1
fi

# Configuration Git
echo ""
echo "⚙️  Configuration Git..."
git config user.name "Auto-Update Bot" 2>/dev/null || true
git config user.email "action@github.com" 2>/dev/null || true
echo "✅ Git configuré"

# Ajout des fichiers
echo ""
echo "📁 Ajout des fichiers..."
git add .
if [ $? -eq 0 ]; then
    echo "✅ Fichiers ajoutés"
else
    echo "❌ Erreur ajout fichiers"
    exit 1
fi

# Commit initial
echo ""
echo "💾 Commit initial..."
git commit -m "🤖 Initial commit: Auto-update GitHub project

- Workflow GitHub Actions configuré
- Script Python de génération de rapport
- Documentation complète
- Tests et validation inclus
- Configuration pour mise à jour quotidienne à 9h UTC"
if [ $? -eq 0 ]; then
    echo "✅ Commit créé"
else
    echo "❌ Erreur commit"
    exit 1
fi

# Instructions finales
echo ""
echo "🎉 DÉPLOIEMENT TERMINÉ !"
echo "========================"
echo ""
echo "📋 Prochaines étapes:"
echo "1. Créer un repository sur GitHub"
echo "2. Ajouter le remote: git remote add origin <votre-repo-url>"
echo "3. Pusher: git push -u origin main"
echo "4. Aller dans Settings > Actions > General"
echo "5. Activer 'Read and write permissions'"
echo "6. Activer 'Allow GitHub Actions to create and approve pull requests'"
echo "7. Tester manuellement dans l'onglet Actions"
echo ""
echo "🔧 Configuration optionnelle:"
echo "- Modifier l'horaire dans .github/workflows/auto-update.yml"
echo "- Personnaliser le contenu dans scripts/generate_report.py"
echo "- Ajouter des APIs dans le script"
echo ""
echo "📚 Documentation:"
echo "- README.md: Documentation complète"
echo "- scripts/demo.py: Démonstration des fonctionnalités"
echo "- scripts/validate_project.py: Validation du projet"
echo ""
echo "🎯 Le projet sera exécuté automatiquement tous les jours à 9h UTC !"
