print('\033[1;31m_\033[m'*23)
print('\033[1;34mCOMPARADOR DE NUMEROS\033[m')
print('\033[1;31m-\033[m'*23)

primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))

if primeiro > segundo :
    print('\033[1;33mO primeiro valor é maior!\033[m')
elif segundo > primeiro :
    print('\033[1:33mO segundo valor é maior!\033[m')
else:
    print('\033[1;31mOs dois valores sao iguais!\033[m')
