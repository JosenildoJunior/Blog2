from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_post = models.DateTimeField('Data da publicação')
    

    def __str__(self):
        return self.titulo
