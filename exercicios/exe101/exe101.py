a = 50
print('\033[32m_\033[m' * a)
print(f'\033[1;32m{"SISTEMA DE IDADE PARA VOTAÇAO":=^{a}}\033[m')
print('\033[32m-\033[m' * a)


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'\033[34mCom {idade} anos: Nao vota.'
    elif 16<= idade < 18 or idade >65 :
        return f'\033[34mCom {idade} anos : Voto opcional.'
    else:
        return f'\033[34mCom {idade} anos: Voto obrigatorio.'


nasc = int(input('\033[35mEm que ano voce nasceu? '))
print(voto(nasc))
