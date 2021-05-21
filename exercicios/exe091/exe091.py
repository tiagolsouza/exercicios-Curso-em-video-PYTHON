a = 50
print('\033[32m_\033[m'*a)
print(f'\033[1;32m{"SISTEMA DE ROLAGEM DE DADOS E ORDENAÇAO":=^{a}}\033[m')
print('\033[32m-\033[m'*a)

from time import sleep
from random import randint
from operator import itemgetter

jogos = {'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1,6),}

for c,k in jogos.items():
    print(f'\033[1;35m{c} tirou {k} nos dados!')
    sleep(0.5)

ranking = list(sorted(jogos.items(), key=itemgetter(1), reverse=True))

print('\033[36m-=\033[m'*15)
print('\033[1;34m==CLASSIFICAÇAO GERAL==\033[m')
for b,d in enumerate(ranking):
    print(f'\033[1;35m Em {b+1}º lugar: {d[0]} com {d[1]}.')
    sleep(0.5)