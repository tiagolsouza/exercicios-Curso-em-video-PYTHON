a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE SORTEIO DE NUMEROS DA MEGA SENA', a))
print('\033[32m-\033[m'*a)

from random import randint
from time import sleep
jogadas = int(input('\033[1;35mQuantos jogos quer que eu sorteie? \033[m'))
mega = list()
inteiro = 0

print(f'\033[32m{"NUMEROS SORTEADOS":-^30}\033[m')
for c in range(0,jogadas):
    for n in range(0,6):
        adicionar = randint(1, 60)
        if n == 0 :
            inteiro = adicionar
        else:
            while inteiro == adicionar :
                adicionar = randint(1, 60)
        mega.append(adicionar)
        inteiro = adicionar
    mega.sort()
    print(f'\033[1;34m{mega}\033[m')
    mega.clear()
    sleep(1)
print(f'\033[32m{"BOA SORTE":-^30}\033[m')