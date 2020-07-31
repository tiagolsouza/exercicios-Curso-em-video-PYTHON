a = 25
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE TABUADAS', a))
print('\033[32m-\033[m'*a)

tab = 0

while True:
    tab = int(input('\033[36mDigite o valor da tabuada (ou um valor negativo para sair): '))
    print('\033[34m-' * 15)
    if tab < 0:
        break
    for c in range(1,11):
        print(f'\033[1;35m{tab} x {c:2} = {tab*c}\033[m')
    print('\033[34m-'*15)
print('SISTEMA DE TABUADAS ENCERRADA. Volte sempre!')