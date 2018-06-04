#!/usr/bin/python3
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = (num1+num2)

s = '''Primeiro valor digitado {0:.>10}
Segundo valor digitado {1:.>11}
Resultado da soma: {2:.>15}'''

print(s.format(num1, num2, num3))