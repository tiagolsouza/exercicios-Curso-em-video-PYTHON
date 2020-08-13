a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE VALIDAÇAO DE EXPRESSOES MATEMATICAS', a))
print('\033[32m-\033[m'*a)


expr = str(input('\033[1;35mDigite a expressao: \033[m'))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('\033[1;34mSua expressao esta valida!\033[m')
else:
    print('\033[1;31mSua expressao esta errada!\033[m')
