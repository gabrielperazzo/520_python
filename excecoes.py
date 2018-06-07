#!/usr/bin/python3

import datetime

users = ['Hector', 'Vanderlei', 'Adauto', 'Daniel']

try:
    number = int(input('Digite um número inteiro entre 0 e 3: '))
    print(users[number])
except ValueError as e:
    print(e)
except IndexError as e:
    d = datetime.datetime.now()
    f = open('python.log' , 'a')
    f.write('{0} - {1}\n'.format(d.strftime('%Y-%m-%d %H:%M'),str(e)))
    f.close()