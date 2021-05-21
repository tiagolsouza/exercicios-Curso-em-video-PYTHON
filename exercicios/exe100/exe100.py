a = 50
print('\033[32m_\033[m' * a)
print(f'\033[1;32m{"SISTEMA QUE SORTEIA E SOMA PARES":=^{a}}\033[m')
print('\033[32m-\033[m' * a)

from random import randint
from time import sleep

def sorteia(lista):
    print('\033[1;34msorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        lista.append(randint(1,10))
        print(f'{lista[-1]}', end=' ')
        sleep(0.3)
    print('Pronto!\033[m')


def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'\033[34mSomando os valores pares de {lista}, temos {soma}\033[m')


numeros = list()
sorteia(numeros)
somapar(numeros)

