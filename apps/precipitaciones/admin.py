from django.contrib import admin
from apps.precipitaciones.models import Precipitaciones


@admin.register(Precipitaciones)
class PrecipitacionesAdmin(admin.ModelAdmin):
    pass