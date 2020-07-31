
r1 = float(input('digite o valor da 1ª reta: '))
r2 = float(input('digite o valor da 2ª reta: '))
r3 = float(input('digite o valor da 3ª reta: '))
#if r1<r2+r3 and r2<r3+r1 and r3<r1+r2:
if (abs(r1-r2)<r3<(r1+r2)) and (abs(r2-r3)<r1<(r2+r3)) and (abs(r3-r1)<r2<(r3+r1)):
    print('ok')
else:
    print('fck')
