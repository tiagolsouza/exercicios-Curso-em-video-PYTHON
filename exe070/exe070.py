a = 25
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE NOME E PREÇOS DE PRODUTOS', a))
print('\033[32m-\033[m'*a)

nome = menor = cont = 'o'
preço = total = maior = menorp = 0

while True :
    nome = str(input('\033[36mDigite o nome do produto: ')).strip().capitalize()
    preço = float(input('Digite o preço do produto: R$'))
    if total == 0 :
        menor = nome
        menorp = preço
    total += preço
    if preço > 1000 :
        maior += 1
    if preço < menorp :
        menorp = preço
        menor = nome
    while cont not in 'SN' :
        cont = str(input('\033[1;35mDeseja continuar? [S/N]: ')).upper()[0]
    if cont in 'N' :
        print('\033[33mENCERRADO')
        break
    cont = 'o'
print(f'\033[1;34mO tatal gasto na compra foi: {total}.\n{maior} produtos custam mais de R$1000,00\n{menor} é o produto mais barato.\033[m')
