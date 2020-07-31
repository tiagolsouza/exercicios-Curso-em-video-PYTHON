a = 30
print('\033[32m_\033[m'*a)
print('\033[1;32m{:=^{}}\033[m'.format('VALIDAÇÃO DE PALÍNDROMOS',a))
print('\033[32m-\033[m'*a)

frase = str(input('Digite uma frase: ')).lower().split()
frase = ''.join(frase)
tamanho = len(frase)
resultado = ('é um palíndromo!!')
print(frase)

for c in range(0,tamanho):
    if frase[c] != frase[tamanho-1-c] :
        resultado = ('não é um palíndromo!!')
print('\033[1;34mA frase digitada \033[4m{}\033[m'.format(resultado))

'''inverso = ''
    for letra in range(tamanho-1, -1, -1):
      inverso += frase[letra]
      
    ou
    inverso = frase[::-1]
    
    if inverso == frase :
      print('é palindromo')
    else:
      print('nao e palindromo')'''
