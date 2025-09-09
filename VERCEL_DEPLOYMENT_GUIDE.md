# 🚀 Déploiement Vercel - Projet Masco

## 📋 Configuration pour Vercel

Votre projet Masco a été reconfiguré pour être déployé sur **Vercel**. Voici ce qui a été fait :

### ✅ Fichiers Ajoutés/Modifiés

#### 🔧 Configuration Vercel
- **`vercel.json`** - Configuration principale Vercel
- **`wsgi.py`** - Point d'entrée WSGI pour Vercel
- **`requirements.txt`** - Dépendances Python
- **`build.py`** - Script de build automatique
- **`manage.py`** - Gestionnaire Django à la racine

#### 🔗 Modules Python
- **`backend/__init__.py`** - Module backend
- **`backend/Bac/__init__.py`** - Sous-module Bac

#### ⚙️ Settings Django
- **ALLOWED_HOSTS** configuré pour Vercel
- **DEBUG** basé sur variable d'environnement
- Configuration statique pour production

### 🎯 Structure Optimisée

```
Masco/
├── vercel.json              # Configuration Vercel
├── wsgi.py                  # Point d'entrée WSGI
├── requirements.txt         # Dépendances Python
├── build.py                 # Script de build
├── manage.py                # Gestionnaire Django
├── backend/                 # Backend Django
│   ├── __init__.py         # Module Python
│   └── Bac/
│       ├── __init__.py     # Sous-module Python
│       └── myblog_project/ # Projet Django principal
└── README.md                # Documentation
```

### 🚀 Étapes de Déploiement

#### 1. Préparer le Repository
```bash
# Ajouter les nouveaux fichiers à Git
git add .
git commit -m "Configure project for Vercel deployment

✨ Added:
- vercel.json configuration
- wsgi.py entry point
- requirements.txt
- build.py script
- Python modules structure

🎯 Ready for Vercel deployment!"

git push origin main
```

#### 2. Déployer sur Vercel

##### Option A: Via Interface Web
1. Aller sur [vercel.com](https://vercel.com)
2. Se connecter avec GitHub
3. Importer le repository `energies`
4. Vercel détectera automatiquement la configuration
5. Cliquer sur "Deploy"

##### Option B: Via CLI Vercel
```bash
# Installer Vercel CLI
npm i -g vercel

# Se connecter
vercel login

# Déployer depuis le dossier racine
cd "d:\Maquettes\Masco"
vercel --prod
```

### ⚙️ Variables d'Environnement Vercel

Dans le dashboard Vercel, ajouter ces variables :

```
DEBUG=False
DJANGO_SETTINGS_MODULE=backend.Bac.myblog_project.myblog_project.settings
SECRET_KEY=votre-clé-secrète-django
```

### 🌐 URLs de Production

Une fois déployé, votre site sera accessible sur :
- **URL Vercel :** `https://votre-projet.vercel.app`
- **Domaine custom :** Configurable dans Vercel

### 📂 Fichiers Statiques

Les fichiers statiques seront servis directement par Vercel :
- **Images :** `/static/blog/images/`
- **CSS :** `/static/blog/css/`
- **Vidéos :** `/static/blog/videos/`

### 🔧 Configuration Avancée

#### Base de Données
- **Développement :** SQLite (local)
- **Production :** SQLite (Vercel supporte SQLite)
- **Alternative :** PostgreSQL avec Vercel Postgres

#### Domaine Personnalisé
1. Dans Vercel Dashboard → Settings
2. Domains → Add Domain
3. Configurer DNS selon instructions

#### HTTPS
- **Automatique** avec certificats SSL gratuits
- **Redirection HTTP → HTTPS** activée par défaut

### 🛠️ Commandes Utiles

```bash
# Test local
python manage.py runserver

# Build local
python build.py

# Déploiement Vercel
vercel --prod

# Logs de production
vercel logs
```

### ⚡ Performance Vercel

- **Edge Network** : CDN global automatique
- **Serverless Functions** : Auto-scaling
- **Static Generation** : Fichiers optimisés
- **Analytics** : Métriques intégrées

### 🐛 Dépannage

#### Erreurs Courantes
1. **Import Error** : Vérifier les `__init__.py`
2. **Static Files** : Exécuter `collectstatic`
3. **Database** : Migrations appliquées
4. **Secrets** : Variables d'environnement configurées

#### Logs
```bash
# Voir les logs Vercel
vercel logs --follow

# Logs de build
vercel logs --build
```

### 📞 Support

- **Vercel Docs** : [vercel.com/docs](https://vercel.com/docs)
- **Django on Vercel** : [vercel.com/guides/deploying-django-with-vercel](https://vercel.com/guides/deploying-django-with-vercel)

## 🎉 Votre Projet Masco est Prêt pour Vercel !

**Repository :** Configuré ✅  
**Build Scripts :** Créés ✅  
**Configuration :** Optimisée ✅  
**Documentation :** Complète ✅  

Il suffit maintenant de push sur GitHub et déployer sur Vercel ! 🚀
