from math import sin, cos, tan, radians
ang = float(input('Digite o valor do angulo em graus: '))
r = radians(ang)
print('O valor do seno sera: {:.2f},\nO valor do cosseno sera: {:.2f},\nO valor da tangente sera: {:.2f}'.format(sin(r), cos(r), tan(r)))
