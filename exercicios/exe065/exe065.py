a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('MAIOR E MENOR VALORES', a))
print('\033[32m-\033[m'*a)

media = cont = maior = menor = numero = soma = 0
sair = 's'

while sair != 'N' :
    cont +=1
    numero = int(input('\033[1;36mDigite um numero: \033[m'))
    soma += numero
    if cont == 1 :
        maior = menor = numero
    if numero > maior :
        maior = numero
    elif numero < menor :
        menor = numero
    sair = str(input('\033[1;35mContinuar? [S/N]\033[m')).strip().upper()[0]

media = soma/cont
print('\033[1;34mO maior numero foi: {}, e o menor numero foi: {}. A media foi: {}\033[m'.format(maior, menor, media))
