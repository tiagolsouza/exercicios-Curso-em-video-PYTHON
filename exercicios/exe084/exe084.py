a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE IDENTIFICAÇÃO DE PESOS', a))
print('\033[32m-\033[m'*a)

listafinal = list()
listainit = list()
tamanho = 0
maiorp = menorp = 0
continuar = 's'

while True:
    if 's' in continuar:
        listainit.append(str(input('\033[36mNome: ')))
        listainit.append(int(input('Peso: \033[m')))
        listafinal.append(listainit[:])
        tamanho +=1
        if tamanho == 1:
            maiorp = listainit[-1]
            menorp = listainit[-1]
        elif menorp > listainit[-1]:
            menorp = listainit[-1]
        elif maiorp < listainit[-1]:
            maiorp = listainit[-1]
        listainit.clear()
    elif 'n' in continuar:
        break
    elif 'sn' not in continuar:
        print('\033[31mTente novamente!\033[m')
    continuar = str(input('\033[35mQuer continuar? [S/N] \033[m')).lower().strip()[0]

print(f'\033[34mAo todo, você cadastrou {tamanho} pessoas.\033[m')
#print(f'\033[34mAo todo, você cadastrou {len(listafinal} pessoas.\033[m')


print(f'\033[34mO maior peso cadastrado foi de {maiorp}Kg. Peso de: ', end='')
for c in listafinal:
    if c[1] == maiorp:
        print(f'\033[35m{c[0]}\033[m', end=' ')

print('')
print(f'\033[34mO menor peso cadastrado foi de {menorp}Kg. Peso de: ', end='')
for c in listafinal:
    if c[1] == menorp:
        print(f'\033[35m{c[0]}\033[m', end=' ')
