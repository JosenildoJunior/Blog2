from django.urls import path
from . import views

app_name = 'forums'

urlpatterns = [
    # página inicial !
    path('', views.index, name='index'),
    
]
