from django.urls import path
from . import views

urlpatterns = [ # Urls para redireccionar las vistas 
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),#Ruta para el login
    path('register/', views.registro, name='register'),#Ruta para registrar
    path('agregar/', views.agregar_persona, name='agregar_persona'),# Ruta para agregar persona
    path('logout/', views.logout_view, name='logout'),#Ruta para cerrar sesion.
]