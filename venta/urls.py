from django.urls import path
from . import views
from tiendaMusica.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('carrito/', views.carrito, name='carrito'),
    path('video/', views.video, name='video'),
    path('contacto/', views.contacto, name='contacto'),
    path('inicio/', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('agregar-album', views.agregar_album, name='agregar-album'),
    path('listar-album', views.listar_album, name='listar-album'),
    path('modificar-album/<id>', views.modificar_album, name='modificar-album'),
    path('eliminar-album/<id>', views.eliminar_album, name='eliminar-album'),
    
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)

