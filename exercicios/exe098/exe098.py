a = 50
print('\033[32m_\033[m' * a)
print(f'\033[1;32m{"SISTEMA DE CONTAGEM ADAPTAVEL":=^{a}}\033[m')
print('\033[32m-\033[m' * a)

from time import sleep


def cont(a, b, c):
    if c == 0:
        passo = 1
    else:
        passo = abs(c)
    print('\033[34m-=\033[m' * 20)
    print(f'\033[1;34mContagem de {a} ate {b} de {passo} em {passo}.\033[m')
    if a < b :
        cont = a
        while cont <= b :
            print(f'\033[35m{cont}', end=' ')
            cont += passo
            sleep(0.5)
        print('\033[34m\nFIM!\033[m')
    else:
        cont = a
        while cont >= b:
            print(f'\033[35m{cont}', end=' ')
            cont -= passo
            sleep(0.5)
        print('\033[34m\nFIM!\033[m')


'''print('-='*16)
print('\033[1;34mContagem de 1 ate 10 de 1 em 1:\033[m')
for c in range(1, 11):
    print(f'\033[35m{c}', end=' ')
    #sleep(0.5)
print('\033[34m\nFIM!\033[m')

print('-='*16)
print('\033[1;34mContagem de 10 ate 1 de 1 em 1:\033[m')
for c in range(10, 0, -1):
    print(f'\033[35m{c}\033[m', end=' ')
    #sleep(0.5)
print('\033[34m\nFIM!\033[m')
print('-='*20)'''


cont(1, 10, 1)
cont(10, 1, 1)
print('\033[34mAgora é sua vez, personalize a contagem!\033[m')
inicio = int(input('\033[36mInicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: \033[m'))

cont(inicio, fim, passo)