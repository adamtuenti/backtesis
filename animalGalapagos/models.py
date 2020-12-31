from django.db import models
from django.conf import settings
from django.contrib import admin
# from django.contrib.auth.models import User
import django.db.models.deletion




class AnimalModel(models.Model):
    idAnimal = models.CharField(primary_key=True, max_length=254)
    imagenAnimal = models.ImageField(upload_to = "AnimalImagenes/")
    nombreAnimal = models.CharField(max_length=254)
    nombreTecnico = models.CharField(max_length=100, default=None)


	

    def __str__(self):
        return str(self.idAnimal)


admin.site.register(AnimalModel)