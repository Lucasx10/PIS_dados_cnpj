from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Busca, Socio, SituacaoCadastral, Cnae, Estabelecimento, Empresa
from django.db.models import Avg, Count, DateField
from django.db.models.functions import TruncMonth, Cast

def home(request):
    count = Busca.objects.count()
    media = Busca.objects.aggregate(Avg('vl_capital_social'))['vl_capital_social__avg']
    
    # Calcular a porcentagem de cada UF
    total_count = Busca.objects.count()
    uf_counts = Busca.objects.values('st_uf').annotate(count=Count('st_uf'))
    uf_percentages = [
        {'uf': uf['st_uf'], 'percentage': (uf['count'] / total_count) * 100}
        for uf in uf_counts
    ]
    
    # Buscar o CNAE principal mais listado
    cnae_principal_mais_listado = Busca.objects.values('cnae_principal').annotate(count=Count('cnae_principal')).order_by('-count').first()
    cnae_mais_listado = cnae_principal_mais_listado['cnae_principal'] if cnae_principal_mais_listado else 'N/A'

    # Passar a contagem, a média, as porcentagens e o CNAE para o template
    context = {
        'row_count': count,
        'media': media,
        'uf_percentages': uf_percentages,
        'cnae_mais_listado': cnae_mais_listado
    }
    
    return render(request, 'dashboard.html', context)


def relatorio_uf(request):
    # Conta o número de vezes que cada UF aparece
    uf_counts = Busca.objects.values('st_uf').annotate(count=Count('st_uf')).order_by('st_uf')

    labels = []
    data = []

    for uf_count in uf_counts:
        labels.append(uf_count['st_uf'])
        data.append(uf_count['count'])

    return JsonResponse({'labels': labels, 'data': data})

def relatorio_data(request):
    dados = Busca.objects.annotate(
        month=TruncMonth(Cast('dt_inicio_atividade', output_field=DateField()))
    ).values('month').annotate(count=Count('id')).order_by('month')

    labels = [item['month'].strftime('%Y-%m') for item in dados]
    data = [item['count'] for item in dados]

    return JsonResponse({'labels': labels, 'data': data})

def buscar_socio(request):
    mensagem = ''
    if request.method == 'POST':
        nome = request.POST.get('nome', '')
        cpf = request.POST.get('cpf', '')
        cnpj_base_query = Socio.objects.filter(st_nome=nome, st_cpf_cnpj=cpf).values_list('st_cnpj_base', flat=True)
        
        resultado = None
        
        if cnpj_base_query:
            cnpj_base = cnpj_base_query[0]
            estabelecimento = Estabelecimento.objects.filter(st_cnpj_base=cnpj_base).values_list('cd_motivo_situacao_cadastral', 'cd_cnae_principal', 'dt_inicio_atividade', 'st_uf')
            
            if estabelecimento:
                cd_motivo_situacao_cadastral = estabelecimento[0][0]
                cd_cnae_principal = estabelecimento[0][1]
                dt_inicio_atividade = estabelecimento[0][2]
                st_uf = estabelecimento[0][3]
                
                motivo_situacao_cadastral = SituacaoCadastral.objects.filter(cd_motivo_situacao_cadastral=cd_motivo_situacao_cadastral).values_list('st_motivo_situacao_cadastral', flat=True)
                cnae_principal = Cnae.objects.filter(cd_cnae=cd_cnae_principal).values_list('st_cnae', flat=True)
                
                motivo_situacao_cadastral = motivo_situacao_cadastral[0] if motivo_situacao_cadastral else None
                cnae_principal = cnae_principal[0] if cnae_principal else None
                
                empresa = Empresa.objects.filter(st_cnpj_base=cnpj_base).values_list('st_razao_social', 'vl_capital_social')

                if empresa:
                    st_razao_social = empresa[0][0]
                    vl_capital_social_str = empresa[0][1]
                    if vl_capital_social_str:
                        vl_capital_social_str = vl_capital_social_str.replace('.', '').replace(',', '.')
                        vl_capital_social = float(vl_capital_social_str)
                    else:
                        vl_capital_social = 0.0
                else:
                    st_razao_social = 'S/N'
                    vl_capital_social = 0.0
                
                busca_existente = Busca.objects.filter(nome=nome, cpf=cpf).exists()
                
                resultado = {
                    'nome': nome,
                    'cpf': cpf,
                    'cnpj_base': cnpj_base,
                    'st_nome_fantasia': st_razao_social,
                    'cd_motivo_situacao_cadastral': motivo_situacao_cadastral,
                    'cd_cnae_principal': cnae_principal,
                    'dt_inicio_atividade': dt_inicio_atividade,
                    'st_uf': st_uf,
                    'vl_capital_social': vl_capital_social,
                    'busca_existente': busca_existente
                }
        
        if not resultado:
            mensagem = 'Nenhum resultado encontrado.'

        return render(request, 'search.html', {'resultado': resultado, 'mensagem': mensagem})
    
    return render(request, 'search.html')


def salvar_busca(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        cnpj_base = request.POST.get('cnpj_base')
        st_nome_fantasia = request.POST.get('st_nome_fantasia')
        cd_motivo_situacao_cadastral = request.POST.get('cd_motivo_situacao_cadastral')
        cd_cnae_principal = request.POST.get('cd_cnae_principal')
        dt_inicio_atividade = request.POST.get('dt_inicio_atividade')
        st_uf = request.POST.get('st_uf')
        vl_capital_social_str = request.POST.get('vl_capital_social')
        
        if vl_capital_social_str:
            # Substituir vírgula por ponto
            vl_capital_social_str = vl_capital_social_str.replace(',', '.')
            try:
                vl_capital_social = float(vl_capital_social_str)
            except ValueError:
                vl_capital_social = 0.0
        else:
            vl_capital_social = 0.0
        
        
        busca = Busca.objects.create(
            nome=nome, cpf=cpf, cnpj_base=cnpj_base,
            nome_fantasia=st_nome_fantasia, motivo_situacao_cadastral=cd_motivo_situacao_cadastral,
            cnae_principal=cd_cnae_principal, dt_inicio_atividade=dt_inicio_atividade, st_uf=st_uf,
            vl_capital_social=vl_capital_social
        )
        busca.save()
        
        return redirect('buscar_socio')

def tabela_socios(request):
    socios = Busca.objects.all()  # Obtém todos os sócios da tabela
    return render(request, 'table.html', {'socios': socios})
