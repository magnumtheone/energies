@echo off
echo =================================
echo    CONFIGURATION MASCO BLOG
echo =================================

cd /d "d:\Maquettes\Masco\backend\Bac\myblog_project"

echo 1. Activation de l'environnement virtuel...
call venv\Scripts\activate

echo 2. Installation des dépendances...
pip install django pillow

echo 3. Création et application des migrations...
python manage.py makemigrations
python manage.py migrate

echo 4. Création d'un superutilisateur (optionnel)...
echo Voulez-vous créer un compte administrateur? (y/n)
set /p create_admin=
if /i "%create_admin%"=="y" (
    python manage.py createsuperuser
)

echo 5. Création d'articles exemple...
python manage.py create_sample_articles

echo 6. Collecte des fichiers statiques...
python manage.py collectstatic --noinput

echo =================================
echo   CONFIGURATION TERMINÉE !
echo =================================
echo.
echo Pour démarrer le serveur, utilisez :
echo python manage.py runserver
echo.
echo Puis accédez à : http://127.0.0.1:8000
echo Interface admin : http://127.0.0.1:8000/admin
echo.
pause
