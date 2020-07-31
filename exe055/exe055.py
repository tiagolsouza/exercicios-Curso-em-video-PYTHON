a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('TESTE DE PESO',a))
print('\033[32m-\033[m'*a)

maior = 0
menor = 1000

for c in range(0,5):
    massa = float(input('\033[1;33mDigite a massa da {}ª pessoa: \033[m'.format(c+1)))
    if massa > maior :
        maior = massa
    if massa < menor :
        menor = massa
print('\033[1;34mA maior massa lida foi de: {}Kg e o de menor massa foi de: {}Kg.\033[m'.format(maior, menor))

'''if c==1:
    maior = massa
    menor = massa'''