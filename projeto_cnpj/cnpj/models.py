from django.db import models

class Socio(models.Model):
    st_nome = models.CharField(max_length=255)
    st_cpf_cnpj = models.CharField(max_length=14)
    st_cnpj_base = models.CharField(max_length=20)
    
    class Meta:
        managed = False  # Não gerenciar automaticamente esta tabela
        db_table = 'tb_socio'  

class Busca(models.Model):
    CURSO_CHOICES = (
        ('CC', "Ciencia da computacaoo"),
        ('LI', "Licenciatura em informatica"),
    )
    
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    cnpj_base = models.CharField(max_length=20, blank=True, null=True)
    nome_fantasia = models.CharField(max_length=100, blank=True, null=True)
    motivo_situacao_cadastral = models.CharField(max_length=100, blank=True, null=True)
    cnae_principal = models.CharField(max_length=100, blank=True, null=True)
    dt_inicio_atividade = models.CharField(blank=True, null=True)
    vl_capital_social = models.FloatField(blank=True, null=True)
    st_uf = models.CharField(max_length=2, blank=True, null=True)
    curso = models.CharField(max_length=2, choices=CURSO_CHOICES, default='CC')
    
class Estabelecimento(models.Model):
    st_nome_fantasia = models.CharField(max_length=200, blank=True, null=True)
    st_cnpj_base = models.CharField(max_length=20)
    cd_motivo_situacao_cadastral = models.CharField(max_length=50, blank=True, null=True)
    cd_cnae_principal = models.CharField(max_length=50, blank=True, null=True)
    dt_inicio_atividade = models.CharField(blank=True, null=True)
    st_uf = models.CharField(max_length=2, blank=True, null=True)
    
    class Meta:
        managed = False 
        db_table = 'tb_estabelecimento'
        
class Empresa(models.Model):
    st_cnpj_base = models.CharField(max_length=20)
    st_razao_social = models.CharField(max_length=200, blank=True, null=True)
    vl_capital_social = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        managed = False 
        db_table = 'tb_empresa'

class SituacaoCadastral(models.Model):
    cd_motivo_situacao_cadastral = models.CharField(max_length=255)
    st_motivo_situacao_cadastral = models.CharField(max_length=255)
    
    class Meta:
        managed = False 
        db_table = 'tb_motivo_situacao_cadastral'
        
class Cnae(models.Model):
    cd_cnae = models.CharField(max_length=255)
    st_cnae = models.CharField(max_length=255)
    
    class Meta:
        managed = False  
        db_table = 'tb_cnae'
  