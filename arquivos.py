#!/usr/bin/python3

import random

f = open('usuarios.csv' , 'a')
#linhas = f.readlines()
#f.close

nome = input('Digite um nome: ')
f.write(str(random.randint(0,100)) + ',' + nome + '\n')
