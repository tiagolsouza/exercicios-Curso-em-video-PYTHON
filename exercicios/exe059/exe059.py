a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('MANIPULAÇAO DE VALORRES',a))
print('\033[32m-\033[m'*a)

menu = 0
valor1 = 0
valor2 = 0
resultado = 0
maior = 'maior'

valor1 = float(input('\033[1;36mDigite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

while menu != 5 :
    menu = int(input('''\033[1;35mMenu:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
\033[1;36mDigite uma opçao do menu acima: \033[m'''))
    if menu == 1 :
        resultado = valor1+valor2
        print('\033[1;33mO resultado da soma de {} com {} sera: {}'.format(valor1, valor2, resultado))
    if menu == 2 :
        resultado = valor1*valor2
        print('\033[1;33mO resultado da multiplicaçao de {} com {} sera: {}'.format(valor1, valor2, resultado))
    if menu == 3 :
        print('\033[1;33mO primeiro valor é o maior.\033[m' if valor1 > valor2 else '\033[1;33mO segundo valor é o maior.\033[m')
    if menu == 4 :
        valor1 = float(input('\033[1;36mDigite o primeiro valor: '))
        valor2 = float(input('Digite o egundo valor: \033[m'))
    print('\033[1;36m-----\033[m')
print('\033[1;33mFIM\033[m')