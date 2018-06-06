#!/usr/bin/python3

def minusculizar(i):
    return i.lower()

lista = ['a','A','B','C','D']
print(lista)
print(sorted(lista))
print(sorted(lista, key=minusculizar))

f = open('usuarios.csv', 'r')
usuarios = [u.strip().split(',') for u in f.readlines()]
f.close()

def ordenar_pelo_nome(i):
    i[1] = str(i[1])
    return i[1].lower()

for u in sorted(usuarios, key=ordenar_pelo_nome):
    print(u)

exit()

f = open('usuarios.csv' , 'r')
linhas = f.readlines()
f.close()

usuarios = []
for l in sorted(linhas):
    usuarios.append(l.strip().split(','))
    print(usuarios)
