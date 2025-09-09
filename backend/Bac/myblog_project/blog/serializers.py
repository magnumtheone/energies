from rest_framework import serializers
from .models import Article, Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'titre', 'fichier', 'url']

class ArticleSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = ['id', 'titre', 'contenu', 'date_publication', 'auteur', 'image', 'videos']

class ArticleListSerializer(serializers.ModelSerializer):
    """Serializer simplifié pour la liste d'articles (sans le contenu complet)"""
    
    class Meta:
        model = Article
        fields = ['id', 'titre', 'contenu', 'date_publication', 'auteur', 'image']
