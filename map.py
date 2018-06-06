#!/usr/bin/python3

import random

sobrenomes = ['Silva', 'Santos', 'Costa', 'Souza', 'Jacinto']

f = open('usuarios.csv', 'r')
usuarios = [u.strip().split(',') for u in f.readlines()]

def to_dict(i):
    dic = {"id" : i[0]} 
    dic["nome"] = i[1]
    dic["sobrenome"] = random.choice(sobrenomes)
    return dic

#def add_sobrenome(i):
#    i.append(random.choice(sobrenomes))
#    return i

usuarios = list(map(to_dict, usuarios))

for i in sorted(usuarios, key=lambda u : u['sobrenome']):
    print(i)