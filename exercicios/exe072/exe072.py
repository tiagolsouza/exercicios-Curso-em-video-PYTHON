a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE ESCRITA DE NUMEROS POR EXTENSO', a))
print('\033[32m-\033[m'*a)

extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('\033[1;35mDigite um numero inteiro entre 0 e 20: '))

while True:
    if 0<=numero<=20 :
        print(f'\033[34mVoce digitou o numero: \033[4;34m{extenso[numero]}\033[m')
        break
    else:
        numero = int(input('\033[31mTente novamente.Digite um numero inteiro entre 0 e 20: '))
print('\033[1;32mFIM')

'''while True:
    numero=int(input('Digite um numero entre 0 e 20'))
    if 0<=numero<=20:
        break
    print('tente novamente.', end='')
print(f'Vc digitou o numero {extenso[numero]}')'''
