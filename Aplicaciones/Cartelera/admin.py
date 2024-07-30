from django.contrib import admin
from.models import Genero
from.models import Director
from.models import Paises
from.models import Pelicula
# Register your models here.
admin.site.register(Genero)
admin.site.register(Director)
admin.site.register(Paises)
admin.site.register(Pelicula)