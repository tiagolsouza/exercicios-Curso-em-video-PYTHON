a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE MATRIZES', a))
print('\033[32m-\033[m'*a)

matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = mai = scol = 0

for n in range(0,3):
    for m in range(0,3):
        matriz[n][m] = int(input(f'\033[36mDigite um valor para a posiçao [{n},{m}]: \033[m'))

print('\033[35m-=\033[m'*20)
print(f'\033[1;34mMATRIZ[{n+1}x{m+1}]\033[35m')
for n in range(0,3):
    for m in range(0,3):
        print(f'[{matriz[n][m]:^5}]', end=' ')
        if matriz[n][m] % 2 == 0:
            par += matriz[n][m]
    print('')

for m in range(0,3):
    scol += matriz[m][2]

for n in range(0,3):
    if n == 0:
        mai = matriz[1][n]
    else:
        if mai < matriz[1][n]:
            mai = matriz[1][n]

print('\033[35m-=\033[m'*20)

print(f'\033[1;34mA soma dos valores pares é: {par}.')
print(f'\033[1;34mA soma dos valores da terceira coluna é: {scol}')
print(f'\033[1;34mO maior valor da segunda linha é: {mai}')

