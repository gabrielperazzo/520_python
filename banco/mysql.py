#!/usr/bin/python3

import MySQLdb
from faker import Faker
from random import uniform

cnn = MySQLdb.connect(host='127.0.0.1', user='gabriel', passwd="123@4linux", db="python")

cur = cnn.cursor()
fake = Faker('pt_BR')

sql = "INSERT INTO usuarios (nome, email, cv, salario) VALUES ('{}','{}','{}','{}')"


for i in range(1000):
    u = {}
    u['name'] = fake.name()
    u['mail'] = fake.email()
    u['job'] = fake.job()
    u['cash'] = round(uniform(1000, 2000), 2)
    cur.execute(sql.format(u['name'], u['mail'], u['job'], u['cash']))

cnn.commit()

cur.execute('SELECT * FROM usuarios')
for i in cur:
    print('{}\t{}\t{}'.format(i[0], i[1], i[4]))

