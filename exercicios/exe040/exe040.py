print('\033[32m_\033[m'*41)
print('\33[1;32mSistema de calculo das médias dos alunos!\033[m')
print('\033[32m-\033[m'*41)

nota1 = float(input('Digite a primeira nota no aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1+nota2)/2

if media < 5:
    print('\033[1;31mO aluno esta REPROVADO!\033[m')
elif media >=5 and media < 7:
    print('\033[1;32mO aluno esta em RECUPERAÇAO!')
else:
    print('\033[1;35mO aluno esta APROVADO!')
