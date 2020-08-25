a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE APROVEITAMENTO', a))
print('\033[32m-\033[m'*a)

aluno = {}
aluno['nome'] = str(input('\033[36mdigite o nome do aluno: '))
aluno['media'] = float(input(f'Digite a media de {aluno["nome"]}: '))

if aluno['media'] >= 7 :
    aluno['situaçao'] = 'aprovado'
elif 5 < aluno['media'] < 7 :
    aluno['situaçao'] = 'em recuperaçao'
else:
    aluno['situaçao'] = 'reprovado'

print('\033[32m-=\033[m'*12)
for c,k in aluno.items():
    print(f'\033[1;34m{c} é igual a {k}.')