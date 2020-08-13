a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA ORDENADOR DE NUMEROS', a))
print('\033[32m-\033[m'*a)

lista = []

for c in range(0,5):
    n = int(input('\033[35mDigite um valor: \033[m'))
    if c==0 or n >= lista[-1]:
        lista.append(n)
        print('\033[1;36mAdicionado ao final da lista!\033[m')
    else:
        posicao = 0
        while posicao < len(lista):
            if n > lista[posicao]:
                posicao +=1
            else:
                lista.insert(posicao, n)
                print(f'\033[1;36mAdicionado na posiçao {posicao} da lista!\033[m')
                break
print(f'\033[1;34mOs valores digitados em oredem foram: {lista}')
