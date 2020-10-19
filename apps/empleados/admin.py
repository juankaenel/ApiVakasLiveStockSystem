from django.contrib import admin
from apps.empleados.models import Empleados


@admin.register(Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    """Usuario admin"""
    #campos a mostrar
    #list_display = ('pk') # mostrame estos datos
    ##links
    #list_display_links=('pk',)
    ##campos para editar desde ahi
    #list_editable =('telefono','nombre')
    ##para realizar busqueda
    #search_fields= ('user__email','user__username','telefono')
    ##filtros
    #list_filter=('created_at','updated_at','user__is_active','user__is_staff')