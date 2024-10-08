# Generated by Django 5.0.1 on 2024-09-16 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cnae',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_cnae', models.CharField(max_length=255)),
                ('st_cnae', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tb_cnae',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_cnpj_base', models.CharField(max_length=20)),
                ('st_razao_social', models.CharField(blank=True, max_length=200, null=True)),
                ('vl_capital_social', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tb_empresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_nome_fantasia', models.CharField(blank=True, max_length=200, null=True)),
                ('st_cnpj_base', models.CharField(max_length=20)),
                ('cd_motivo_situacao_cadastral', models.CharField(blank=True, max_length=50, null=True)),
                ('cd_cnae_principal', models.CharField(blank=True, max_length=50, null=True)),
                ('dt_inicio_atividade', models.CharField(blank=True, null=True)),
                ('st_uf', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'tb_estabelecimento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SituacaoCadastral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_motivo_situacao_cadastral', models.CharField(max_length=255)),
                ('st_motivo_situacao_cadastral', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tb_motivo_situacao_cadastral',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_nome', models.CharField(max_length=255)),
                ('st_cpf_cnpj', models.CharField(max_length=14)),
                ('st_cnpj_base', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tb_socio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Busca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14)),
                ('cnpj_base', models.CharField(blank=True, max_length=20, null=True)),
                ('nome_fantasia', models.CharField(blank=True, max_length=100, null=True)),
                ('motivo_situacao_cadastral', models.CharField(blank=True, max_length=100, null=True)),
                ('cnae_principal', models.CharField(blank=True, max_length=100, null=True)),
                ('dt_inicio_atividade', models.CharField(blank=True, null=True)),
                ('vl_capital_social', models.FloatField(blank=True, null=True)),
                ('st_uf', models.CharField(blank=True, max_length=2, null=True)),
                ('curso', models.CharField(choices=[('CC', 'Ciencia da computacaoo'), ('LI', 'Licenciatura em informatica')], default='CC', max_length=2)),
            ],
            options={
                'db_table': 'cnpj_busca',
            },
        ),
    ]
