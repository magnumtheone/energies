from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Article

class Command(BaseCommand):
    help = 'Nettoie la base de données en supprimant les utilisateurs et articles indésirables'

    def handle(self, *args, **options):
        # Supprimer l'utilisateur "college_maele" s'il existe
        try:
            user_to_delete = User.objects.get(username='college_maele')
            user_to_delete.delete()
            self.stdout.write(
                self.style.SUCCESS('Utilisateur "college_maele" supprimé avec succès!')
            )
        except User.DoesNotExist:
            self.stdout.write(
                self.style.WARNING('Utilisateur "college_maele" non trouvé.')
            )
        
        # Supprimer tous les anciens articles (gardons seulement les 3 articles Masco)
        articles_to_keep = [
            'Réhabilitation ferroviaire : premières phases',
            'Techniques modernes de génie civil en RDC', 
            'Sécurité et formation sur nos chantiers'
        ]
        
        # Supprimer tous les articles qui ne sont pas dans la liste
        old_articles = Article.objects.exclude(titre__in=articles_to_keep)
        count = old_articles.count()
        old_articles.delete()
        
        if count > 0:
            self.stdout.write(
                self.style.SUCCESS(f'{count} ancien(s) article(s) supprimé(s).')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('Aucun ancien article à supprimer.')
            )
        
        # Afficher le résumé
        remaining_articles = Article.objects.count()
        remaining_users = User.objects.count()
        
        self.stdout.write(
            self.style.SUCCESS(f'\nRésumé après nettoyage:')
        )
        self.stdout.write(f'- Articles restants: {remaining_articles}')
        self.stdout.write(f'- Utilisateurs restants: {remaining_users}')
        
        if remaining_articles > 0:
            self.stdout.write('\nArticles actuels:')
            for article in Article.objects.all():
                self.stdout.write(f'  - {article.titre} (par {article.auteur})')
