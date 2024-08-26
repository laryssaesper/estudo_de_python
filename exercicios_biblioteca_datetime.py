import datetime

niver=datetime.date(2006, 5, 22) #organizado de forma ano, mês e dia
print(niver)
print(niver.ctime()) #função .ctime() usada para formatar a data

#para acessar um dado específico
ano=niver.year
mes=niver.month
dia=niver.day
print(dia, mes, ano)

#para alterar algum dado
novo_dia=niver.replace(year=2024)
print(novo_dia)

#dados atuais
tudo=datetime.datetime.now() #pega data e hora atuais
print(tudo)

hoje=datetime.date.today() #data de hoje
print(hoje)