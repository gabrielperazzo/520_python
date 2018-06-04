#!/usr/bin/python3

#Capturar dois valores numérios do terminal e compará-los

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