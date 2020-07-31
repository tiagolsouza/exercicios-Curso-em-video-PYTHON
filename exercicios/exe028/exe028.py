from random import randint
from time import sleep
a = randint(0,5)
b = int(input('Descubra o numero escolhido de 0 a 5: '))
print('Processando...')
sleep(3)
print('Parabens, voce acertou!' if b==a else 'Tente novamente!')