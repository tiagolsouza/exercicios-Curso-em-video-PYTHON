print('\033[32m_\033[m'*41)
print('\33[1;32mSistema de teste de traingulos!\033[m')
print('\033[32m-\033[m'*41)

r1 = float(input('digite o valor da 1ª reta: '))
r2 = float(input('digite o valor da 2ª reta: '))
r3 = float(input('digite o valor da 3ª reta: '))
#if r1<r2+r3 and r2<r3+r1 and r3<r1+r2:

if (abs(r1-r2)<r3<(r1+r2)) and (abs(r2-r3)<r1<(r2+r3)) and (abs(r3-r1)<r2<(r3+r1)):
    if r1 == r2 and r1 == r3 :  #r1 == r2 == r3
        print('\033[1;35mO triangulo formado é do tipo: \033[4mEQUILATERO\033[m')
    elif r1 == r2 or r1 == r3 or r2 == r3 :
        print('\033[1;35mO triangulo formado é do tipo: \033[4mISOSCELES\033[m')
    else:       #r1 != r2 != r3 != r1
        print('\033[1;35mO triangulo formado é do tipo: \033[4mESCALENO\033[m')
else:
    print('\033[1;31mAs retas nao formam trinagulo!!\033[m')