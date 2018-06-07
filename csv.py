#!/usr/bin/python3

from arquivo import Arquivo

class CSV(Arquivo):
    
    def __init__(self, nome):
        if not nome.lower().endswith('.csv'):
           print('O arquivo não é .csv')
           return
        else:
           super(CSV, self).__init__(nome)

    def escrever(self, s):
        if type(s) is not tuple:
            print('s não é tupla -> ()')
            return
        if len(s) != 2:
            print('A tupla deve ter dois valores')
            return
        if type(s[0]) is not int:
            print('s[0] não é inteiro')
            return
        if not s[1].strip():
            print('s[1] não pode ser vazio')
            return
        super(CSV, self).escrever('{0},{1}'.format(s[0],s[1]))

    def __str__(self):
        return '{0} - {1} lines'.format(self.nome, self.linhas)

    def __getitem__(self, i):
        if type(i) is int:
            return self.ler(i)
        i = i.lower()
        return [l.strip() for l in self.arquivo if i in l.lower()]

csv = CSV('usuarios.csv')
#csv.escrever((99, 'Boleslau'))
#print(csv.ler(5))
print(csv['BOLESLAU'])