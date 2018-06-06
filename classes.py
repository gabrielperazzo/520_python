#!/usr/bin/python3

class Arquivo:

    def __init__(self, nome):
        self.nome = nome
        self.arquivo = open(nome, 'r')
        self.linhas = len(self.arquivo.readlines())
        self.arquivo.seek(0)

    def ler(self, n):
        for i, l in enumerate(self.arquivo, start=1):
            if i == n:
                return l.strip()

arquivo = Arquivo('usuarios.csv')
letras = Arquivo('letras.txt')
print(arquivo.nome, arquivo.linhas)
print(letras.nome, letras.linhas)
print(arquivo.ler(12))