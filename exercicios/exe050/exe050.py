print('\033[32m_\033[m'*20)
print('\033[1;32m{:=^20}\033[m'.format('SOMA DE PARES'))
print('\033[32m-\033[m'*20)

s = 0
for c in range(0,6):
    valor = int(input('\033[1;35mDigite um valor inteiro: \033[m'))
    teste = valor % 2
    if teste == 0 :
        s += valor
print('\033[1;33mO resultado da soma foi: {}'.format(s))
print('\033[1;34mFIM\033[m')
