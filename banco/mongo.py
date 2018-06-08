#!/usr/bin/python3

from pymongo import MongoClient
from pymongo import errors

client = MongoClient()
db = client['bradesco']

try:
    r = {}
    r['_id'] = 9
    r['numero'] = 4456
    r['nome'] = 'Adauto'
    db.cc.insert(r)
except errors.DuplicateKeyError as e:
    print('Chave duplicada...')

for i in db.cc.find():
    try:
        print(i['nome'])
    except:
        pass