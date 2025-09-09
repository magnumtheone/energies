@echo off
echo Démarrage du serveur Django pour Masco...
cd /d "d:\Maquettes\Masco\backend\Bac\myblog_project"

echo Activation de l'environnement virtuel...
call venv\Scripts\activate

echo Vérification des migrations...
python manage.py makemigrations
python manage.py migrate

echo Démarrage du serveur sur http://127.0.0.1:8000
echo.
echo IMPORTANT: Une fois le serveur démarré, ouvrez votre navigateur et allez sur:
echo http://127.0.0.1:8000
echo.
echo Les articles du blog devraient maintenant s'afficher correctement !
echo Pour arrêter le serveur, appuyez sur Ctrl+C
echo.
python manage.py runserver

pause
