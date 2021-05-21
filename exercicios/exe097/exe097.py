a = 50
print('\033[32m_\033[m' * a)
print(f'\033[1;32m{"SISTEMA DE IMPRESSAO REDIMENSIONAVEL":=^{a}}\033[m')
print('\033[32m-\033[m' * a)


def imp(txt):
    tm = int(len(txt) + 4)
    print('\033[1;34m~\033[m' * (tm))
    print(f'\033[1;35m{txt:^{tm}}')
    print('\033[1;34m~\033[m' * (tm))


texto = str(input('Escreva um texto: '))
imp(texto)