from django.urls import path
from Mascotillas import views


urlpatterns = [
    path('',views.home, name="Home"),
    path('home',views.home, name="Home"),
    path('Mascotas',views.mascotas, name="mascotas"),
    path('Productos',views.productos,name="productos"),
    path('Servicios',views.servicios,name="servicios"),
    path('buscarMascota',views.buscarMascota,name="BuscarMascota"),
    path('buscar/',views.buscar,name="Buscar"),
]