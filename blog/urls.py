from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'), #notre premier modèle (pattern) d'URL
]
