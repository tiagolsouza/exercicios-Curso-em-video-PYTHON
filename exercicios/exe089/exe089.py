a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE BOLETIM', a))
print('\033[32m-\033[m'*a)

boletim = list()
individuo = list()
notas = list()
media = 0
continuar = 's'
conti2 = 0

while True:
    if 's' in continuar:
        individuo.append(input('Nome: '))
        notas.append(float(input('Nota 1: ')))
        notas.append(float(input('Nota 2: ')))
        individuo.append(notas[:])
        boletim.append(individuo[:])
        notas.clear()
        individuo.clear()
    elif 'n' in continuar:
        break
    else:
        print('Tente novamente!', end='')
    continuar = str(input('Deseja continuar? [S/N]')).lower().strip()[0]

print('\033[35m-=\033[m'*20)

print('\033[1;34mNº  NOME            MEDIA')
print('-'*26)

for c, n in enumerate(boletim):
    media = (n[1][0]+n[1][1])/2
    #print(f'n={n}, c={c}')
    print(f'{c:<2}  {n[0]:<15} {media:>5}')

print('\033[35m-=\033[m'*20)

while True:
    conti2 = int(input('\033[1;36mMostrar notas de qual aluno? (999 para interromper) \033[m'))
    if conti2 == 999:
        break
    elif conti2 > len(boletim):
        print('\033[31mAluno nao encontrado, tente novamente! \033[m')
    else:
        print(f'\033[1;34mNotas de {boletim[conti2][0]} são: {boletim[conti2][1]}\033[m')