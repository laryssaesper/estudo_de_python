#LISTA DE EXERCÍCIOS 26 DE AGOSTO DE 2024
#1 - Crie uma aplicação que leia 2 números e um nome, processe a média desses número e exiba os dados. A leitura dos dados deve ser feita via teclado (input).
print("EXERCÍCIO 1\n")
print("Qual é o seu nome?")
nome=str(input("O meu nome é: "))
num1=float(input("Digite um número: "))
num2=float(input("Digite outro número: "))
media:float=(num1+num2)/2
print(f"Olá {nome}, tudo bem? Os números que você digitou foram {num1} e {num2}, respectivamente. Também, a média deles foi de {media}.")

#2 - Desenvolva um programa capaz de calcular a área do quadrado, fazendo a leitura das dimensões via teclado.
#Área=L^2 ou L*L
print("\nEXERCÍCIO 2\n")
print(f"{nome}, agora vamos calcular a área de um quadrado!")
lado=float(input("Qual é o tamanho do lado do quadrado? "))
calculo:int=lado**2
print("Área do quadrado é igual a: ", calculo)

#3 - Desenvolva um programa capaz de exibir a hora e data atual do sistema.
import datetime #biblioteca especial com comandos para manipulação de data e hora
data=datetime.datetime.now()
print(data)