print('\033[32m_\033[m'*26)
print('\033[1;32mSistema de calculo de IMC!\033[m')
print('\033[32m-\033[m'*26)

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura**2)
print('Seu IMC é: {:.2f}'.format(imc))

if imc < 18.5 :
    print('\033[1;33mVoce esta abaixo do peso!!\033[m')
elif imc > 18.5 and imc < 25 :
    print('\033[1;35mVoce esta no peso ideal!!\033[m')
elif 25 < imc < 30 :
    print('\033[1;33mVoce esta de sobrepeso\033[m')
elif 30 < imc < 40 :
    print('\033[1;33mVoce esta com obesidade!!\033[m')
else:
    print('\033[1;31mVoce esta com obesidade morbida!!\033[m')
