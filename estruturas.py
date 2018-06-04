#!/usr/bin/python3

#Capturar dois valores numérios do terminal e compará-los

for i in 'Teste de for i':
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