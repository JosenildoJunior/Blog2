from django.urls import path
from . import views

app_name = 'forums'

urlpatterns = [
    # página inicial !
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('novo_post', views.novo_post, name='novo_post'),
    path('edit_post/<int:edit_id>', views.edit_post, name='edit_post'),
    
]
