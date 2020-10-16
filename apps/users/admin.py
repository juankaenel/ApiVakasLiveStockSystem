from django.contrib import admin
from apps.users.models import PerfilUsuario


@admin.register(PerfilUsuario)
class PerfilUsuario(admin.ModelAdmin):
    """Perfil admin"""
    #campos a mostrar
    list_display = ('pk','nombre','dni','telefono') # mostrame estos datos
    ##links
    list_display_links=('pk',)
    ##campos para editar desde ahi
    list_editable =('telefono','nombre')
    ##para realizar busqueda
    search_fields= ('user__email','user__username','telefono')
    ##filtros
    list_filter=('created_at','updated_at','user__is_active','user__is_staff')