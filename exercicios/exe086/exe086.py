a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE MATRIZES', a))
print('\033[32m-\033[m'*a)

matriz = [[0,0,0],[0,0,0],[0,0,0]]
#matriz = list()
#pilha = list()

for n in range(0,3):
    for m in range(0,3):
        matriz[n][m] = int(input(f'\033[36mDigite um valor para a posiçao [{n},{m}]: \033[m'))
        #pilha.append(int(input(f'\033[36mDigite um valor para a posiçao [{n},{m}]: \033[m')))
    #matriz.append(pilha[:])
    #pilha.clear()

print(f'\033[1;34mMATRIZ[{n+1}x{m+1}]\033[35m')
for n in range(0,3):
    for m in range(0,3):
        print(f'[{matriz[n][m]:^5}]', end=' ')
    print('')
