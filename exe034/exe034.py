a = float(input('Digite o salario do funcionario: '))
if a>=1250:
    print('O salario de R${} tera 10% de reajuste e sera de R${}'.format(a, a*1.1))
else:
    print('O salario de R${} tera 15% de reajuste e sera de R${}'.format(a, a * 1.15))
