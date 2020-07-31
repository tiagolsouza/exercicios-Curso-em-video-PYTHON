a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('TESTE DE PESO',a))
print('\033[32m-\033[m'*a)

media = 0
nomevelho = 'não houve'
velho = 0
nova = 0

for c in range(0,4):
    nome = str(input('\033[1;33mDigite o nome da {}ª pessoa: '.format(c+1)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c+1)))
    sexo = str(input('''[M] masculino.
[F] Feminino.
Digite seu sexo de acordo com a tabela acima: ''')).upper()
    print('---\033[m')
    media += idade
    if sexo == 'M' :            #sexo in 'Mn'
        if velho < idade :
            velho = idade
            nomevelho = nome
    else:
        if idade < 20 :
            nova += 1
media=(media/4)
print('''\033[1;34mA media de idade do grupo é: {}.
O nome do homem mais velho é: {}.
E finalmente há {} mulheres menores de 20 anos.\033[m'''.format(media, nomevelho, nova))
