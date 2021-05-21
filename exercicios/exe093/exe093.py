a = 50
print('\033[32m_\033[m'*a)
print(f'\033[1;32m{"SISTEMA DE APROVEITAMENTO DO ATLETA":=^{a}}\033[m')
print('\033[32m-\033[m'*a)

atleta = {}
partidas = []
atleta['nome'] = str(input('\033[35mNome do jogador: '))
jogos = int(input(f'Quantas partidas {atleta["nome"]} jogou? '))
totgol = 0

for c in range(0,jogos):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    totgol += partidas[c]

atleta['gols'] = partidas[:]
atleta['total'] = totgol     #atleta['total'] = sum(partidas)

print('\033[36m-=\033[m'*20)
print('\033[1;34m', atleta)

print('\033[36m-=\033[m'*20)
for c,k in atleta.items():
    print(f'\033[1;34mO campo {c} tem {k}.\033[m')

print('\033[36m-=\033[m'*20)
print(f'\033[1;34m{atleta["nome"]} jogou {jogos} partidas.\033[m')
for b,d in enumerate(partidas):
    print(f'\033[1;34m  =>Na partida {b+1}, fez {d} gols.\033[m')
print(f'\033[1;34mFoi um total de {totgol} gols.')
print('\033[36m-=\033[m'*20)
