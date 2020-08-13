a = 50
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('SISTEMA DE IDENTIIFADOR DE VOGAIS', a))
print('\033[32m-\033[m'*a)

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\n\033[34mNa palavra {p} temos: \033[m', end='')
    for v in p:
        if v.lower() in 'aeiou':
            print(f'\033[35m{v}', end=' ')
