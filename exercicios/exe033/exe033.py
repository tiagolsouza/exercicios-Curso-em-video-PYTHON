a = int(input('Digite o primeiro numero: '))    #a=3
b = int(input('Digite o segundo numero: '))     #b=2
c = int(input('Digite o terceiro numero: '))    #c=1
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor sera: {}'.format(maior))
print('O menor valor sera: {}'.format(menor))
