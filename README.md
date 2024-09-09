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
