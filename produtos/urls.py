from django.urls import path
from . import views

urlpatterns = [
    path('relatorio_vist/', views.relatorio_vist, name = 'relatorio_vist' ),
    
]
