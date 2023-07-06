from django.shortcuts import  render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm



# Create your views here.

def index(request):
    
    albums = Album.objects.all()
    data = {"albums": albums}
    return render(request, 'venta/index.html', data)

def carrito(request):
    return render(request, 'venta/carrito.html')

def contacto(request):
    return render(request, 'venta/contacto.html')

def video(request):
    return render(request, 'venta/video.html')

def inicio(request):
    return render(request, 'venta/inicio.html')


def agregar_album(request):
    data = {'form': AlbumForm()}
    
    if request.method == 'POST':
        formulario = AlbumForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data['form'] = formulario
    
    
    return render(request, 'venta/album/agregar.html', data)



def listar_album(request):
    albums = Album.objects.all()
    data = {'albums': albums}
    return render(request, 'venta/album/listar.html', data)
    

def modificar_album(request, id):
    album = get_object_or_404(Album, id=id)
    data = {'form': AlbumForm(instance=album)}
    
    if request.method == 'POST':
        formulario = AlbumForm(data=request.POST, instance=album, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Album modificado correctamente"
            return redirect(to="listar-producto")
        data['form'] = formulario
    
    return render(request, 'venta/album/modificar.html', data)

def eliminar_album(request, id):
    album = get_object_or_404(Album, id=id)
    album.delete()
    return redirect(to="listar-album")


