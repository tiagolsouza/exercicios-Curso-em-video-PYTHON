a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA ORDENADOR DE NUMEROS', a))
print('\033[32m-\033[m'*a)

cont = 's'
lista = []
lista.append(int(input('\033[35mDigite um valor: ')))

while True:
    cont = input('\033[36mQuer continuar? [S/N] \033[m').lower().strip()
    if 's' in cont:
        lista.append(int(input('\033[35mDigite um valor: ')))
    elif 'n' in cont:
        break
    else:
        print('\033[1;31mTente novamente!')
print(f'\033[1;34mVoce digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'\033[1;34mOs valores em ordem decrescente sao: {lista}')
print('\033[1;34mO valor 5 faz parte da lista\033[m' if 5 in lista else '\033[1;31mO valor 5 nao foi encontrado!\033[m')