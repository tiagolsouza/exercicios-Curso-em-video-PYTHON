a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE GERADOR DE NUMEROS ALEATORIOS', a))
print('\033[32m-\033[m'*a)

from random import randint

menor = maior = 0
tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

for c in range(0,5):
    if c == 0:
        menor = maior = tupla[0]
    else:
        if menor > tupla[c]:
            menor = tupla[c]
        if maior < tupla[c]:
            maior = tupla[c]
print(f'\033[1;34mOs valores sorteador foram: \033[35m{tupla}\033[m')
print(f'\033[1;34mO maior valor sorteado foi: \033[35m{maior}\033[m')
print(f'\033[1;34mO menor valor sorteado foi: \033[35m{menor}\033[m')