from datetime import date
ano = int(input('Informe o ano do seu nascimento: '))
alist = date.today().year - ano

if alist == 18:
    print('\033[1;32mParabens, ja esta na hora de vc se alistar ao serviço militar!!\033[m')
elif alist <= 18:
    print('\033[1;34mVoce ainda nao tem idade suficiente para se alistar, falta(m) {} ano(s) para seu alistamento!!\033[m'.format(18-alist))
else:
    print('\033[1;31mVoce passou do tempo de alistamento em {} ano(s), apresente-se imediatamente a um posto militar!!\033[m'.format(abs(18-alist)))
