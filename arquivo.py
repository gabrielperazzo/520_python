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

    def escrever(self,s):
        self.arquivo.close()
        self.arquivo = open(self.nome, 'a')
        self.arquivo.write(s + '\n')

#arquivo = Arquivo('usuarios.csv')
#print(arquivo.nome, arquivo.linhas)
#print(arquivo.ler(12))
#arquivo.escrever('5,Dragonfly')

#letras = Arquivo('letras.txt')
#print(letras.nome, letras.linhas)