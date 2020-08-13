a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA ORDENADOR DE PARES E IMPARES', a))
print('\033[32m-\033[m'*a)

lista = []
par = []
impar = []
cont = 's'

while True:
    if 's' in cont:
        lista.append(int(input('\033[36mDigite um numero inteiro: \033[m')))
        if lista[-1] % 2 == 0:
            par.append(lista[-1])
        else:
            impar.append(lista[-1])
    elif 'n' in cont:
        break
    else:
        print('\033[1;31mValor invalido, tente novamente!\033[m')
    cont = input('\033[35mQuer continuar? [S/N]\033[m').lower().strip()[0]

print(f'\033[1;34mOs valores digitado foram {lista}.')
print(f'Os valores pares foram {par}')
print(f'Os valores impares foram {impar}')