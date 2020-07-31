from math import hypot
x = float(input('Digite o comprimento do cateto adjacente: '))
y = float(input('Digite o comprimento do cateto oposto: '))
h = hypot(x,y)
print('O valor da hipotenusa sera: {:.3f}'.format(h))
