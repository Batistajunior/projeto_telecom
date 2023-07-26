#Projeto Telecom - Análise de Dados

Este projeto tem o objetivo de realizar a análise de dados de uma empresa de telecomunicações utilizando a ferramenta Pentaho para a extração, transformação e carregamento (ETL) dos dados a partir de um arquivo CSV e a criação de dashboards com gráficos em Flash para visualização dos resultados.


Configuração do Ambiente

Antes de iniciar o projeto, é necessário ter as seguintes ferramentas e bibliotecas instaladas:

PostgreSQL: Banco de dados relacional para armazenar os dados de telecomunicações.
Pentaho Data Integration (PDI): Ferramenta de ETL para transformação dos dados.
Pentaho BI Server: Ferramenta para criação dos dashboards com gráficos em Flash.
Python 3: Linguagem de programação para execução de scripts e análises adicionais.
Flask: Framework para desenvolvimento da aplicação web para exibição dos dashboards.

Configuração da Base de Dados

Crie uma base de dados no PostgreSQL para armazenar os dados de telecomunicações.
Importe o arquivo CSV contendo os dados de telecomunicações para uma tabela no PostgreSQL.


Configuração do Pentaho Data Integration (PDI)

Abra o Pentaho Data Integration (PDI) e crie uma nova transformação.
Adicione um nó "CSV File Input" e configure-o para ler o arquivo CSV contendo os dados de telecomunicações.
Adicione os passos de transformação necessários (por exemplo, seleção de colunas, limpeza de dados) para preparar os dados para a análise.
Adicione um nó "Table Output" e configure-o para escrever os dados transformados na tabela do PostgreSQL.
Salve a transformação.


Configuração do Pentaho BI Server

Abra o Pentaho BI Server e crie um novo dashboard.
Adicione os gráficos em Flash desejados (por exemplo, gráfico de barras, gráfico de pizza) para visualizar os dados de telecomunicações.
Conecte os gráficos ao banco de dados PostgreSQL criando consultas SQL para extrair os dados relevantes.
Salve o dashboard.




Configuração do Flask e Dashboards Web

No diretório do projeto, crie um ambiente virtual Python usando o comando:

python3 -m venv venv


ive o ambiente virtual usando o comando:

source venv/bin/activate



Instale as bibliotecas Flask e psycopg2 usando o comando:

pip install Flask psycopg2



No diretório do projeto, crie um arquivo "app.py" contendo o código do servidor Flask para exibir os dashboards:



# Importe as bibliotecas necessárias

from flask import Flask, render_template, send_file
import io
import psycopg2

app = Flask(__name__)

# Defina as rotas para os dashboards

@app.route('/')
def index():
    # Código para executar o Pentaho BI Server e mostrar o dashboard Flash
    # ...

# Inicie o servidor Flask

if __name__ == '__main__':
    app.run(debug=True)



Execute o servidor Flask usando o comando:

python3 app.py


Acesse o dashboard no navegador usando o endereço "http://127.0.0.1:5000".






