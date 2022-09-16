from django.contrib import admin
from .models import *

class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('id_persona', 'id_puesto',)
    list_filter=('id_puesto',)

class PersonasAdmin(admin.ModelAdmin):
    list_display=('nombre', 'apep', 'apem',)
    search_fields = ('nombre', 'apep', 'apem',)

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active', 'is_staff',)
    list_filter = ('is_active',)
    search_fields=('nombre',)

class usuarios_codigosAdmin(admin.ModelAdmin):
    list_display = ('codigo_reg','id_persona',)
    search_fields = ('codigo_reg','id_persona',)

admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(Personas, PersonasAdmin)
admin.site.register(Usuario, UsuariosAdmin)
admin.site.register(usuarios_codigos, usuarios_codigosAdmin)