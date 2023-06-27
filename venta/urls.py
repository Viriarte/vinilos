from django.urls import path
from . import views

urlpatterns =[
    
    path('', views.index, name='index'),
    path('vinilos/', views.vinilos, name='vinilos'),
    path('accesorios/', views.accesorios, name='accesorios'),
    path('cassetes/', views.cassetes, name='cassetes'),
    path('cds/', views.cds, name='cds'),
    path('compra/', views.compra, name='compra'),
    path('contacto/', views.contacto, name='contacto'),
    path('cuentas/', views.cuentas, name='cuentas'),
    path('index/', views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    path('genero', views.lista_generos, name='genero'),
    path('lista_albums',views.lista_albums, name='lista_albums'),
    path('agregar_album',views.agregar_album, name='albumsAdd'),
    path('eliminar_album/<str:pk>',views.eliminar_album, name='album_del'),
    path('buscar_album/<str:pk>',views.buscar_album, name='album_findEdit'),
    path('actualizar_album',views.modificar_album, name='albumUpdate'),
]




