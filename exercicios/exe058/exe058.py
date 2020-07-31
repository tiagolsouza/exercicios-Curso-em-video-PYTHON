a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('JOGO DE ADIVINHAÇAO',a))
print('\033[32m-\033[m'*a)

from random import randint
num = int(input('\033[1;32mAdivinhe o numero que o computador esta pensando entre 0 e 10: \033[m'))
comp = randint(0,10)
tent = 1
temp = 'aaa'
while num != comp :
    tent +=1
    if abs(num - comp) > 2 :
        temp = '\033[4;34me esta frio!!\033[m'
    else:
        temp = '\033[4;31mmas esta quente!!\033[m'
    print('\033[1;31mVoce errou, {},\033[1;31mtente novamente: \033[m'.format(temp))
    num = int(input('\033[1;3mAdivinhe o numero que o computador esta pensando entre 0 e 10: \033[m'))
print('\033[1;34mParabens, vc conseguiu acertar, com {} tentativas\033[m'.format(tent))
