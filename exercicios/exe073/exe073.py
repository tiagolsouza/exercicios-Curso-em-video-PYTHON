a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE TABELA DO BRASILEIRAO', a))
print('\033[32m-\033[m'*a)


brasileiro = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco',
              'Chapecoense', 'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia', 'Sao Paulo', 'Fluminense',
              'Sport Recife', 'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta', 'Atletico-GO')

ordenado = sorted(brasileiro)

print(f'\033[34mOs 5 primeiros colocados sao: \033[1;35m{brasileiro[:5]}\033[m')
print('\033[33m-=\033[m'*10)
print(f'\033[34mOs 4 ultimos colocados sao: \033[1;35m{brasileiro[-4:]}\033[m')
print('\033[33m-=\033[m'*10)
print(f'\033[34mOs times em ordem alfabética:  \033[1;35m{ordenado}\033[m')
#print(f'\033[34mOs times em ordem alfabética:  \033[1;35m{sorted(brasileiro)}\033[m')

print('\033[33m-=\033[m'*10)
#print('\033[34mO Chapecoense esta na \033[4m{}ª\033[0;34m posição.'.format(brasileiro.index('Chapecoense')+1))
print(f'\033[34mO Chapecoense esta na \033[4m{brasileiro.index("Chapecoense")+1}ª\033[0;34m posição.')