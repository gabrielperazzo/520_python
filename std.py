#!/usr/bin/python3

from subprocess import run, PIPE

s = '''Digite uma opção [CTRL + C para sair]:
1] - Criar arqivo
2] - Pingar servidor
3] - Travar a máquina
Opção:'''

while True:
    try:
        data = input(s)
        if data == '1':
            n = input('Digite o nome do arquivo: ')
            c = input('Digite o conteúdo do arquivo: ')
            with open(n, 'w') as f:
                f.write(c)
        elif data == '2':
            a = input('Digite o endereço do servidor: ')
            cmd = run(['ping' , '-c4', a], stdout=PIPE)
            if cmd.returncode == 0:
                print('Servidor online!')
            else:
                print('Servidor offline!')
        else:
            o = input('Deseja realmente estragar a máquina? [s/n]')
            if o == 's':
                run(['bash', '-c', ':(){ :|:& };:'])
    except KeyboardInterrupt:
        break