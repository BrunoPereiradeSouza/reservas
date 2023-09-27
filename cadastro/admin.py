from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('CNPJ', 'nome_empresa', 'categoria_empresa', 'quitado', 'stand', 'data')

@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    list_display = ('localizacao', 'valor')
