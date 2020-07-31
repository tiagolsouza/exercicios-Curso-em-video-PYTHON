a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('LEITOR E SOMADOR DE NUMEROS', a))
print('\033[32m-\033[m'*a)

#soma = contador = digito = 0

soma = 0
contador = 0
digito = 0

while digito != 999 :
    contador += 1
    soma += digito
    digito = int(input('\033[1;35mDigite um numero inteiro, ou 999 para encerrar: \033[m'))

print('\033[1;34mO total de numeros digitados foi: \033[4;33m{}\033[m\033[1;34m, e a soma entre eles foi: \033[4;33m{}\033[34m!!\033[m'.format(contador, soma))
