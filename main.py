from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)#Criando o site (app = uma instancia da classe Flask) de modo padrão do flask.

@app.route('/')#Route é o link da pág. (No caso Pagina inicial, por isso está em branco)
def rensbr():
    return render_template('rensbr.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/certificados')
def certificados():
    return render_template('certificados.html')

@app.route('/dash_pagamentos')
def dash_pagamentos():
    return render_template('dash_pagamentos.html')

@app.route('/dash_estoque')
def dash_estoque():
    return render_template('dash_estoque.html')

@app.route('/dash_projeto1')
def dash_projeto1():
    return render_template('dash_projeto1.html')

@app.route('/autom_conferir_fechamento')
def autom_conferir_fechamento():
    return render_template('autom_conferir_fechamento.html')

@app.route('/calculadora_de_juros')
def calculadora_de_juros():
    return render_template('calculadora_de_juros.html')
@app.route('/download_calculadora', endpoint='download_calculadora')#Não tem arq html. É um arquivo para download.
def download_calculadora():
    return send_from_directory('static', 'calculadora_de_juros/dist_Calc.zip', as_attachment=True)

@app.route('/este_site')
def este_site():
    return render_template('este_site.html')

@app.route('/lista_python')#Testando python no html, página está criada mas não vai aparecer.
def lista_python():
    lista = [1,2,3,4,5,6,7,8,9,10]
    return render_template('lista_python.html', lista = lista)

if __name__ == '__main__':
    app.run(debug=True)

