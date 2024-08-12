#digitar suas três últimas vendas
print("Digite suas três últimas vendas dessa semana.")
venda1=float(input("\nDigite sua primeira venda: "))
venda2=float(input("\nDigite sua segunda venda: "))
venda3=float(input("\nDigite sua terceira venda: "))
total=venda1+venda2+venda3
media=total/3
#calcular bônus
if total<=120:
    bonus=(total*10)/100
else:
    bonus=(total*20)/100
#demonstração final
print(f"\nSuas vendas foram de {venda1}, {venda2} e {venda3}.\nSeu total foi de {total}.\nSua média foi de {media}.\nSeu bônus foi de {bonus}.")
