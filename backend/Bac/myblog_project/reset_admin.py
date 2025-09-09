#!/usr/bin/env python
"""
Script pour créer un nouveau superutilisateur ou réinitialiser le mot de passe d'un existant
"""
import os
import django
import sys

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog_project.settings')
django.setup()

from django.contrib.auth.models import User

def create_or_reset_superuser():
    """Crée un nouveau superutilisateur ou réinitialise un existant"""
    
    username = 'admin'
    email = 'admin@masco.com'
    password = 'masco123'  # Mot de passe simple à retenir
    
    try:
        # Essaie de trouver un utilisateur existant
        user = User.objects.get(username=username)
        print(f"Utilisateur '{username}' trouvé. Mise à jour du mot de passe...")
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.email = email
        user.save()
        print(f"✅ Mot de passe mis à jour pour l'utilisateur '{username}'")
        
    except User.DoesNotExist:
        # Crée un nouvel utilisateur si il n'existe pas
        print(f"Création d'un nouvel utilisateur '{username}'...")
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"✅ Superutilisateur '{username}' créé avec succès!")
    
    print(f"\n📝 Informations de connexion:")
    print(f"   Nom d'utilisateur: {username}")
    print(f"   Email: {email}")
    print(f"   Mot de passe: {password}")
    print(f"\n🌐 Accédez à l'admin Django à: http://127.0.0.1:8000/admin/")
    
    return user

if __name__ == '__main__':
    create_or_reset_superuser()
