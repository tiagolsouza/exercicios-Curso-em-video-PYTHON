a = 50
print('\033[32m_\033[m' * a)
print(f'\033[1;32m{"SISTEMA DE VERIFICAÇAO DE MAIOR DIGITO":=^{a}}\033[m')
print('\033[32m-\033[m' * a)

from random import randint
from time import sleep

def maior(*num):
    cont = mai = 0
    print('-='*30)
    print('\nAnalisando os valores recebidos...')
    for c in num:
        print(c, end=' ')
        sleep(0.3)
        if cont == 0:
            mai = c
        else:
            if c > mai:
                mai = c
        cont +=1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi: {mai}')



maior(randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()