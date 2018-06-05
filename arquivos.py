#!/usr/bin/python3

f = open('usuarios.csv' , 'r+')

for l in sorted(f.readlines(), reverse=True):
    print(l.title())

nome = input('Digite um nome: ')
f.write(nome + '\n')

