n1 = float(input('Digite a largura da parede em metros: '))
n2 = float(input('Digite a altura da parede em metros: '))
a = n1 * n2     #area da parede
b = a/2         #qtdade de tinta
print('A parede de {}m x {}m tem area de {}m²\nA quantidade de tinta necessaria sera: {:.2f}l'.format(n1, n2, a, b))
