#!/usr/bin/python3

class Arquivo:

    def __init__(self, nome):
        self.nome = nome
        self.arquivo = open(nome, 'r')
        self.linhas = len(self.arquivo.readlines())

a = Arquivo
print(a)
