#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1 style="font-family: sans-serif">FLASK!</h1>'

@app.route('/local/<int:i>')
@app.route('/local/')
def local(i):
    print('Acessaram aqui...')
    return '<h1>0 parâmetro é: {0}</h1>'.format(i)

app.run()