a = 50
print('\033[32m_\033[m'*a)
print(f'\033[1;32m{"SISTEMA DE CADASTRO TRABALHISTA":=^{a}}\033[m')
print('\033[32m-\033[m'*a)

from datetime import datetime

ficha = {}
ficha['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
ficha['idade'] = datetime.now().year - nasc
ficha['ctps'] = int(input('Numero da carteira de trabalho (0 caso nao tenha): '))
if ficha['ctps'] != 0 :
     ficha['contratação'] = int(input('Ano de contrataçao: '))
     ficha['salario'] = float(input('Salario: '))
     ficha['aposentadoria'] = (ficha['idade']) + ((ficha['contratação'] + 35) - datetime.now().year)

print('-='*20)
for c,k in ficha.items():
    print(f'- {c} tem valor {k}.')
