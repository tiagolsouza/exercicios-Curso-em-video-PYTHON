km = int(input('Digite a distancia da viagem em km: '))

#preco = km*0.50 if km<=200 else km*0.45

if km<=200:
    print('O valor da passagem sera: R${}'.format(km*0.5))
else:
    print('O valor da passagem sera R${}'.format(km*0.45))
