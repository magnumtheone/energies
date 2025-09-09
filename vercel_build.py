#!/usr/bin/env python3

import os
import sys
import django
from django.core.management import execute_from_command_line

def setup_django():
    """Configuration Django pour Vercel"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog_project.settings')
    os.environ.setdefault('VERCEL_ENV', 'production')
    
    # Ajouter les chemins nécessaires au PYTHONPATH
    base_dir = os.path.dirname(os.path.abspath(__file__))
    paths = [
        base_dir,
        os.path.join(base_dir, 'backend'),
        os.path.join(base_dir, 'backend', 'Bac'),
        os.path.join(base_dir, 'backend', 'Bac', 'myblog_project'),
    ]
    
    for path in paths:
        if path not in sys.path:
            sys.path.insert(0, path)
    
    django.setup()

def create_sample_data():
    """Créer des données d'exemple pour Vercel"""
    try:
        from blog.models import Article
        from django.contrib.auth.models import User
        
        # Créer un utilisateur par défaut si nécessaire
        if not User.objects.filter(username='masco_team').exists():
            user = User.objects.create_user(
                username='masco_team',
                email='contact@masco.cd',
                password='masco123'
            )
            print("✅ Utilisateur créé: masco_team")
        else:
            user = User.objects.get(username='masco_team')
        
        # Créer des articles d'exemple si nécessaire
        if not Article.objects.exists():
            articles = [
                {
                    'titre': 'Innovation dans les Énergies Renouvelables',
                    'contenu': 'Chez Masco, nous développons des solutions énergétiques durables pour l\'avenir de la RDC...',
                    'auteur': user,
                },
                {
                    'titre': 'Projets d\'Infrastructure Moderne',
                    'contenu': 'Notre équipe réalise des projets d\'infrastructure innovants qui transforment les communautés...',
                    'auteur': user,
                },
                {
                    'titre': 'Développement Durable en Construction',
                    'contenu': 'Les pratiques de construction durable sont au cœur de notre mission chez Masco...',
                    'auteur': user,
                }
            ]
            
            for article_data in articles:
                Article.objects.create(**article_data)
            
            print(f"✅ {len(articles)} articles créés")
        
    except Exception as e:
        print(f"⚠️ Erreur lors de la création des données: {e}")

def main():
    """Script de construction pour Vercel"""
    print("🔨 Début du processus de construction pour Vercel...")
    
    try:
        setup_django()
        
        # Exécuter les migrations
        print("📦 Exécution des migrations...")
        execute_from_command_line(['manage.py', 'migrate', '--noinput'])
        
        # Créer des données d'exemple
        print("📝 Création des données d'exemple...")
        create_sample_data()
        
        print("✅ Construction terminée avec succès!")
        
    except Exception as e:
        print(f"❌ Erreur lors de la construction: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
