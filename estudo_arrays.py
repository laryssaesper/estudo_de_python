import numpy as np

#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
vet1=[]
for i in range(0, 5):
    a=int(input("Escreva um número para ser adicionado na lista: "))
    vet1.append(a)
print(vet1)

#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vet1.reverse()
print(vet1)

#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas=[]
for i in range(0, 4):
    nota=float(input(f"Digite sua {i+1} nota: "))
    notas.append(i)
print(notas)
print("A média de suas notas é: ", np.mean(nota))