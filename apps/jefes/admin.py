from django.contrib import admin
from apps.jefes.models import Jefes


@admin.register(Jefes)
class JefesAdmin(admin.ModelAdmin):
    """Usuario admin"""
    #campos a mostrar
    list_display = ('pk','cuig','renspa') # mostrame estos datos
    ##links
    list_display_links=('pk',)
    ##campos para editar desde ahi
    #list_editable =('telefono','nombre')
    ##para realizar busqueda
    #search_fields= ('user__email','user__username','telefono')
    ##filtros
    #list_filter=('created_at','updated_at','user__is_active','user__is_staff')