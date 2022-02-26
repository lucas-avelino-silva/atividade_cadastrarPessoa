from http.client import responses
import os
from flask import Flask, jsonify, request, render_template



app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    return render_template('index.html')


@app.route("/enviar", methods=["POST", "GET"])
def retornar():
    nome = request.form["nome"]
    email = request.form["email"]
    senha = request.form["senha"]
    
    return str(nome)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)