#!/usr/bin/python3

f = open('usuarios.csv' , 'r')
linhas = f.readlines()
f.close()

usuarios = []
for l in sorted(linhas):
    usuarios.append(l.strip().split(','))
    print(usuarios)

    