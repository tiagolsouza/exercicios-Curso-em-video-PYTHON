a = 35
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE CAIXA ELETRONICO', a))
print('\033[32m-\033[m'*a)

'''saque = not50 = not20 = not10 = not1 = 0

saque = int(input('\033[1;36mQuanto você quer sacar? R$'))

not50 = saque // 50
saque = saque - (not50*50)
not20 = saque // 20
saque = saque - (not20*20)
not10 = saque // 10
saque = saque - (not10*10)
not1 = saque // 1
saque = saque - (not1*1)

print(f'Notas de 50: {not50}')
print(f'Notas de 20: {not20}')
print(f'Notas de 10: {not10}')
print(f'Notas de 1: {not1}')'''

saque = int(input('\033[1;36mQuanto você quer sacar? R$'))
total = saque
ced = 50
totalced = 0

while True :
    if total >= ced :
        total -= ced
        totalced += 1
    else:
        if totalced > 0 :
            print(f'\033[1;34mTotal de {totalced} cedulas de R${ced}')
        if ced == 50 :
            ced = 20
        elif ced == 20 :
            ced = 10
        elif ced == 10 :
            ced = 1
        totalced = 0
        if total == 0 :
            break
print('\033[1;33mFIM')