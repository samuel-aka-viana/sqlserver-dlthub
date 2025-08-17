# SQLServer DLT Hub Connector

Este repositório demonstra como criar e usar um conector customizado para SQL Server no DLT Hub (Data Load Tools Hub) usando Python e ODBC.

## Visão Geral

O projeto inclui:

* **main.py**: Pipeline de exemplo que se conecta ao SQL Server, extrai dados e envia para o DLT Hub.
* **query\_duck.py**: Exemplo de extração de dados usando consultas SQL.
* **.dlt/**: Configurações de projeto DLT (p.ex., definições de streams e credenciais).
* **Dockerfile** & **docker-compose.yml**: Ambiente containerizado com UnixODBC e driver MSDTC.
* **requirements.txt**: Dependências Python (pyodbc, dlt, etc.).
* **test\_main.py**: Suite de testes unitários para validar a conexão e extração.

## Funcionalidades

* Conexão com instâncias Microsoft SQL Server via ODBC.
* Extração de dados incremental e full load em pipelines DLT.
* Configuração flexível de DSN e credenciais através de variáveis de ambiente.
* Contêiner Docker para facilitar testes e deploy em CI/CD.

## Pré-requisitos

* **Python 3.8+**
* **ODBC Driver** para SQL Server (msodbcsql17)
* **unixODBC-dev** (headers de desenvolvimento)
* **DLT CLI** instalado e configurado

## Instalação

```bash
# Adicionar repositório Microsoft e instalar driver
curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17
sudo apt-get install -y unixodbc-dev

# Clonar e instalar dependências Python
git clone https://github.com/samuel-aka-viana/sqlserver-dlthub.git
cd sqlserver-dlthub
pip install -r requirements.txt
```

## Configuração

Defina as seguintes variáveis de ambiente:

```bash
export SQLSERVER_HOST=<host>
export SQLSERVER_DB=<database>
export SQLSERVER_USER=<user>
export SQLSERVER_PASSWORD=<password>
export DLT_HUB_API_KEY=<seu_token_dlt>
```

## Uso

Para executar o pipeline DLT:

```bash
dlt pipeline init --template basic_sqlserver_connector
python main.py
```

Para testar localmente com Docker Compose:

```bash
docker-compose up --build -d
```

## Estrutura de Pastas

```
sqlserver-dlthub/
├── main.py               # Pipeline DLT de exemplo
├── query_duck.py         # Exemplo de consulta a SQL Server
├── .dlt/                 # Configurações DLT Hub
├── Dockerfile            # Imagem container com ODBC
├── docker-compose.yml    # Compose para testes locais
├── requirements.txt      # Dependências Python
└── test_main.py          # Testes unitários
```

## Testes

```bash
pytest test_main.py
```

## Contribuições

Contribuições são bem-vindas! Abra issues ou pull requests para melhorias.

## Licença

MIT © Samuel Viana
