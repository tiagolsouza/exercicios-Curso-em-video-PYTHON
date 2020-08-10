a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE DETECÇAO DE NUMEROS', a))
print('\033[32m-\033[m'*a)

nove = 0
par = '0'
num1 = int(input('\033[35mDigite um numero inteiro: '))
num2 = int(input('\033[35mDigite um numero inteiro: '))
num3 = int(input('\033[35mDigite um numero inteiro: '))
num4 = int(input('\033[35mDigite um numero inteiro: '))

tupla = (num1, num2, num3, num4)

for c in range(0,4):
    if tupla[c] == 9 :
        nove +=1
    if tupla[c]%2 == 0:
        par[c] = str(tupla[c])
print('\033[33m-='*15)
print(f'\033[1;34mApareceram {nove} vezes o valor 9.')
print(f'\033[1;34mO valor 3 foi digitado primeiramente na {tupla.index(3)+1} posiçao.'if tupla.count(3) != 0 else 'Nao houve 3')
print(par)