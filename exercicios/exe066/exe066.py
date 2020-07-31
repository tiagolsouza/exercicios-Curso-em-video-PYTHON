a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('LEITOR DE NUMEROS', a))
print('\033[32m-\033[m'*a)

n = cont = soma = 0

while True:
    n = int(input('\033[36mDigite um numero (999 para sair): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'\033[1;33mO total de numeros digitados foi {cont}, e a soma entre eles é {soma}\033[m')
