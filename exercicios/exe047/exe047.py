print('\033[32m_\033[m'*20)
print('\033[1;32m{:^20}\033[m'.format('NUMEROS PARES'))
print('\033[32m-\033[m'*20)

for c in range(2,51,2):
    print(c, end=' ')
print('\n\033[1;31mFIM\033[m')
