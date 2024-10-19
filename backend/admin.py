from django.contrib import admin
from .models import *

@admin.register(Empresa)

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('cnpj','name','razao_social','sede','estado','ranking')


@admin.register(Area_cobertura)

class AreaCoberturaAdmin(admin.ModelAdmin):
    list_display = ('id','tecnologias')


@admin.register(empresa_area_cobertura)

class empresaAreaCobertura(admin.ModelAdmin):
    list_display = ('empresa_cnpj', 'area_cobertura_id')


@admin.register(Plano)

class Plano(admin.ModelAdmin):
    list_display = ('id', 'banda', 'empresa_cnpj')


@admin.register(Infraestrutura)

class Infuraestrutura(admin.ModelAdmin):
    list_display = ('id', 'asn', 'ptt', 'bgp', 'operadora_backbone', 'capacidade_backbone', 'empresa_cnpj')





# Register your models here.
