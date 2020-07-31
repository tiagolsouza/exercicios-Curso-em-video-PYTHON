a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('VALIDAÇAO DE SEXO',a))
print('\033[32m-\033[m'*a)

nome = str(input('\033[1;35mOla, digite seu nome: \033[m')).capitalize()
sexo = 'o'

while sexo not in 'MF':
    sexo = str(input('\033[1;32mDigite seu sexo [M/F]: \033[m')).strip().upper()[0]
    if sexo not in 'MF' :
        print('\033[1;31m{}, voce nao digitou seu sexo corretamente, por favor tente novamente!\033[m'.format(nome))
    print(sexo)
print('\033[1;34mOla, {}, seu sexo é {}\033[m'.format(nome, sexo))
