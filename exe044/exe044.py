print('\033[32m_\033[m'*21)
print('\033[1;32mSistema de descontos!\033[m')
print('\033[32m-\033[m'*21)

produto = float(input('Digite o preço do produto: R$ '))

print('\033[1;34mFORMAS DE PAGAMENTO:\033[m')
print('\033[35mPagamento a vista no dinheiro/cheque--{:->20}\033[m'.format(0))
print('\033[35mPagamento a vista no cartao-----------{:->20}\033[m'.format(1))
print('\033[35mPagamento parcelado no cartao---------{:->20}\033[m'.format('nº de parcelas'))
pag = int(input('\033[1;35m\nDgite a forma de pagamento de acordo com a lista acima:\033[m '))

if pag == 0 :
    print('\033[1;33mVoce escolheu a forma de pagamento a vista no dinheiro ou cheque e tera 10% de desconto.\033[m')
    print('\033[1;33mPortanto, o produto de R${:.2f} saira por: R${:.2f}\033[m'.format(produto, produto*0.9))
elif pag == 1 :
    print('\033[1;33mVoce escolheu a forma de pagamento a vista no cartão e tera 5% de desconto.\033[m')
    print('\033[1;33mPortanto, o produto de R${:.2f} saira por: R${:.2f}\033[m'.format(produto, produto*0.95))
elif pag == 2 :
    print('\033[1;33mVoce escolheu a forma de pagamento parcelado em 2 vezes no cartão sem desconto.\033[m')
    print('\033[1;33mPortanto, o produto sairá no valor de R${:.2f}\033[m'.format(produto))
else:
    print('\033[1;33mVoce escolheu a forma de pagamento parcelado em {} vezes no cartão com 20% de juros.\033[m'.format(pag))
    print('\033[1;33mPortanto, o produto de R${:.2f} saira por: R${:.2f}. Em {} parcelas de R${:.2f}\033[m'.format(produto, produto * 1.2, pag, ((produto * 1.2)/pag)))
