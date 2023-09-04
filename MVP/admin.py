from django.contrib import admin
from .models import CuidadorMascotas, Mascota, DuenoMascota

admin.site.register(CuidadorMascotas)
admin.site.register(Mascota)
admin.site.register(DuenoMascota)