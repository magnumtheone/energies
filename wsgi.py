import os
import sys
from django.core.wsgi import get_wsgi_application

# Ajouter le chemin racine au PYTHONPATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.Bac.myblog_project.myblog_project.settings')

application = get_wsgi_application()

# Pour Vercel
app = application
