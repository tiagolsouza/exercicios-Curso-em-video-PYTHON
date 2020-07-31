a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('FATORIAL',a))
print('\033[32m-\033[m'*a)

fat = int(input('\033[1;36mDigite um numero: \033[m'))
resultado = 0
cont = fat
print('\033[35m{}!=\033[m'.format(fat), end='')

while cont != 0 :
    if cont == fat :
        print('\033[35m{}x\033[m'.format(cont), end='')
        resultado = cont
    elif cont == 1 :
        print('\033[35m{}=\033[m'.format(cont), end='')
    else:
        print('\033[35m{}x\033[m'.format(cont), end='')
        resultado *= cont
    cont -= 1
print('\033[33m{}\033[m'.format(resultado))
print('\033[34mFIM\033[m')

