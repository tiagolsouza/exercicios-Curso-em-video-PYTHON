print('\033[32m_\033[m'*20)
print('\033[1;32m{:=^20}\033[m'.format('TABOADA'))
print('\033[32m-\033[m'*20)

s = int(input('\033[1;34mDigite um numero pra ver sua taboada: \033[m'))
for c in range(1,11):
    print('\033[32m{:2}x{:2} = {:2}\033[m'.format(c,s,c*s))
print('\033[1;34m------\nFiM\033[m')
