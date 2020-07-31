a = 25
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE PAR OU IMPAR', a))
print('\033[32m-\033[m'*a)

from random import randint
pc = num = soma = cont = 0
sinal = 'P'

while True:
    num = int(input('\033[36mDigite um valor: '))
    sinal = str(input('Par ou Impar? [P/I] ')).upper()
    while sinal not in 'PI':
        sinal = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    pc = randint(0,10)
    soma = pc + num
    if soma % 2 != 0 :
        print(f'\033[34mVoce jogou {num} e o computador {pc}. O total de {soma} deu IMPAR!')
    else:
        print(f'\033[34mVoce jogou {num} e o computador {pc}. O total de {soma} deu PAR!')
    if sinal == 'P' and soma % 2 == 0 :
        print('\033[34mVoce venceu! \nVamos jogar novamente...\033[m')
    elif sinal == 'I' and soma % 2 != 0 :
        print('\033[34mVoce venceu! \nVamos jogar novamente...\033[m')
    else:
        print('\033[1;31mVoce perdeu!!')
        print(f'\033[1;34m GAME OVER! Voce venceu {cont} vezes\033[m')
        break
    cont += 1