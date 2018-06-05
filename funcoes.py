#!/usr/bin/python3

def nomeados(a, b='dois', c='tres'):
    print(a, b, c)

nomeados('um', b='quatro', c='cinco')

def args(*a):
    print(a[5])

def kwargs(**k):
    print(k)

#args(1,2,3,4,5,6,7,8,9,0)

kwargs(h='hector', d='danilo', t='thais', b='bruna', j='joyce')