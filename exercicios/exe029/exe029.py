a = float(input('Qual a velocidade do veiculo? '))
if a<=80:
    print('Segue o baile!')
else:
    b = (a-80)*7
    print('Voce estava {:.2f}km/h acima da velocidade limite, portanto vai pagar R${:.2f} de multa'.format(a-80, b))
