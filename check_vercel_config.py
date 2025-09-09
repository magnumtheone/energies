#!/usr/bin/env python
"""
Test de la configuration Vercel pour Masco
"""
import os
import sys
import json

def check_file_exists(filepath, description):
    """Vérifie si un fichier existe"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} - MANQUANT")
        return False

def check_vercel_config():
    """Vérifie la configuration Vercel"""
    print("🔍 VÉRIFICATION DE LA CONFIGURATION VERCEL")
    print("=" * 50)
    
    all_good = True
    
    # Fichiers essentiels
    files_to_check = [
        ("vercel.json", "Configuration Vercel"),
        ("wsgi.py", "Point d'entrée WSGI"), 
        ("requirements.txt", "Dépendances Python"),
        ("manage.py", "Gestionnaire Django racine"),
        ("build.py", "Script de build"),
        ("backend/__init__.py", "Module backend"),
        ("backend/Bac/__init__.py", "Sous-module Bac"),
        ("VERCEL_DEPLOYMENT_GUIDE.md", "Guide de déploiement")
    ]
    
    for filepath, description in files_to_check:
        if not check_file_exists(filepath, description):
            all_good = False
    
    # Vérification du contenu vercel.json
    print("\n🔧 VÉRIFICATION DU CONTENU vercel.json:")
    if os.path.exists("vercel.json"):
        try:
            with open("vercel.json", "r") as f:
                config = json.load(f)
            print("✅ vercel.json - JSON valide")
            
            # Vérifications spécifiques
            if "builds" in config:
                print("✅ Section 'builds' présente")
            if "routes" in config:
                print("✅ Section 'routes' présente")
            if "env" in config:
                print("✅ Variables d'environnement configurées")
                
        except json.JSONDecodeError:
            print("❌ vercel.json - JSON INVALIDE")
            all_good = False
    
    # Vérification structure Django
    print("\n🏗️ VÉRIFICATION STRUCTURE DJANGO:")
    django_files = [
        "backend/Bac/myblog_project/manage.py",
        "backend/Bac/myblog_project/myblog_project/settings.py",
        "backend/Bac/myblog_project/myblog_project/wsgi.py",
        "backend/Bac/myblog_project/blog/models.py"
    ]
    
    for filepath in django_files:
        check_file_exists(filepath, f"Django - {os.path.basename(filepath)}")
    
    # Vérification assets
    print("\n🖼️ VÉRIFICATION DES ASSETS:")
    assets_dirs = [
        "backend/Bac/myblog_project/blog/static/blog/images",
        "backend/Bac/myblog_project/blog/static/blog/videos",
        "backend/Bac/myblog_project/blog/static/blog/css"
    ]
    
    for dirpath in assets_dirs:
        if os.path.exists(dirpath):
            count = len([f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))])
            print(f"✅ {dirpath}: {count} fichiers")
        else:
            print(f"❌ {dirpath}: DOSSIER MANQUANT")
            all_good = False
    
    # Image partenaire ajoutée
    partner_image = "backend/Bac/myblog_project/blog/static/blog/images/vice-ministere.jpg"
    if check_file_exists(partner_image, "Image Vice-Ministère"):
        print("✅ Nouveau partenaire ajouté avec succès")
    
    print("\n" + "=" * 50)
    if all_good:
        print("🎉 CONFIGURATION VERCEL PRÊTE !")
        print("\n📋 PROCHAINES ÉTAPES:")
        print("1. Repository Git pushé ✅")
        print("2. Aller sur vercel.com")
        print("3. Importer le repository 'energies'")
        print("4. Vercel détectera automatiquement la config")
        print("5. Cliquer sur 'Deploy'")
        print("\n🌐 Votre site Masco sera en ligne !")
    else:
        print("❌ CONFIGURATION INCOMPLÈTE")
        print("Veuillez corriger les erreurs avant de déployer")
    
    return all_good

if __name__ == "__main__":
    # Aller dans le bon répertoire
    if os.path.basename(os.getcwd()) != "Masco":
        masco_path = "d:/Maquettes/Masco"
        if os.path.exists(masco_path):
            os.chdir(masco_path)
        else:
            print("❌ Impossible de trouver le dossier Masco")
            sys.exit(1)
    
    success = check_vercel_config()
    sys.exit(0 if success else 1)
