#!/usr/bin/python3

import psycopg2 as psql

DB='python'
USER='gabriel'
PASS='4linux'
HOST='127.0.0.1'

cnn_str = 'host={0} dbname={1} user={2} password={3}'
cnn = psql.connect(cnn_str.format(HOST, DB, USER, PASS))

cur = cnn.cursor()

#sql = "INSERT INTO usuarios (nome, email, cv, salario) VALUES ('{}','{}','{}','{}')"
#cur.execute(sql.format('Gabriel', 'g@gmagazine.com', 'Kingsman', 2500.00))
#cnn.commit()

#cur.execute('SELECT id, nome, salario FROM usuarios')
#print('{0:^4}|{1:^20}|{2:^20}'.format('ID', 'NOME', 'SALARIO'))
#for rs in cur:
#   print('{0[0]:^4}|{0[1]:^20}|{0[2]:^20}'.format(rs))

sql = "insert into usuarios (nome, email, cv, salario) values ('{}','{}','{}','{}')"

with open('usuarios.csv', 'r') as f:
    for l in f:
        l = l.strip().split(',')
        cur.execute(sql.format(l[1], l[2], '', l[3]))
    cnn.commit()