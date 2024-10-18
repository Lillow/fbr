from django.db import models

class Empresa():
    cnpj = models.CharField(max_length = 18, unique = True)
    name = models.CharField(max_length = 45)
    razao_social = models.CharField(max_length = 45)
    sede = models.CharField(max_length = 45)
    estado = models.CharField(max_length = 45)
    ranking = models.CharField(max_length = 45)

class Area_cobertura():
    id = models.IntegerField
    tecnologias = models.CharField(max_length = 45)

class empresa_area_cobertura():
    empresa_cnpj = models.ForeignKey(Empresa, related_name='cnpj')
    area_cobertura_id = models.ForeignKey(Area_cobertura)

class Plano():
    id = models.IntegerField()
    banda = models.CharField(max_length = 45)
    empresa_cnpj = models.ForeignKey(Empresa, related_name='cnpj')

class Infraestrutura():
    id = models.IntegerField()
    asn = models.CharField(max_length = 45)
    ptt = models.CharField(max_length = 45)
    bgp = models.CharField(max_length = 45)
    operadora_backbone = models.CharField(max_length = 45)
    capacidade_backbone = models.CharField(max_length = 45)
    empresa_cnpj = models.ForeignKey(Empresa, related_name = 'cnpj')

class Servico():
    id = models.IntegerField()
    tipo_plano = models.CharField(max_length = 45)
    sla = models.CharField(max_length = 45)
    preco = models.IntegerField()
    empresa_cnpj = models.ForeignKey(Empresa, related_name = 'cnpj')
    plano_id = models.ForeignKey(Plano, related_name = 'id')
    plano_empresa_cnpj = models.ForeignKey(Plano, related_name='empresa_cnpj')

class Setor():
    id = models.IntegerField()
    nome = models.CharField(max_length = 45)

class Pessoa():
    cpf = models.CharField(max_length = 45)
    nome = models.CharField(max_length = 45)
    cargo = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    telefone = models.CharField(max_length = 45)
    setor_id = models.ForeignKey(Setor, related_name = 'id') 

class Endereco():
    id = models.IntegerField()
    estado = models.CharField(max_length = 45)
    cidade = models.CharField(max_length = 45)
    bairro = models.CharField(max_length = 45)
    empresa_cnpj = models.ForeignKey(Empresa, related_name='cnpj')
    pessoa_cpf = models.ForeignKey(Pessoa, related_name='cpf')


class Servidor(models.Model):
    name = models.CharField()
    class meta():
        abstract = True

class Backbone(Servidor):
    provedor = models.TextField()

    class Meta():
        verbose_name = 'backbone'
        verbose_name_plural = 'backbones'

    def __str__(self):
        return self.provedor

class Dns(Servidor):
    class Meta():
        verbose_name = 'dns'
        verbose_name_plural = 'dns'
# Create your models here.
