'''Escrever um programa para aprovar um emprestimo bancario, a mensalidade deve ser menor que 30%
   do salario do meliante'''

print('\033[34m_\033[m'*57)
print('\033[1;32mBem vindo ao sistema de aprovaçao de imprestimo bancario\033[34m|\033[m')
print('\033[34m-\033[m'*57)
casa = float(input('Primeiramente digite o valor da casa que deseja comprar: '))
salario = float(input('Em seguida, digite o seu salario mensal: '))
prazo = float(input('Por ultimo, digite quantos anos vc pretende pagar o imprestimo: '))

mensalidade = casa / (prazo * 12)
print('mens: {}'.format(mensalidade))
print('30% do salario= {}'.format(salario*0.30))

if mensalidade <= salario*0.30 :
    print('\033[1;32mParabens, voce tem direito a um emprestimo para comprar sua casa!\033[m')
else:
    print('\033[1;31mInfelismente, voce nao possui o perfil necessario para realizar imprestimo!\033[m')
