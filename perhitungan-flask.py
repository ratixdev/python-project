from flask import flask

app = flask(__name__)

@app.route("/")
def index():
    return ("index.html")

@app.route('/penjumlahan/<int:input1>/<int:input2>')
def penjumlahan(input1,input2):
    return 'Hasil dari {} + {} adalah {}'. format(input1,input2,(input1+input2))

@app.route('/pengurangan/<int:input1>/<int:input2>')
def pengurangan(input1,input2):
    return 'Hasil dari {} - {} adalah {}'. format(input1,input2,(input1-input2))

@app.route('/perkalian/<int:input1>/<int:input2>')
def perkalian(input1,input2):
    return 'Hasil dari {} x {} adalah {}'. format(input1,input2,(input1*input2))

@app.route('/pembagian/<int:input1>/<int:input2>')
def pembagian(input1,input2):
    return 'Hasil dari {} / {} adalah {}'. format(input1,input2,(input1/input2))