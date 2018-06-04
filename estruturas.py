#!/usr/bin/python3

nome_banda = input('Digite o nome de uma banda: ')
nome_musica = input('Digite o nome de uma música: ')

music = {"nome" : nome_banda , "musica" : nome_musica}
print(music["musica"])

exit()

novo_nome = input('Digite um novo nome: ')
nomes = ['Tricia', 'Maisa', 'Andreia']
nomes.append(novo_nome)
print(nomes)

exit()

nomes = 'abcdefghijklmnopqrs'
nome = input('Digite uma letra qualquer: ')

if nome.lower() in nomes:
    print('Achei o {0}'.format(nome))
else:
    print('Não achei o {0}'.format(nome))

exit()

nomes = ('Nome A', 'Nome B', 'Nome C', 'Nome D', 'Nome E')
if 'Nome D' in nomes:
    print('Achei o Nome D')

i = 0
while i < 10:
    print("{0} Tome muito líquido".format(i))
    i = i + 1

exit()

nmax = int(input("Digite a quantidade desejada: "))

for i in enumerate(range(nmax), start = 100):
    print(i)

exit()

for i in range(100):
    i = i*2
    print(i)

exit()

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 < num2:
    s = '{0} é menor que {1}'
elif num1 == num2:
    s = '{0} é igual a {1}'
else:
    s = '{0} não é menor que {1}'
#s = '{0} é menor que {1}' if num1 < num2 else '{0} não é menor que {1}'

print(s.format(num1,num2))