import os
import sys
from django.core.wsgi import get_wsgi_application

# Ajouter les chemins nécessaires au PYTHONPATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'backend'))
sys.path.insert(0, os.path.join(BASE_DIR, 'backend', 'Bac'))
sys.path.insert(0, os.path.join(BASE_DIR, 'backend', 'Bac', 'myblog_project'))

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog_project.settings')

def _run_startup_tasks():
    """Exécuter migrations et créer données minimales sur Vercel (cold start)."""
    if os.environ.get('VERCEL_ENV'):
        try:
            from django.core.management import call_command
            from django.contrib.auth.models import User
            from blog.models import Article
            # Migrations
            call_command('migrate', interactive=False, verbosity=0)
            # Données exemples si vide
            if not User.objects.filter(username='masco_team').exists():
                User.objects.create_user('masco_team', password='masco123')
            user = User.objects.get(username='masco_team')
            if not Article.objects.exists():
                Article.objects.create(titre='Bienvenue chez Masco', contenu="Plateforme déployée sur Vercel.", auteur=user)
                Article.objects.create(titre='Nos Projets', contenu="Découvrez nos innovations en énergie et construction.", auteur=user)
        except Exception as e:
            print(f"[Startup] Erreur initialisation: {e}")

try:
    application = get_wsgi_application()
    _run_startup_tasks()
except Exception as e:
    print(f"Erreur lors du chargement de l'application Django: {e}")
    import traceback
    traceback.print_exc()
    raise

# Pour Vercel
app = application
