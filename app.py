from http.client import responses
import os
from flask import Flask, jsonify, request, render_template
from flaskext.mysql import MySQL


app = Flask(__name__)


# Estou configurando o banco

mysql = MySQL()


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'db_atividade'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)


@app.route("/", methods=["GET"])
def main():
    return render_template('index.html')


@app.route("/enviar", methods=["POST", "GET"])
def retornar():
    nome = request.form["nome"]
    email = request.form["email"]
    endereco = request.form["endereco"]
    if nome and email and endereco:
        conexao = mysql.connect()
        cursor = conexao.curso()
        cursor.execute('INSERT INTO usuario (nome, email, endereco) VALUES (%s, %s, %s)', (nome, email, endereco))
        conexao.commit()
        cadastrado = f"O {nome} foi cadastrado com sucesso :)"
        return cadastrado
        #return str(nome)


# rota de listagem dos cadastros

@app.route("/listar", methods=["POST", "GET"])
def listar_pessoas():
    conexao = mysql.connect()
    cursor = conexao.cursor()
    cursor.execute('SELECT nome FROM usuario')
    data = cursor.fetchall()
    #for x in range(len(data)):
        #print(data[x])
    conexao.commit()
    return render_template('pessoas.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)
