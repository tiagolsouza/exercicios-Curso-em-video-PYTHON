a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('PROGRESSAO ARITMETICA',a))
print('\033[32m-\033[m'*a)

prog = int(input('\033[1;36mDigite o primeiro termo da PA: \033[m'))
raz = int(input('\033[36mDigite a razao da PA: '))
cont = 10
resultado = prog
novo = 0


print('\033[1;34m(\033[m', end='')
while cont > 0 :
    cont -= 1
    if cont == 0 :
        print('\033[1;34m{})'.format(resultado))
        novo = int(input('\033[1;33mQuanto digitos a mais gostaria de mostrar(0 para nenhum)? \033[m'))
        cont = novo
        if cont != 0:
            print('\033[1;34m(\033[m', end='')
    else:
        print('\033[1;34m{}, \033[m'.format(resultado), end='')
    resultado += raz
print('\033[4;33mFIM\033[m')
