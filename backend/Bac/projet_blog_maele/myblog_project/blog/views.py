from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    """
    Page d'accueil publique (front statique + petits extraits du blog).
    Affiche les 4 derniers articles pour la section blog du front.
    """
    articles = Article.objects.order_by('-date_publication')[:3]
    return render(request, 'blog/index.html', {'articles': articles})

def accueil(request):
    """
    Page listant tous les articles (utilisée pour la page 'Articles').
    """
    articles = Article.objects.order_by('-date_publication')
    return render(request, 'blog/accueil.html', {'articles': articles})

def detail_article(request, id_article):
    """
    Cette vue affiche un article détaillé en fonction de son ID.
    """
    # Récupérer l'article spécifique par son ID
    article = get_object_or_404(Article, id=id_article)
    return render(request, 'blog/detail.html', {'article': article})

