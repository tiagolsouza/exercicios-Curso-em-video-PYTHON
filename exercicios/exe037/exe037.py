print('\033[1;31m_\033[m'*19)
print('\033[1;34mCONVERSOR DE BASES\033[m')
print('\033[1;31m-\033[m'*19)

numero = int(input('Digite um numero inteiro a ser convertido: '))
base = int(input('Digite o codigo da base a ser convertido o numero digitado anteriormente, da seguinte forma: 1 para binario, 3 para octal, 2 para hexadecimal: '))

if base == 1 :
    numero = bin(numero)
    print('O valor digitado convertido em binario sera: {}'.format(numero[2:]))
elif base == 2 :
    numero = oct(numero)
    print('O valor digitado em octadecimal sera: {}'.format(numero))
else:
    numero = hex(numero)
    print('O valor digitado em hexadecimal sera: {}'.format(numero))
