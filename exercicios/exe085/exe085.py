a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE PARES E IMPARES', a))
print('\033[32m-\033[m'*a)

lista = [[],[]]
#lista = list()
pilha = 0
#par = list()
#impar = list()

for c in range(0,7):
    pilha = int(input(f'\033[35mDigite o {c+1}º valor: \033[m'))
    if pilha % 2 == 0:
        lista[0].append(pilha)
        #par.append(pilha)
    else:
        lista[1].append(pilha)
        #impar.append(pilha)

lista[0].sort()
lista[1].sort()
#par.sort()
#impar.sort()
#lista.append(par[:])
#lista.append(impar[:])

print('\033[1;34mOs valores pares digitados foram:\033[35m {}'.format(lista[0]))
print(f'\033[1;34mOs valores impares digitados foram: \033[35m{lista[1]}')