a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE IDENTIIFADOR DE MAXIMOS E MINIMOS', a))
print('\033[32m-\033[m'*a)

continuar = 's'
lista = [int(input('\033[35mDigite um numero inteiro: \033[m'))]
print('\033[36mAdicionado com sucesso!')

while True:
    continuar = input('\033[35mQuer continuar? [S/N] ').lower().strip()[0]
    if 's' in continuar:
        teste = int(input('\033[35mDigite um numero inteiro: \033[m'))
        if teste in lista:
            print('\033[32mValor duplicado, nao adicionado!\033[m')
        else:
            print('\033[36mAdicionado com sucesso!')
            lista.append(teste)
    elif 'n' in continuar:
        break
    else:
        print('\033[31mTente novamente!\033[m')
lista.sort()
print('\033[1;33m-+'*20)
print(f'\033[1;34mVoce digitou os valores {lista}\033[m')
print('\033[1;33m{:=^40}\033[m'.format('FIM'))
