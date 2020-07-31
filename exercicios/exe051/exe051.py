a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('PROGRESSÃO ARITMETICA', a))
print('\033[32m-\033[m'*a)

prog = int(input('\033[1;35mDigite o primeiro termo da progressão aritmetica: '))
raz = int(input('Digite a razão da progressão: \033[m'))

print('(', end='')
for c in range(0,10):
    print(prog, end=',')
    prog += raz
print(')')
print('FIM')

'''decimo=primeiro+(10-1)*razao
for  c in range(prog,decimo+razao, razao):
    print('{}'.format(c), end='>')'''