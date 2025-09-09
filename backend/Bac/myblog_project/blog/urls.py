from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                       # / -> index.html (front)
    path('articles/', views.accueil, name='accueil'),        # /articles/ -> page listant tous les articles
    path('article/<int:id_article>/', views.detail_article, name='detail_article'),
    
    # API endpoints
    path('api/articles/', views.api_articles_list, name='api_articles_list'),
    path('api/article/<int:id_article>/', views.api_article_detail, name='api_article_detail'),
]