from django.shortcuts import render
from .models import Genero, Album
from .forms import GeneroForm
from django.contrib.auth.decorators import login_required



def index(request):
    lista_albums = Album.objects.all()
    context = {"albums": lista_albums}
    return render(request, 'venta/agregar.html', context)

def vinilos(request):
    return render(request, 'venta/vinilos.html')

def accesorios(request):
    return render(request, 'venta/accesorios.html')

def cassetes(request):
    return render(request, 'venta/cassetes.html')

def cds(request):
    return render(request, 'venta/cds.html')

def compra(request):
    return render(request, 'venta/compra.html')

def contacto(request):
    return render(request, 'venta/contacto.html')

def cuentas(request):
    return render(request, 'venta/cuentas.html')

def index(request):
    return render(request, 'venta/index.html')

def inicio(request):
    return render(request, 'venta/inicio.html')

def lista_albums(request):
    lista_albums = Album.objects.all()
    context = {"albums": lista_albums}
    return render(request, 'venta/agregar.html', context)

def lista_generos(request):
    lista_generos = Genero.objects.all()
    context = {"generos": lista_generos}
    return render(request, 'venta/otro.html', context)

@login_required
def agregar_album(request):
    if request.method != "POST":
        lista_generos = Genero.objects.all()
        context = {"generos": lista_generos}
        return render(request, 'venta/albums_add.html', context)
    else:
        id_album = request.POST["id_album"]
        titulo = request.POST["titulo"]
        lanzamiento = request.POST["lanzamiento"]
        cantidad_canciones = request.POST["cantCanciones"]
        tracklist = request.POST["tracklist"]
        duracion = request.POST["duracion"]
        notas = request.POST["notas"]
        disponibilidad = request.POST["disponibilidad"]

        objAlbum = Album.objects.create(
            id_album=id_album,
            titulo=titulo,
            lanzamiento=lanzamiento,
            cantidad_canciones=cantidad_canciones,
            tracklist=tracklist,
            duracion=duracion,
            notas=notas,
            disponibilidad=disponibilidad
        )

        lista_generos = Genero.objects.all()
        context = {"mensaje": "Se guardó el álbum", "generos": lista_generos}
        return render(request, 'venta/albums_add.html', context)

def eliminar_album(request, pk):
    try:
        album = Album.objects.get(id_album=pk)
        album.delete()
        mensaje = "El álbum se eliminó"
        lista_albums = Album.objects.all()
        context = {"albums": lista_albums, "mensaje": mensaje}
        return render(request, 'venta/agregar.html', context)
    except:
        mensaje = "El álbum NO se eliminó"
        lista_albums = Album.objects.all()
        context = {"albums": lista_albums, "mensaje": mensaje}
        return render(request, 'venta/agregar.html', context)

def buscar_album(request, pk):
    if pk != "":
        album = Album.objects.get(id_album=pk)
        lista_generos = Genero.objects.all()
        context = {"album": album, "generos": lista_generos}
        return render(request, 'venta/albums_edit.html', context)
    else:
        mensaje = "El álbum NO existe"
        context = {"mensaje": mensaje}
        return render(request, 'venta/agregar.html', context)

def modificar_album(request):
    if request.method == "POST":
        id_album = request.POST["id_album"]
        titulo = request.POST["titulo"]
        lanzamiento = request.POST["lanzamiento"]
        genero = request.POST["genero"]
        cantidad_canciones = request.POST["cantCanciones"]
        tracklist = request.POST["tracklist"]
        duracion = request.POST["duracion"]
        notas = request.POST["notas"]
        disponibilidad = request.POST["disponibilidad"]

        objAlbum = Album.objects.get(id_album=id_album)
        objAlbum.titulo = titulo
        objAlbum.lanzamiento = lanzamiento
        objAlbum.genero = genero
        objAlbum.cantidad_canciones = cantidad_canciones
        objAlbum.tracklist = tracklist
        objAlbum.duracion = duracion
        objAlbum.notas = notas
        objAlbum.disponibilidad = disponibilidad
        objAlbum.save()

        lista_generos = Genero.objects.all()
        context = {"mensaje": "Se actualizó el álbum", "generos": lista_generos, "album": objAlbum}
        return render(request, 'venta/albums_edit.html', context)
    else:
        lista_albums = Album.objects.all()
        context = {"albums": lista_albums}
        return render(request, 'venta/agregar.html', context)
    
    def listar_generos(request):
        usuario = request.session["usuario"]
    listar_generos = Genero.objects.all() 
    context = {"generos":listar_generos,"usu":usuario}
    return render(request,'venta/generos_list.html', context)

def agregar_generos(request):
    if request.method == "POST":
        form = GeneroForm(request.POST)
        if form.is_valid:
            form.save()
            form = GeneroForm()
            context = {"mensaje":"Se guardó género","form":form}
            return render(request,'venta/generos_add.html', context)
    else:
        form = GeneroForm()
        context = {"form":form}
        return render(request,'venta/generos_add.html', context)
    
def eliminar_genero(request,pk):
    try:
        genero = Genero.objects.get(id_genero=pk)
        if genero:
            genero.delete()
            lista_generos = Genero.objects.all()
            mensaje = "Se eliminó género"
            context = {"mensaje":mensaje, "generos":lista_generos}
            return render(request,'venta/generos_list.html', context)
    except:
        lista_generos = Genero.objects.all()
        mensaje = "No existe género"
        context = {"mensaje":mensaje, "generos":lista_generos}
        return render(request,'venta/generos_list.html', context)

def editar_genero(request,pk):
    try:
        genero = Genero.objects.get(id_genero=pk)
        if genero:
            if request.method == "POST":
                form = GeneroForm(request.POST,instance=genero)
                form.save()
                form = GeneroForm()
                context = {"mensaje":"Se modificó género","form":form}
                return render(request,'venta/generos_edit.html', context)
            else:
                form = GeneroForm(instance=genero)
                context = {"form":form,"genero":genero}
                return render(request,'venta/generos_edit.html', context)
    except:
        lista_generos = Genero.objects.all()
        mensaje = "No existe género"
        context = {"mensaje":mensaje, "generos":lista_generos}
        return render(request,'venta/generos_list.html', context)
