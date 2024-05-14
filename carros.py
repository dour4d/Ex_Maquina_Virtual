from flask import Flask, render_template, request, redirect, url_for, session, flash

class User:
    def __init__(self,nome,senha):
        self.nome = nome
        self.senha = senha

user1 = User('nath','123')
user2 = User('carol', '321')
users = {
    user1.nome : user1,
    user2.nome : user2
}
class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

carro1 = Carro('azul', 'fusca', '1990')
lista = [carro1]

app = Flask(__name__)
app.secret_key = 'secret123'

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

          
@app.route('/')
def index():
    return render_template('lista.html', titulo='listagem de carro', carros=lista )

@app.route('/novo')
def novo():
    if 'userLogado' not in session or session['userLogado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('cad.html', titulo='Cadrastro de carros')

@app.route('/criar', methods=['POST',])
def criar():
    cor = request.form['cor']
    modelo = request.form['modelo']
    ano = request.form['ano']
    carro = Carro(cor, modelo, ano)
    lista.append(carro)
    return redirect(url_for('index'))


@app.route('/authentic', methods=['POST'])
def authentic():
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    if nome in users:
        user_obj = users[nome]
        if senha == user_obj.senha:
            session['userLogado'] = user_obj.nome
            flash(user_obj.nome + ' logado com sucesso!')
            proximaPagina = request.form.get('proxima')
            if proximaPagina:
                return redirect(proximaPagina)
            else:
                return redirect(url_for('index'))
        else:
            flash('Senha incorreta')
    else:
        flash('Usuario não encontrado')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['userLogado'] = None
    flash('logout efetuado com sucesso!')
    return redirect(url_for('index'))


app.run(debug=True)