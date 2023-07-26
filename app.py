import matplotlib
matplotlib.use('Agg')

from flask import Flask, render_template, send_file
import pandas as pd
import psycopg2
import json
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

def get_data_from_postgres():
    # Substitua este código pelo código real para buscar os dados do PostgreSQL
    # Certifique-se de que o DataFrame retornado tenha as colunas 'gender' e 'age'
    data = {
        'gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'age': [30, 25, 35, 28, 40]
    }
    df = pd.DataFrame(data)
    return df

@app.route('/')
def index():
    # Obter os dados do PostgreSQL
    df = get_data_from_postgres()

    # Plotar o gráfico de dispersão (gender vs age)
    plt.figure(figsize=(8, 6))
    plt.scatter(df['gender'], df['age'])
    plt.xlabel('Gênero')
    plt.ylabel('Idade')
    plt.title('Relação entre Gênero e Idade')

    # Salvar o gráfico como uma imagem em memória
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Renderizar o template HTML passando os dados da imagem
    return render_template('dashboard.html', chart_data=json.dumps(df.to_dict(orient='records')), image=buffer.getvalue())

if __name__ == '__main__':
    app.run(debug=True)
