a = 50
print('\033[32m_\033[m' * a)
print(f'\033[1;32m{"SISTEMA DE IDADE PARA VOTAÇAO":=^{a}}\033[m')
print('\033[32m-\033[m' * a)


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero inteiro.
    :param n: o numero inteiro a ser calculado.
    :param show: Mostra ou nao a conta(opcional).
    :return: retorna o valor do fatorial de n.
    """
    b = 1
    print(f'{n}!=', end='')
    for c in range(n,0, -1):
        b *= c
        if show :
            if c == 1 :
                print(f'{c}=', end='')
            else:
                print(f'{c}x', end='')
    print(f'{b}')


fatorial(5,True)
