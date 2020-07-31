nome = str(input('Digite seu nome completo: ')).strip().title().split()
tamanho= int(len(nome))
print('Ola, {} {}, bem vindo(a)!!'.format(nome[0], nome[tamanho-1]))
