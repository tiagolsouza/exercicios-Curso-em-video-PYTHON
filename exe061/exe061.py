a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('PROGRESSAO ARITMETICA',a))
print('\033[32m-\033[m'*a)

prog = int(input('\033[1;36mDigite o primeiro termo da PA: \033[m'))
raz = int(input('\033[36mDigite a razao da PA: '))
cont = 0
resultado = prog


print('\033[1;34m(\033[m', end='')
while cont < 10 :
    if cont == 9 :
        print('\033[1;34m{})'.format(resultado))
    else:
        print('\033[1;34m{}, \033[m'.format(resultado), end='')
    cont += 1
    resultado += raz
print('\033[4;33mFIM\033[m')
