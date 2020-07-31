from datetime import date

print('\033[32m_\033[m'*41)
print('\33[1;32mSistema de classificaçao etaria do atleta!\033[m')
print('\033[32m-\033[m'*41)

niver = int(input('Digite o ano de nascimento do(a) atleta: '))
faixa = date.today().year - niver

print('O(A) atleta tem {} ano(s)!'.format(faixa))
if faixa < 9 :
    print('\033[1;35mO(A) atleta esta na classificaçao MIRIM!!\033[m')
elif faixa > 9 and faixa < 14 :
    print('\033[1;35mO(A) atleta esta na classificaçao infantil!!\033[m')
elif faixa > 14 and faixa < 19 :
    print('\033[1;35mO(A) atleta esta na classificaçao JUNIOR!!\033[m')
elif faixa > 19 and faixa < 20 :
    print('\033[1;35mO(A) atleta esta na classificaçao SENIOR!!\033[m')
else:
    print('\033[1;35mO(A) atleta esta na classificaçao MASTER!!\033[m')
