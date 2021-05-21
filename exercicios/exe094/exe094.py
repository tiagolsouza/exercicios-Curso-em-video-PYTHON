a = 50
print('\033[32m_\033[m'*a)
print(f'\033[1;32m{"SISTEMA DE NOMES E MEDIA DE IDADES":=^{a}}\033[m')
print('\033[32m-\033[m'*a)

lista = []
pilha = {}
continuar = 's'
somaid = 0

while True:
    if 's' in continuar:
        pilha['nome'] = str(input('\033[35mNome: \033[m'))
        while True:
            pilha['sexo'] = str(input('\033[35mSexo [M/F]: \033[m')).upper().strip()[0]
            if pilha['sexo'] in 'FM':
                break
            #elif 'M' in pilha['sexo']:
            #    break
            else:
                print('\033[31mTente novamente!\033[m')
        pilha['idade'] = int(input('\033[35mIdade: \033[m'))
        somaid += pilha['idade']
        lista.append(pilha.copy())
    elif 'n' in continuar:
        break
    else:
        print('\033[31mTente novamente!\033[m')
    continuar = str(input('\033[36mContinuar? [S/N] \033[m')).lower().strip()[0]
    pilha.clear()

somaid = somaid/len(lista)
contador = 0

print('\033[33m-=\033[m'*20)
print(f'\033[1;34mA) Ao todo temos {len(lista)} cadastradas.')
print(f'\033[1;34mB) A média de idade é de {somaid:.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for f in lista:
    if f['sexo'] == 'F':
        print(f['nome'], end=' ')
        contador +=1
if contador == 0:
    print('NENHUMA', end='')
print(f'\nD) Lista com pessoas com idade acima da média:')
for m in lista:
    if m['idade'] >= somaid:
        print(f'   Nome: {m["nome"]}, sexo: {m["sexo"]}, Idade: {m["idade"]}')
print(f'\033[1;32m{"FIM":-^40}\033[m')