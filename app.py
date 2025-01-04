from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def primeira_pagina():
    return render_template("inicio.html")

@app.route('/imc', methods = ["post"])
def segunda_pagina():
    nome = request.form.get("nome")
    altura = float(request.form.get("altura"))
    peso = float(request.form.get("peso"))
    imc = round((peso/altura**2),2)
    return render_template("imc.html", nomeusuario = nome, imcusuario = imc)