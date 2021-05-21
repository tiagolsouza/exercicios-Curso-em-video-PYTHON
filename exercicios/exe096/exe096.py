a = 50
print('\033[32m_\033[m' * a)
print(f'\033[1;32m{"SISTEMA DE CALCULO DE AREA":=^{a}}\033[m')
print('\033[32m-\033[m' * a)


def area(a, b):
    tot = a * b
    print(f'\033[1;34mA area de um terreno de {a:.2f} x {b:.2f} é de {tot:.2f}m².\033[m')


larg = float(input('\033[35mLargura do terreno (m): '))
comp = float(input('\033[35mComprimento do terreno (m): '))
area(larg, comp)
