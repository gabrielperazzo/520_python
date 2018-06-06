#!/usr/bin/python3

def minusculizar(i):
    return i.lower()

lista = ['a','A','B','C','D']
print(lista)
print(sorted(lista))
print(sorted(lista, key=minusculizar))

f = open('usuarios.csv', 'r')
usuarios = [l for l in [u.strip().split(',') for u in f.readlines()] if l[1].lower().startswith('a')] 
f.close()

def ordenar_pelo_nome(i):
    i[1] = str(i[1])
    return i[1].lower()

for u in sorted(usuarios, key=lambda i : i[1].lower()):
    print(u)

exit()

f = open('usuarios.csv' , 'r')
linhas = f.readlines()
f.close()

usuarios = []
for l in sorted(linhas):
    usuarios.append(l.strip().split(','))
    print(usuarios)
