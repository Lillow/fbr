from django.db import models

class Empresa(models.Model):
    cnpj = models.CharField(max_length = 18, unique = True, primary_key=True)
    name = models.CharField(max_length = 45)
    razao_social = models.CharField(max_length = 45)
    sede = models.CharField(max_length = 45)
    estado = models.CharField(max_length = 45)
    ranking = models.CharField(max_length = 45)

    class meta():
        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'
    def __str__(self):
        return self.cnpj

class Area_cobertura(models.Model):
    id = models.IntegerField(unique = True, primary_key=True)
    tecnologias = models.CharField(max_length = 45)

class empresa_area_cobertura(models.Model):
    empresa_cnpj = models.ForeignKey(Empresa, related_name='area_empresa_cnpj', on_delete= models.CASCADE)
    area_cobertura_id = models.ForeignKey(Area_cobertura, related_name='area_cobertura_id', on_delete=models.CASCADE)

class Plano(models.Model):
    id = models.IntegerField(unique = True ,primary_key=True)
    banda = models.CharField(max_length = 45)
    empresa_cnpj = models.ForeignKey(Empresa, related_name='plano_empresa_cnpj', on_delete= models.CASCADE)

class Infraestrutura(models.Model):
    id = models.IntegerField(unique = True, primary_key=True)
    asn = models.CharField(max_length = 45)
    ptt = models.CharField(max_length = 45)
    bgp = models.CharField(max_length = 45)
    operadora_backbone = models.CharField(max_length = 45)
    capacidade_backbone = models.CharField(max_length = 45)
    empresa_cnpj = models.ForeignKey(Empresa, related_name = 'infra_empresa_cnpj', on_delete= models.CASCADE)

class Servico(models.Model):
    id = models.IntegerField(unique = True, primary_key=True)
    tipo_plano = models.CharField(max_length = 45)
    sla = models.CharField(max_length = 45)
    preco = models.IntegerField()
    empresa_cnpj = models.ForeignKey(Empresa, related_name = 'servico_empresa_cnpj', on_delete= models.CASCADE)
    plano_id = models.ForeignKey(Plano, related_name = 'servico_plano_id', on_delete= models.CASCADE)
    plano_empresa_cnpj = models.ForeignKey(Plano, related_name='servico_plano_empresa_cnpj', on_delete= models.CASCADE)

class Setor(models.Model):
    id = models.IntegerField(unique = True, primary_key=True)
    nome = models.CharField(max_length = 45)

class Pessoa(models.Model):
    cpf = models.CharField(max_length = 45, unique= True, primary_key=True)
    nome = models.CharField(max_length = 45)
    cargo = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    telefone = models.CharField(max_length = 45)
    setor_id = models.ForeignKey(Setor, related_name = 'pessoa_setor_id', on_delete= models.CASCADE) 

class Endereco(models.Model):
    id = models.IntegerField(unique = True, primary_key=True)
    estado = models.CharField(max_length = 45)
    cidade = models.CharField(max_length = 45)
    bairro = models.CharField(max_length = 45)
    empresa_cnpj = models.ForeignKey(Empresa, related_name='endereco_empresa_cnpj', on_delete= models.CASCADE)
    pessoa_cpf = models.ForeignKey(Pessoa, related_name='endereco_pessoa_cpf', on_delete= models.CASCADE)


# class Servidor(models.Model):
#     name = models.CharField()
#     class meta():
#         abstract = True

# class Backbone(Servidor):
#     provedor = models.TextField()

#     class Meta():
#         verbose_name = 'backbone'
#         verbose_name_plural = 'backbones'

#     def __str__(self):
#         return self.provedor

# class Dns(Servidor):
#     class Meta():
#         verbose_name = 'dns'
#         verbose_name_plural = 'dns'
# Create your models here.
