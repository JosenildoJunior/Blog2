from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_post = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    

    def __str__(self):
        return self.titulo
        
