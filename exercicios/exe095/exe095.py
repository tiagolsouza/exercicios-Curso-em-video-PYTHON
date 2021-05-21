a = 50
print('\033[32m_\033[m'*a)
print(f'\033[1;32m{"SISTEMA DE APROVEITAMENTO DO ATLETA":=^{a}}\033[m')
print('\033[32m-\033[m'*a)

lista = []
atleta = {}
partidas = []

while True:
    atleta.clear()
    atleta['nome'] = str(input('\033[35mNome do jogador: '))
    jogos = int(input(f'Quantas partidas {atleta["nome"]} jogou? '))
    partidas.clear()
    for c in range(0,jogos):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    atleta['gols'] = partidas[:]
    atleta['total'] = sum(partidas)
    lista.append(atleta.copy())
    while True:
        resp = str(input('\033[35mQuer continuar? [S/N] \033[m')).upper()[0]
        if resp in 'SN':
            break
        print('\033[31mERRO, responda apenas S ou N!\033[m')
    if resp == 'N':
        break
print('-='*30)
print('\033[34mcod', end=' ')
for i in atleta.keys():
    print(f'{i:<15}', end='')
print()


print('-'*40)
for i,j in enumerate(lista):
    print(f'{i:>3} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca = int(input('\033[1;34mMostrar dados de qual jogador? (999 pra parar) \033[m'))
    if busca == 999:
         break
    if busca >= len(lista):
        print(f'\033[31mERRO! Nao existe jogador com codigo {busca}\033[m')
    else:
        print(f'\033[34m -- LEVANTAMENTO DO JOGADOR {lista[busca]["nome"]}: ')
        for i,g in enumerate(lista[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols')
    print('-'*40)
print('\033[4;32mVOLTE SEMPRE')

'''print('\033[36m-=\033[m'*20)
print(f'\033[1;34m{atleta["nome"]} jogou {jogos} partidas.\033[m')
for b,d in enumerate(partidas):
    print(f'\033[1;34m  =>Na partida {b+1}, fez {d} gols.\033[m')
print(f'\033[1;34mFoi um total de {totgol} gols.')
print('\033[36m-=\033[m'*20)
'''