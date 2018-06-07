#!/usr/bin/python3

class Arquivo:

    def __init__(self, nome):
        self.nome = nome
        self.arquivo = open(nome, 'r')
        self.linhas = len(self.arquivo.readlines())
        self.arquivo.seek(0)

    def ler(self, n): #n é a linha que eu quero printar, 3
        self.reabrir('r')
        for i, l in enumerate(self.arquivo, start=1):
            if i == n:
                return l.strip()

    def escrever(self, s): #1,Nome
        self.reabrir('a')
        self.arquivo.write(s + '\n')
        self.linhas += 1

    def reabrir(self, m):
        if m == self.arquivo.mode:
            if self.arquivo.mode == 'r':
                self.arquivo.seek(0)
        else:
            self.arquivo.close()
            self.arquivo = open(self.nome, m)