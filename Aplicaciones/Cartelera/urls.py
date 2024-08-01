#Configurando el redireccionamiento
from django.urls import path
from . import views
# Crear un arreglo
urlpatterns=[
    path('', views.home),
    #path('ListadoGeneros/',views.ListadoGeneros, name='listadoGeneros'),
    #path('ListadoPeliculas/', views.ListadoPeliculas),
    #path('ListadoDirectores/',views.ListadoDirectores),
    #path('ListadoPaises/',views.ListadoPaises),
    
    #path('eliminarGenero/<id>',views.eliminarGenero, name='eliminarGenero'),
    #path("nuevoGenero/",views.nuevoGenero, name='nuevoGenero'),
    #path('guardarGenero/', views.guardarGenero, name='guardarGenero'),


     #GENERO
    path('listadoGeneros/', views.ListadoGeneros,name='listadoGeneros'),
    path('eliminarGenero/<id>', views.eliminarGenero,name='eliminarGenero'),
    path('nuevoGenero/', views.nuevoGenero,name='nuevoGenero'),
    path('guardarGenero/', views.guardarGenero,name='guardarGenero'),
    path('editarGenero/<id>', views.editarGenero,name='editarGenero'),
    path('procesarActualizacionPis/', views.procesarActualizacionGenero,name='procesarActualizacionGenero'),
    #PAIS
    path('ListadoPaises/', views.ListadoPaises, name='ListadoPaises'),
    path('nuevoPais/', views.nuevoPais,name='nuevoPais'),
    path('guardarPais/', views.guardarPais,name='guardarPais'),
    path('editarPais/<id>', views.editarPais,name='editarPais'),
    path('eliminarPais/<id>', views.eliminarPais,name='eliminarPais'),
    path('procesarActualizacionPais/', views.procesarActualizacionPais,name='procesarActualizacionPais'),

    #DIRECTORES 
    path('tableDirectores', views.tablaDirectores, name = 'tableDirectores'),
    path('TablaFetchDirectores', views.TablaFetchDirectores, name = 'TablaFetchDirectores'),
    path('listadoDirectores', views.listadoDirectores, name = 'listadoDirectores'), 
    path('fetchDirectores', views.fetchDirectores, name = 'fetchDirectores'), 
    path('directorDel/<id>', views.directorDel, name = 'directorDel'),
    path('directorAddForm', views.directorAddForm, name = 'directorPaises'),
    path('directorAdd', views.directorAdd, name = 'directorAdd'),
    path('directorAddFetch', views.directorAddFetch, name = 'directorAddFetch'),
    path('directorUpdateForm/<id>', views.directorUpdateForm, name = 'directorUpdateForm'),
    path('directorUpdate', views.directorUpdate, name = "directorUpdate"),

    #PELICULAS
   
    path('listadoPeliculas', views.ListadoPeliculas),
    path('tablePeliculasFetch', views.tablaPeliculasFetch, name='tablePeliculasFetch'),
    path('fetchPeliculas', views.fetchPeliculas, name='fetchPeliculas'),
    path('peliculaAddFetch', views.peliculaAddFetch, name='peliculaAddFetch'),

 #PAISES
    path('ListadoPeliculas/', views.ListadoPeliculas, name='ListadoPeliculas'),
    #path('guardarPelicula/',views.guardarPelicula, name='guardarPelicula'), 
    #gestion CInes
    path('gestionCines/',views.gestionCines, name='gestionCines'), 
    path('guardarCine/',views.guardarCine, name='guardarCine'), 
    path('listadoCines/',views.listadoCines, name='listadoCines'), 
]