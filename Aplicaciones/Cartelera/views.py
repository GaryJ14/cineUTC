from django.http import JsonResponse
from django.shortcuts import redirect, render
from.models import Genero, Pelicula, Director, Paises, Cine
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return render(request,"home.html")
#Renderizando el template de ListadoGeneros
def ListadoGeneros(request):
    generosbdd=Genero.objects.all()

    return render(request, "listadoGeneros.html",{'generos': generosbdd})

#Se revibe el id para eliminar un genero
def eliminarGenero(request,id):
    generoEliminar=Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request, "Género eliminado Correctamente")
    return redirect('listadoGeneros')

# Renderizando El formulario de nuevo genero
def nuevoGenero(request):
    return render(request,'nuevoGenero.html')
def guardarGenero(request):
    nom=request.POST['nombre']
    des=request.POST['descripcion']
    fot=request.FILES.get('foto')
    nuevoGenero=Genero.objects.create(nombre=nom, descripcion=des, foto=fot)
    messages.success(request, "Género registrado exitosamente")
    return redirect('listadoGeneros')

def editarGenero(request, id):
    generoEditar=Genero.objects.get(id=id)
    return render(request, 'editarGenero.html', {'generoEditar':generoEditar})
#Actualizando nuevos datos en la BDD
def procesarActualizacionGenero(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nombre
    generoConsultado.descripcion=descripcion
    generoConsultado.save()
    messages.success(request, 'Genero actualizado exitosamente.')
    return redirect('listadoGeneros')
#-----------------------------Pais--------------------------------------------------------------
#crear una nueva variable 

def ListadoPaises (request):
    paisbdd=Paises.objects.all()

    return render(request, "listadoPaises.html",{'pais': paisbdd})

def nuevoPais(request):
    return render(request,'nuevoPais.html')
#Insertando Genero en la base de datos 
def guardarPais(request):
    nom=request.POST["nombre"]
    con=request.POST["continente"]
    cap=request.POST["capital"]
    nuevoPais=Paises.objects.create(nombre=nom, continente=con, capital=cap )
    messages.success(request, "Pais registrado exitosamente")
    return redirect('listadoPais')
def eliminarPais(request,id):
    paisEliminar=Paises.objects.get(id=id)
    paisEliminar.delete()
    messages.success(request, "Pais eliminado Correctamente")
    return redirect('/listadoPais') 
#Renderozando formulario de actualización 
def editarPais(request, id):
    paisEditar=Paises.objects.get(id=id)
    return render(request, 'editarPais.html', {'paisEditar':paisEditar})
#Actualizando nuevos datos en la BDD
def procesarActualizacionPais(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    continente=request.POST['continente']
    capital=request.POST['capital']
    paisConsultado=Paises.objects.get(id=id)
    paisConsultado.nombre=nombre
    paisConsultado.continente=continente
    paisConsultado.capital=capital
    paisConsultado.save()
    messages.success(request, 'Pais actualizado exitosamente.')
    return redirect('listadoPais')
#-------------------------------DIRECTORES----------------------------------------------------s
def ListadoDirectores(request):
    directoresBdd=Director.objects.all()
    return render(request, "listadoDirectores.html", {'directores':directoresBdd})

def directorDel(request, id):
    directorDel = Director.objects.get(id = id)
    directorDel.delete()
    messages.success(request, "Director eliminado exitosamente.")
    return redirect('listadoDirectores')

def directorAddForm(request):
    return render(request, "addDirectores.html")

def fetchDirectores(request):
    return render(request, "fetchDirectores.html")

def TablaFetchDirectores(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        directores = Director.objects.all().values('id','dni', 'apellido', 'nombre', 'estado')
        return JsonResponse(list(directores), safe=False)
    return JsonResponse({"error": "Invalid request"}, status=400)

def tablaDirectores(request):
    return render(request, "tablaDirectores.html")

def directorAddFetch(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            dni = request.POST['dni']
            apellido = request.POST['apellido']
            nombre = request.POST['nombre']
            estado = request.POST.get('estado') == 'True'
            foto_dir = request.FILES.get('foto_dir')

            new_director = Director.objects.create(
                dni=dni, 
                apellido=apellido, 
                nombre=nombre, 
                foto_dir=foto_dir, 
                estado=estado
            )

            return JsonResponse({
                'estado': True,
                'mensaje': 'Director registrado exitosamente.'})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error"}, status=400)


def directorAdd(request):
    dni=request.POST['dni']
    apellido=request.POST['apellido']
    nombre=request.POST['nombre']
    foto_dir = request.FILES.get("foto_dir")
    estado=request.POST.get('estado')
    if(request.POST.get('estado') == 'True'):
        est = True
    else:
        est = False

    newPais = Director.objects.create(dni=dni, apellido = apellido, nombre = nombre, foto_dir = foto_dir, estado = estado)
    messages.success(request, "Director registrado exitosamente.")
    return redirect('listadoDirectores')


def directorUpdateForm(request, id):
    dateDirector = Director.objects.get(id = id)
    return render(request, "editarDirectores.html", {'dateDirector' : dateDirector})

def directorUpdate(request):
    id=request.POST['id']
    dni=request.POST['dni']
    apellido=request.POST['apellido']
    nombre=request.POST['nombre']
    fot = request.FILES.get("foto_dir")
    estado=request.POST.get('estado')
   
    consulta =Director.objects.get(id = id)
    consulta.dni = dni
    consulta.apellido = apellido
    consulta.nombre = nombre
    consulta.foto_dir = fot
    if(request.POST.get('estado') == 'True'):
        est = True
    else:
        est = False
    consulta.estado = estado
    consulta.save()
    messages.success(request,'Director actualizado exitosamente.')
    return redirect('listadoDirectores')

#Funcion para gestionar el crud de Cines
def gestionCines(request):
    return render(request,'gestionCines.html')

#Insertando cines mediante AJAX en la Base de Datos

@csrf_exempt
def guardarCine(request):
    nom=request.POST["nombre"]
    dir=request.POST["direccion"]
    tel=request.POST["telefono"]
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel)    
    return JsonResponse({
        'estado': True,
        'mensaje': 'Género registrado exitosamente.'
    })
#reenderizar el listado de cines
def listadoCines (request):
    cines=Cine.objects.all()

    return render(request, "listadoCines.html",{'cines': cines})

#crear una nueva variable 
def ListadoPeliculas(request):
    
    peliculabdd=Pelicula.objects.all()

    return render(request, "listadoPeliculas.html",{'pelicula': peliculabdd})

def fetchPeliculas(request):
    generos = Genero.objects.all()
    directores = Director.objects.all()
    return render(request, "fetchPeliculas.html", {'generos': generos, 'directores': directores})

def tablaPeliculasFetch(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        peliculas = Pelicula.objects.all().values('id', 'titulo', 'duracion', 'sinopsis', 'genero__nombre', 'director__nombre')
        return JsonResponse(list(peliculas), safe=False)
    
    return JsonResponse({"error": "Invalid request"}, status=400)

def tablaPeliculas(request):
    return render(request, "tablaPeliculas.html")


def peliculaAddFetch(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            titulo = request.POST.get('titulo')
            duracion = request.POST.get('duracion')
            sinopsis = request.POST.get('sinopsis')
            id= request.POST.get('genero')
            id = request.POST.get('director')
            portada = request.FILES.get('portada')
            genero = Genero.objects.get(id=id)
            director = Director.objects.get(id=id)

            nueva_pelicula = Pelicula(
                titulo=titulo,
                duracion=duracion,
                sinopsis=sinopsis,
                genero=genero,
                director=director,
                portada=portada
            )
            nueva_pelicula.save()
            return JsonResponse({
                'estado': True,
                'mensaje': 'Cine registrado exitosamente.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)








#DIRECTORES

def directorAddFetch(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            dni = request.POST['dni']
            apellido = request.POST['apellido']
            nombre = request.POST['nombre']
            estado = request.POST.get('estado') == 'True'
            fot = request.FILES.get('foto_dir')

            new_director = Director.objects.create(
                dni=dni, 
                apellido=apellido, 
                nombre=nombre, 
                foto_dir=fot, 
                estado=estado
            )

            return JsonResponse({
                'estado': True,
                'mensaje': 'Cine registrado exitosamente.'})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error"},status=400)
                        

def TablaFetchDirectores(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        directores = Director.objects.all().values('id','dni', 'apellido', 'nombre', 'estado','foto_dir')
        return JsonResponse(list(directores), safe=False)
    return JsonResponse({"error": "Invalid request"}, status=400)