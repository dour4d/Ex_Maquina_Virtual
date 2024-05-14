from flask import Flask, render_template, request, redirect, url_for
from fastapi import FastAPI
class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

carro1 = Carro('azul', 'fusca', '1990')
lista = [carro1]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='listagem de carro', carros=lista )

@app.route('/novo')
def novo():
    return render_template('cad.html', titulo='Cadrastro de carros')

@app.route('/criar', methods=['POST',])
def criar():
    cor = request.form['cor']
    modelo = request.form['modelo']
    ano = request.form['ano']
    carro = Carro(cor, modelo, ano)
    lista.append(carro)
    return redirect(url_for('index'))

app.run(debug=True)