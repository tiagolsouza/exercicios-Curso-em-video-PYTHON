a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('FIBONACCI', a))
print('\033[32m-\033[m'*a)

vzs = int(input('\033[1;35mQuantos elementos de Fibonacci gostaria ver? \033[m'))
num0 = 0
num1 = 1
num2 = 1
cont = vzs

while cont > 0 :
    '''if cont == vzs :
        print('\033[1;36m{}\033[m'.format(num0), end='')
        num0 = num1
    else:
        print('\033[1;36m->{}\033[m'.format(num0), end='')'''

    if cont == 1:
        print('{}'.format(num0), end='')
    else:
        print('{},'.format(num0), end='')
    num0 = num1
    num1 = num2
    num2 = num0 + num1
    cont -= 1

print('\n\033[1;34mFIM\033[m')