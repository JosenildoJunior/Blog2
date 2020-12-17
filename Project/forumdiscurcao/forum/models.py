from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_post = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    autor = models.ForeignKey(User, on_delete=models.RESTRICT)
    

    def __str__(self):
        return self.titulo
        
