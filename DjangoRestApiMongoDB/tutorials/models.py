from django.db import models

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)
#Chaque champ est spécifié en tant qu'attribut de classe 
#et chaque attribut est mappé à une colonne de base de données.
#Le champ id est ajouté automatiquement.