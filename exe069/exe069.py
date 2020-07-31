a = 25
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE IDENTIFICAÇAO DE IDADE E SEXO', a))
print('\033[32m-\033[m'*a)

idade = contid = conthom = contmul = 0
sexo = cont = 'o'

while True:
    print('\033[1;33mCADASTRE UMA PESSOA!')
    print('\033[36m-'*25)
    idade = int(input('\033[36mDigite a idade: '))
    while sexo not in 'MF' :
        sexo = str(input('\033[36mDigite o sexo [M/F]: \033[m')).upper()[0]
    print('\033[36m-' *25)
    if idade > 17 :
        contid += 1
    if sexo in 'M' :
        conthom += 1
    if sexo in 'F' :
        if idade < 21 :
            contmul += 1
    while cont not in 'SN' :
        cont = str(input('\033[1;35mContinuar? [S/N] \033[m')).upper()[0]
    if cont == 'N' :
        print('\033[33mENCERRADO!\033[m')
        break
    sexo = cont = 'o'
    print('\033[36m-_' * 13)
print(f'\033[1;34mAo total:\n{contid} tem mais de 18 anos.\n{conthom} homens foram cadastrados.\n{contmul} mulheres tem menos de 20 anos\033[m')
