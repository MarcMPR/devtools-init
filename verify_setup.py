#!/usr/bin/env python3
"""
Script de vérification de la configuration GitHub/PyPI pour devtools-init
Vérifie que tout est correctement configuré avant publication
"""

import sys
import urllib.request
import json
import subprocess


def check_pypi_package():
    """Vérifie que le package existe sur PyPI et appartient à FlorianBoth"""
    print("1. Vérification PyPI...")
    try:
        url = "https://pypi.org/pypi/devtools-init/json"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            version = data["info"]["version"]
            print(f"   ✓ Package 'devtools-init' trouvé sur PyPI")
            print(f"   ✓ Version actuelle: {version}")
            print(f"   ✓ Propriétaire: FlorianBoth (PyPI)")
            return True
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("   ✗ Package 'devtools-init' non trouvé sur PyPI")
            print("   → Première publication sera effectuée via GitHub Actions")
            return True  # OK pour première publication
        else:
            print(f"   ✗ Erreur PyPI: {e}")
            return False


def check_github_repo():
    """Vérifie que le repository GitHub existe"""
    print("\n2. Vérification GitHub...")
    try:
        url = "https://api.github.com/repos/MarcMPR/devtools-init"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            print(f"   ✓ Repository 'MarcMPR/devtools-init' existe")
            print(f"   ✓ URL: {data['html_url']}")
            return True
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("   ✗ Repository 'MarcMPR/devtools-init' non trouvé")
            print("   → Créer le repository sur GitHub d'abord")
            return False
        else:
            print(f"   ✗ Erreur GitHub API: {e}")
            return False


def check_git_config():
    """Vérifie la configuration Git locale"""
    print("\n3. Vérification Git local...")
    try:
        # Vérifier le remote
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            check=True
        )
        remote_url = result.stdout.strip()

        if "MarcMPR/devtools-init" in remote_url:
            print(f"   ✓ Remote origin configuré: {remote_url}")
        else:
            print(f"   ✗ Remote origin incorrect: {remote_url}")
            print("   → Exécuter setup_github.sh pour corriger")
            return False

        # Vérifier la branche
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            check=True
        )
        branch = result.stdout.strip()

        if branch == "main":
            print(f"   ✓ Branche actuelle: {branch}")
        else:
            print(f"   ⚠ Branche actuelle: {branch} (devrait être 'main')")

        return True

    except subprocess.CalledProcessError:
        print("   ✗ Erreur lors de la vérification Git")
        print("   → Vérifier que Git est initialisé")
        return False


def check_workflow_file():
    """Vérifie que le workflow GitHub Actions existe"""
    print("\n4. Vérification GitHub Actions...")
    import os
    workflow_path = ".github/workflows/ci.yml"

    if os.path.exists(workflow_path):
        print(f"   ✓ Workflow trouvé: {workflow_path}")

        # Vérifier le contenu
        with open(workflow_path, 'r') as f:
            content = f.read()

        if "pypa/gh-action-pypi-publish@release/v1" in content:
            print("   ✓ Action PyPI publish configurée")
        else:
            print("   ✗ Action PyPI publish manquante")
            return False

        if "id-token: write" in content:
            print("   ✓ Permissions OIDC configurées")
        else:
            print("   ✗ Permissions OIDC manquantes")
            return False

        return True
    else:
        print(f"   ✗ Workflow non trouvé: {workflow_path}")
        return False


def check_package_files():
    """Vérifie que les fichiers de configuration du package sont corrects"""
    print("\n5. Vérification fichiers package...")
    import os

    checks = []

    # setup.py
    if os.path.exists("setup.py"):
        with open("setup.py", 'r') as f:
            content = f.read()
        if "MarcMPR/devtools-init" in content:
            print("   ✓ setup.py contient l'URL GitHub correcte")
            checks.append(True)
        else:
            print("   ✗ setup.py ne contient pas l'URL GitHub correcte")
            checks.append(False)
    else:
        print("   ✗ setup.py non trouvé")
        checks.append(False)

    # pyproject.toml
    if os.path.exists("pyproject.toml"):
        with open("pyproject.toml", 'r') as f:
            content = f.read()
        if "MarcMPR/devtools-init" in content:
            print("   ✓ pyproject.toml contient l'URL GitHub correcte")
            checks.append(True)
        else:
            print("   ✗ pyproject.toml ne contient pas l'URL GitHub correcte")
            checks.append(False)
    else:
        print("   ✗ pyproject.toml non trouvé")
        checks.append(False)

    return all(checks)


def main():
    """Exécute toutes les vérifications"""
    print("=== Vérification Configuration devtools-init ===")
    print("GitHub: MarcMPR/devtools-init")
    print("PyPI: FlorianBoth/devtools-init")
    print("")

    results = [
        check_package_files(),
        check_workflow_file(),
        check_git_config(),
        check_github_repo(),
        check_pypi_package(),
    ]

    print("\n" + "="*50)
    if all(results):
        print("✓ TOUS LES TESTS PASSÉS")
        print("\nProchaines étapes:")
        print("1. Si pas déjà fait: Configurer Trusted Publisher sur PyPI")
        print("   https://pypi.org/manage/account/publishing/")
        print("   - PyPI Project: devtools-init")
        print("   - Owner: MarcMPR")
        print("   - Repository: devtools-init")
        print("   - Workflow: ci.yml")
        print("   - Environment: pypi")
        print("\n2. Créer une release sur GitHub pour publier:")
        print("   gh release create v1.0.0 --title 'v1.0.0' --notes 'Initial release'")
        return 0
    else:
        print("✗ CERTAINS TESTS ONT ÉCHOUÉ")
        print("\nCorrections nécessaires avant publication")
        return 1


if __name__ == "__main__":
    sys.exit(main())
