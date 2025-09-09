from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Article

def home(request):
    """
    Page d'accueil publique (front statique + petits extraits du blog).
    Affiche les 4 derniers articles pour la section blog du front.
    """
    articles = Article.objects.order_by('-date_publication')[:3]
    return render(request, 'blog/masco_index.html', {'articles': articles})

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

# API Views pour le frontend
@csrf_exempt
@require_http_methods(["GET"])
def api_articles_list(request):
    """
    API pour récupérer la liste des articles au format JSON
    """
    try:
        articles = Article.objects.order_by('-date_publication')
        
        articles_data = []
        for article in articles:
            article_data = {
                'id': article.id,
                'titre': article.titre,
                'contenu': article.contenu,
                'date_publication': article.date_publication.isoformat(),
                'auteur': article.auteur,
                'image': article.image.url if article.image else None,
            }
            articles_data.append(article_data)
        
        return JsonResponse(articles_data, safe=False)
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["GET"])
def api_article_detail(request, id_article):
    """
    API pour récupérer un article spécifique au format JSON
    """
    try:
        article = get_object_or_404(Article, id=id_article)
        
        article_data = {
            'id': article.id,
            'titre': article.titre,
            'contenu': article.contenu,
            'date_publication': article.date_publication.isoformat(),
            'auteur': article.auteur,
            'image': article.image.url if article.image else None,
        }
        
        return JsonResponse(article_data)
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

