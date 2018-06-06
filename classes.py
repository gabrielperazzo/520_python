#!/usr/bin/python3

class Arquivo:

    def __init__(self, nome):
        self.nome = nome
        self.arquivo = open(nome, 'r')
        self.linhas = len(self.arquivo.readlines())

arquivo = Arquivo('usuarios.csv')
letras = Arquivo('letras.txt')
print(arquivo.nome, arquivo.linhas)
print(letras.nome, letras.linhas)