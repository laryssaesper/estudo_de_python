#Uso de funções
#Sintaxe
#def nome (parametros):

#crie um programa que receba do usuário o número de repetições e serem executadas as operações
#matemáticas básicas. Cada operação deve possuir sua função e devem ser chamadas por meio de um loop

x=(int(input("Digite o número de vezes em que o looping irá acontecer: ")))
a=(float(input("Digite seu número: ")))
b=(float(input("Digite seu outro número: ")))

def soma (a, b):
    result=(a+b)
    return result

def sub (a, b):
    result=(a-b)
    return result

def multi (a, b):
    result=(a*b)
    return result

def subt (a, b):
    result=(a/b)
    return result

for i in range(x):
    print(soma (a, b))
    print(sub (a, b))
    print(multi (a, b))
    print(subt (a, b))
