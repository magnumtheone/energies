#!/usr/bin/env python
"""
Script de build pour Vercel
"""
import os
import shutil
import subprocess
import sys

def collect_static():
    """Collecte les fichiers statiques"""
    print("🔧 Collection des fichiers statiques...")
    
    # Chemin du projet Django
    django_dir = os.path.join("backend", "Bac", "myblog_project")
    
    # Aller dans le dossier Django
    os.chdir(django_dir)
    
    # Exécuter collectstatic
    try:
        subprocess.run([sys.executable, "manage.py", "collectstatic", "--noinput"], check=True)
        print("✅ Fichiers statiques collectés avec succès")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de la collecte des fichiers statiques: {e}")
        return False
    
    return True

def setup_database():
    """Configure la base de données"""
    print("🔧 Configuration de la base de données...")
    
    try:
        subprocess.run([sys.executable, "manage.py", "migrate", "--noinput"], check=True)
        print("✅ Migrations appliquées avec succès")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors des migrations: {e}")
        return False
    
    return True

def main():
    """Fonction principale de build"""
    print("🚀 Début du build Vercel pour Masco...")
    
    # Collecte des fichiers statiques
    if not collect_static():
        sys.exit(1)
    
    # Configuration de la base de données
    if not setup_database():
        sys.exit(1)
    
    print("✅ Build Vercel terminé avec succès!")

if __name__ == "__main__":
    main()
