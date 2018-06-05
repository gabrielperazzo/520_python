#!/usr/bin/python3

#def nomeados(a, b='dois', c='tres'):
#   print(a, b, c)

#nomeados('um', b='quatro', c='cinco')

def args(*a):
    print(a)

def kwargs(**k):
    print(k)

def ambos(*a, **k):
    print(a)
    print(k)

tupla = ('Hector' , '123' , '554322', 'hector.vido')
#a, *b, c = tupla
#print(a, c)

lista = ['Gatinho', 'Cachorrinho', 'Patinho', 'Leãozinho']
def escopo():
    #lista = ['Rosinha', 'Copo-de-leitinho', 'Dente-de-leaozinho']
    lista.append('Jacarezinho')
    print(lista)

def externa():
    print('TEste')
    def interna():
        print('Priiiishhh')
    return interna

externa()()
    
#args(1,2,3,4,5,6,7,8,9,0)

#kwargs(h='hector', d='danilo', t='thais', b='bruna', j='joyce')