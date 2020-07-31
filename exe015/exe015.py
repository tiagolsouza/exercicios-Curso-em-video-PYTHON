dias = int(input('Digite a quantidade de dias que utilizou o veiculo: '))
km = float(input('Digite a quantidade de quilometros percorridos: '))
totdias = dias*60
totkm   = km*0.15
total   = totdias+totkm
print(f'O total a ser pago pelo aluguel do veiculo sera de: R${total}')
print(type(total))
