from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarUsuario/', views.registrarUsuario),
    path('edicionUsuario/<dni>', views.edicionUsuario),
    path('editarUsuario/', views.editarUsuario),
    path('eliminarUsuario/<dni>', views.eliminarUsuario)
]