frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira posiçao da letra A aparece em: {}'.format(frase.find('A')+1))
print('A ultima posiçao da letra A aparece em: {}'.format(frase.rfind('A')+1))
