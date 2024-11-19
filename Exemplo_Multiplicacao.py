#ler dois números
num_a=int(input("Digite seu número A: "))
num_b=int(input("digite seu número B: "))
if num_a==num_b:
    c=num_a+num_b
    print(f"\nSeus números são iguais e a soma deles é {c}")
else:
    c=num_a*num_b
    print(f"\nSeus números são diferentes e o resultado a multiplicação entre eles é {c}")
