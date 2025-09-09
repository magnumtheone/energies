Déploiement sur Render

Étapes rapides

1. Créer un service Web sur Render connecté à ce repository.
2. Variables d'environnement recommandées (Settings > Environment):
   - SECRET_KEY: clé Django secrète
   - DEBUG: False
   - DATABASE_URL: (par ex. postgres://user:pass@host:5432/dbname) — recommandé
   - AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME (si stockage S3 pour les médias)
   - RENDER_EXTERNAL_URL: https://<your-service>.onrender.com (optionnel)
3. Build command (Render):
   python backend/Bac/myblog_project/manage.py collectstatic --noinput --settings=myblog_project.settings
4. Start command (Render):
   gunicorn myblog_project.wsgi:application --bind 0.0.0.0:$PORT

Notes
- WhiteNoise est configuré pour servir les fichiers statiques.
- Pour les médias utilisateur en production, configure un stockage S3 ou Render Object Storage et définis les variables AWS.
- Assure-toi d'utiliser une base Postgres en production et de définir `DATABASE_URL`.
