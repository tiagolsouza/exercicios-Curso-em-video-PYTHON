print('\033[32m_\033[m'*20)
print('\033[1;32m{:^20}\033[m'.format('SOMA DE IMPARES'))
print('\033[32m-\033[m'*20)

s = 0
for c in range(1,500,2):
    if c % 3 == 0 :
        print(c, end=',')
        s += c
print('\n\033[1;34mAsoma total é: {}\033[m'.format(s))
