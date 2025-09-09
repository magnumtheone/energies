import os
import sys
import django

# Ensure project root is on PYTHONPATH so settings module can be imported
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog_project.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()
username = 'admin'
email = 'admin@example.com'
password = 'Admin1234!'
if User.objects.filter(username=username).exists():
    print('SUPERUSER ALREADY EXISTS')
else:
    User.objects.create_superuser(username, email, password)
    print('SUPERUSER CREATED')
