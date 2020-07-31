a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('VALIDAÇÃO DE NUMEROS PRIMOS', a))
print('\033[32m-\033[m'*a)

primo = int(input('\033[1;32mDigite um numero inteiro pra testar se é primo: \033[m'))
teste = ('é primo')
resto = 0

for c in range(2,primo):
    resto = primo % c
    if resto == 0 :
        teste = ('não é primo')
print('\033[1;34mO numero digitado {}\033[m'.format(teste))
