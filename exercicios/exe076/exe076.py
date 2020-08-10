a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE LISTA DE PREÇOS DE SUPERMERCADO', a))
print('\033[32m-\033[m'*a)

lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Trensferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)

print('\n')
print('\033[1;34m-\033[m'*40)
print('\033[1;34m{:^40}\033[m'.format('Lista de preços'))
print('\033[1;34m-\033[m'*40)

for c in range(0,18,2):
    print('\033[1;35m{:.<25}R${: >8}\033[m'.format(lista[c], lista[c+1]))
print('\033[1;34m-\033[m'*40)
