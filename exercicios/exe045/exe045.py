print('\033[32m_\033[m'*20)
print('\033[1;32m{:^20}\033[m'.format('JOKENPÔ'))
print('\033[32m-\033[m'*20)

from random import choice
from time import sleep

print('\033[1;33mGESTOS:\033[36m\nPedra:...1\nPapel:...2\nTesoura:.3\033[m')
gesto1 = int(input('\033[1;35mDigite o seu gesto de acordo com a tabela acima: \033[m'))
gesto2 = ('pedra', 'papel', 'tesoura')
escolhido = choice(gesto2)  #escolhido = randint(0,2)

print('\033[1;32mJO KEN PÔ\033[m')
#sleep(3)

print(gesto1)
print(escolhido)

if gesto1 == 1 :
    if escolhido == 'pedra' :
        print('\033[35mVoce escolheu: {}\033[m'.format('pedra'))
        print('\033[35mO computador escolheu: {}\033[m'.format(escolhido))
        print('\033[1;33mVoces empataram!\033[m')
    if escolhido == 'papel' :
        print('\033[1;35mVoce escolheu: {}\033[m'.format('pedra'))
        print('\033[1;35mO computador escolheu: {}\033[m'.format(escolhido))
        print('\033[1;31mVoce perdeu!\033[m')
    if escolhido == 'tesoura' :
        print('\033[1;35mVoce escolheu: {}\033[m'.format('pedra'))
        print('\033[1;35mO computador escolheu: {}\033[m'.format(escolhido))
        print('\033[1;34mVoce ganhou, parabens!\033[m')

elif gesto1 == 2 :
    if escolhido == 'papel' :
        print('\033[35mVoce escolheu: {}\033[m'.format('papel'))
        print('\033[35mO computador escolheu: {}\033[m'.format(escolhido))
        print('\033[1;33mVoces empataram!\033[m')
    if escolhido == 'tesoura' :
        print('\033[1;35mVoce escolheu: {}\033[m'.format('papel'))
        print('\033[1;35mO computador escolheu: {}\033[m'.format(escolhido))
        print('\033[1;31mVoce perdeu!\033[m')
    if escolhido == 'pedra' :
        print('\033[1;35mVoce escolheu: {}\033[m'.format('papel'))
        print('\033[1;35mO computador escolheu: {}\033[m'.format(escolhido))
        print('\033[1;34mVoce ganhou, parabens!\033[m')

elif gesto1 == 3 :
    if escolhido == 'tesoura' :
        print('\033[35mVoce escolheu: {}\033[m'.format('tesoura'))
        print('\033[35mO computador escolheu: {}\033[m'.format(escolhido))
        print('\033[1;33mVoces empataram!\033[m')
    if escolhido == 'pedra' :
        print('\033[1;35mVoce escolheu: {}\033[m'.format('tesoura'))
        print('\033[1;35mO computador escolheu: {}\033[m'.format(escolhido))
        print('\033[1;31mVoce perdeu!\033[m')
    if escolhido == 'papel' :
        print('\033[1;35mVoce escolheu: {}\033[m'.format('tesoura'))
        print('\033[1;35mO computador escolheu: {}\033[m'.format(escolhido))
        print('\033[1;34mVoce ganhou, parabens!\033[m')

else:
    print('\033[1;31mAlgo de errado nao esta certo\033[m')
