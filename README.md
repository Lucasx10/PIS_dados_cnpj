# Projeto - Sistema para acompanhamento de inserção de alunos egressos que empreenderam

O projeto consiste em:
- Um script Python para baixar dados de CNPJs.
- Uma aplicação Django para acessar e gerenciar esses dados.
- Um banco de dados PostgreSQL para armazenar as informações.

## Instalação

### Requisitos

- Python 3.x
- PostgreSQL
- pip
- Git

## Explicação do projeto
- **[script_cnpj_postgres.py](https://github.com/Lucasx10/PIS_dados_cnpj/blob/main/script/script_cnpj_postgres.py)**

    #### Carregar variáveis de ambiente:

    ```python
        ENV_PATH = os.path.join(os.path.dirname(__file__), '..', '.env')
        config = Config(RepositoryEnv(ENV_PATH))
    ```
O código carrega variáveis do arquivo .env para definir credenciais do banco de dados.


`get_latest_url()`: 
1. Busca a última URL no 'http://200.152.38.155/CNPJ/dados_abertos_cnpj/', Faz scraping da página de dados abertos e encontra o link mais recente de arquivos disponíveis para download.

2. Faz uma requisição HTTP à URL base e lê o conteúdo HTML da página para extrair uma tabela de links para arquivos .zip.

3. O DataFrame resultante é filtrado para incluir apenas arquivos .zip.

`create_table()`: Cria uma tabela no banco de dados
Verifica se a tabela já existe e, se não, cria uma nova tabela baseada nos layouts definidos.

### Passos

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Lucasx10/PIS_dados_cnpj.git
   cd PIS_dados_cnpj
    ```
2. **Crie e ative um ambiente virtual:**


    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Windows use: venv\Scripts\activate
    ```
3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```
4. **Configure o PostgreSQL:**

    - Crie um banco de dados PostgreSQL.
    - Atualize as configurações do banco de dados no arquivo `.env`

Exemplo de configuração no [`.env.example`](https://github.com/Lucasx10/PIS_dados_cnpj/blob/main/.env.example):


## Configuração

### Script para Baixar Dados

1. **Execute o script para baixar e armazenar CNPJs:**

    ```bash
    cd script/
    python script_cnpj_postgres.py
    ```

Script em python irá carregar os arquivos de cnpj dos dados públicos da Receita Federal no banco de dados PostgreSQL configurado. (Ele demora um pouco)

2. **Execute as migrações do Django:**

    ```bash
    cd ..
    cd projeto_cnpj/
    python manage.py migrate
    ```

## Uso

- **Inicie o servidor Django:**
    
    ```bash
    python manage.py runserver
    ```

Acesse a aplicação em: http://127.0.0.1:8000
