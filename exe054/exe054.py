a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('TESTE DE MAIORIDADE',a))
print('\033[32m-\033[m'*a)

from datetime import date
teste = 0
maior = 0
menor = 0

for c in range(0,7):
    idade = int(input('\033[1;32mDigite o ano de nascimento da {}ª pessoa: \033[m'.format(c+1)))
    teste = date.today().year - idade
    if teste < 21 :
        menor += 1
    else:
        maior += 1
print('\033[1;34mNo total, {} pessoa sao menores de idade, e {} são maiores.\033[m'.format(menor, maior))
