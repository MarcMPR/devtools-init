#!/bin/bash

# Configuration automatique du repository GitHub pour devtools-init
# GitHub: MarcMPR/devtools-init
# PyPI: FlorianBoth/devtools-init

set -e

echo "=== Configuration GitHub pour devtools-init ==="
echo ""

# Vérifier si on est dans le bon répertoire
if [ ! -f "setup.py" ] || [ ! -f "pyproject.toml" ]; then
    echo "Erreur: Ce script doit être exécuté depuis PC2/devtools-init/"
    exit 1
fi

# Configuration du remote GitHub
GITHUB_REPO="https://github.com/MarcMPR/devtools-init.git"

echo "1. Configuration du remote GitHub..."
if git remote get-url origin &>/dev/null; then
    echo "   Remote 'origin' existe déjà, mise à jour..."
    git remote set-url origin "$GITHUB_REPO"
else
    echo "   Ajout du remote 'origin'..."
    git remote add origin "$GITHUB_REPO"
fi

# Vérifier la branche actuelle
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo "2. Création/passage à la branche main..."
    git checkout -B main
else
    echo "2. Déjà sur la branche main"
fi

# Afficher le statut
echo ""
echo "3. Statut du repository:"
git status --short

# Push vers GitHub
echo ""
read -p "Push vers GitHub? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "4. Push vers GitHub..."
    git push -u origin main
    echo ""
    echo "✓ Configuration terminée!"
    echo ""
    echo "Prochaines étapes:"
    echo "1. Aller sur https://pypi.org/manage/account/publishing/"
    echo "2. Configurer Trusted Publisher:"
    echo "   - PyPI Project Name: devtools-init"
    echo "   - Owner: MarcMPR"
    echo "   - Repository: devtools-init"
    echo "   - Workflow: ci.yml"
    echo "   - Environment: pypi"
    echo "3. Créer une release sur GitHub pour déclencher la publication"
else
    echo "Push annulé. Configuration du remote terminée."
fi
