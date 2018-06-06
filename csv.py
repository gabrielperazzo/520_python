#!/usr/bin/python3

from arquivo import Arquivo

class CSV(Arquivo):
    
    def __init__(self, nome):
        if not nome.lower().endswith('.csv'):
            print('O arquivo não é . csv')
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
        super(CSV, self).escrever('{0},{1}'.format(s[0],s[1]))
        
csv = CSV('usuarios.csv')
csv.escrever((66, 'kingsman'))
#print(csv.ler(5))