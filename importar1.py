#!/usr/bin/python3

#import modulin as m

from modulin import y, lick, Disponivel

print(y)
d = Disponivel(':)')
print(d.disponivel)

print('\n'.join([str(n) for n in lick()]))
print('')
print('\n'.join(list(map(lambda i : str(i), lick()))))

for i in lick():
    print(i)
