from django.core.management.base import BaseCommand
from blog.models import Article
from django.utils import timezone

class Command(BaseCommand):
    help = 'Crée des articles exemple pour Masco'

    def handle(self, *args, **options):
        # Supprimer les articles existants si nécessaire
        Article.objects.all().delete()
        
        # Créer des articles exemple
        articles_data = [
            {
                'titre': 'Réhabilitation ferroviaire : premières phases',
                'contenu': """La réhabilitation de la ligne ferroviaire Kisangani-Ubundu entre dans sa phase active. 
                
                Nos équipes ont commencé les travaux de terrassement et de pose des nouvelles traverses. Cette infrastructure de 115 kilomètres représente un défi technique majeur compte tenu du climat tropical et des contraintes logistiques.

                Les principales étapes comprennent :
                - Évaluation complète de l'état des rails existants
                - Renforcement des ouvrages d'art (ponts et tunnels)
                - Installation de nouveaux systèmes de signalisation
                - Formation du personnel local

                Ce projet s'inscrit dans la vision de développement économique régional et permettra de réduire significativement les coûts de transport de marchandises entre ces deux centres urbains importants.""",
                'auteur': 'Gabriel MADUA MASUDI'
            },
            {
                'titre': 'Techniques modernes de génie civil en RDC',
                'contenu': """L'adaptation des techniques de construction internationales aux réalités du terrain congolais nécessite une approche innovante et pragmatique.

                Chez Masco, nous développons des méthodes qui tiennent compte des spécificités locales :

                **Matériaux locaux optimisés**
                Utilisation du sable de rivière traité et des granulats locaux pour réduire les coûts et l'empreinte carbone.

                **Techniques de bétonnage adaptées**
                Développement de formules de béton résistant aux variations climatiques tropicales avec des adjuvants naturels.

                **Formation continue**
                Mise en place de programmes de formation pour nos équipes locales sur les dernières normes internationales.

                Ces innovations nous permettent de livrer des ouvrages durables tout en respectant les budgets et délais impartis.""",
                'auteur': 'Park CHANG MOOK'
            },
            {
                'titre': 'Sécurité et formation sur nos chantiers',
                'contenu': """La sécurité constitue notre priorité absolue sur tous nos chantiers. Nous avons mis en place un programme complet de formation et de sensibilisation.

                **Programme de sécurité intégrée**
                - Formations obligatoires avant tout début de chantier
                - Équipements de protection individuelle fournis
                - Contrôles quotidiens des installations
                - Procédures d'urgence clairement définies

                **Formation technique continue**
                Nos partenariats avec des instituts techniques permettent à nos équipes d'acquérir de nouvelles compétences :
                - Soudure spécialisée pour les structures métalliques
                - Topographie et géomètres
                - Conduite d'engins de chantier
                - Gestion de projet

                **Résultats concrets**
                Depuis la mise en place de ce programme, nous avons observé une réduction de 75% des incidents sur nos chantiers et une amélioration notable de la qualité des ouvrages livrés.

                Cette approche renforce également l'employabilité de nos équipes et contribue au développement des compétences locales.""",
                'auteur': 'Georges OYEMA SHULUNGU'
            }
        ]

        for i, article_data in enumerate(articles_data):
            article = Article.objects.create(
                titre=article_data['titre'],
                contenu=article_data['contenu'],
                auteur=article_data['auteur'],
                date_publication=timezone.now() - timezone.timedelta(days=30-i*10)
            )
            self.stdout.write(
                self.style.SUCCESS(f'Article créé: "{article.titre}"')
            )

        self.stdout.write(
            self.style.SUCCESS(f'Créé {len(articles_data)} articles avec succès!')
        )
