#!/usr/bin/python3

from subprocess import run, PIPE

cmd = run(['ls','-l'], stdout=PIPE)

f = input('Digite o nome do arquivo: ')
files = cmd.stdout.decode('utf-8').split('\n')

for i in files:
    if f in i:
        print(i)
        break
else:
    print('Arquivo não encontrado')