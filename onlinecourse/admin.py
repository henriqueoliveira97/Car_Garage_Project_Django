from django.contrib import admin
from .models import Mecanico, Cliente, Vendedor, Viatura, Reparacao, Peca, PecaReparacao, Administrativo

from django.contrib import admin
from .models import (
    Mecanico, Cliente, Vendedor, Viatura, Reparacao,
    Peca, PecaReparacao, Administrativo
)

class PecaReparacaoInline(admin.StackedInline):
    model = PecaReparacao
    extra = 1

@admin.register(Reparacao)
class ReparacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'viatura', 'mecanico', 'status', 'custo_total')
    search_fields = ('descricao', 'viatura__marca', 'viatura__modelo')
    list_filter = ('status', 'mecanico', 'viatura')
    inlines = [PecaReparacaoInline]

class ReparacaoInline(admin.StackedInline):
    model = Reparacao
    extra = 0

@admin.register(Viatura)
class ViaturaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'mecanico')
    search_fields = ('marca', 'modelo')
    list_filter = ('marca', 'tipo')
    inlines = [ReparacaoInline]

@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_time')
    list_filter = ('full_time',)

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_sales')

@admin.register(Administrativo)
class AdministrativoAdmin(admin.ModelAdmin):
    list_display = ('user', 'occupation')
    list_filter = ('occupation',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_time', 'conta')
    list_filter = ('first_time',)

@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'custo_unitario')
    search_fields = ('nome',)

