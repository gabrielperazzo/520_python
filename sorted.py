#!/usr/bin/python3

f = open('usuarios.csv', 'r')
usuarios = [u.strip().split(',') for u in f.readlines()]
f.close()

def ordenar_pelo_id(u):
    u[0] = int(u[0])
    return u

for u in sorted(usuarios, key=ordenar_pelo_id):
    print(u)

exit()

f = open('usuarios.csv' , 'r')
linhas = f.readlines()
f.close()

usuarios = []
for l in sorted(linhas):
    usuarios.append(l.strip().split(','))
    print(usuarios)
