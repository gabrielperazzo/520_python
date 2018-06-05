#!/usr/bin/python3

import random

f = open('usuarios.csv' , 'r')
linhas = f.readlines()
f.close()

if ',' in linhas[0]:
    print('O banco de dados já está atualizado')
    exit()
    
f = open('usuarios.csv' , 'w')
for l in linhas:
    f.write('{0},{1}'.format(random.randint(0,100),l))

f.close()
