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


@admin.register(Servico)

class Servico(admin.ModelAdmin):
    list_display = ('id', 'tipo_plano', 'sla', 'preco', 'empresa_cnpj', 'plano_id', 'plano_empresa_cnpj')


@admin.register(Setor)

class Setor(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(Pessoa)

class Pessoa(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'cargo', 'email', 'telefone', 'setor_id')


@admin.register(Endereco)

class Endereco(admin.ModelAdmin):
    list_display = ('id', 'estado', 'cidade', 'bairro', 'empresa_cnpj', 'pessoa_cpf')

# Register your models here.
