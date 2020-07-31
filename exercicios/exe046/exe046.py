print('\033[32m_\033[m'*20)
print('\033[1;32m{:^20}\033[m'.format('CONTAGEM REGRESSIVA'))
print('\033[32m-\033[m'*20)

from time import sleep

#for c in range(11,-1,-1):
for c in range(11,0,-1):
    sleep(1)
    print('\033[1;32m{}\033[m'.format(c-1))
print('\033[1;35mACABOOOOU\033[m')
