from django.urls import path
from . import views
urlpatterns = [
    path('ver_relatorios/', views.ver_relatorios, name="ver_relatorios")
]
