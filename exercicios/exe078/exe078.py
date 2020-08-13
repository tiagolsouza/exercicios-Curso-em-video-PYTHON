a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE IDENTIIFADOR DE MAXIMOS E MINIMOS', a))
print('\033[32m-\033[m'*a)

'''a = [int(input('Digite um numero inteiro: ')), int(input('Digite um numero inteiro: '))
     int(input('Digite um numero inteiro: ')), int(input('Digite um numero inteiro: '))
     int(input('Digite um numero inteiro: '))]
'''
b = []
men=mai= 0

for c in range(0,5):
    b.append(int(input('\033[1;35mDigite um numero inteiro: ')))
    if c == 0:
        men=mai=b[0]
    else:
        if b[c] > mai:
            mai = b[c]
        if b[c] < men:
            men = b[c]

print(f'\033[1;34mVoce digitou os valores {b}')
print(f'\033[1;34mO maior valor digitado foi {mai} nas posiçoes: ', end='')
for i, v in enumerate(b):
    if v == mai :
        print(f'{i}..', end='')
print()
print(f'\033[1;34mO maenor valor digitado foi {men} nas posiçoes: ', end='')
for i, v in enumerate(b):
    if v == men :
        print(f'{i}..', end='')
print()


#print(f'\033[34mO menor numero digitado foi {min(b)}, na posiçao {b.index(min(b))+1}')
#print(f'\033[34mO maior numero digitado foi {max(b)}, na posiçao {b.index(max(b))+1}')
