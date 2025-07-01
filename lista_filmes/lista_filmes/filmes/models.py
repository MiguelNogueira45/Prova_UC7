from django.db import models

class Lista_FilmesModel(models.Model):
    nome = models.CharField(max_length=45)
    status = models.BooleanField(default=False)
    duracao = models.CharField(max_length=10)

   
        


