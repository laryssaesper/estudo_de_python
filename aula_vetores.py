#vetores
#comporta conteúdos de mesmo tipo
#exemplo: lista de compras
list=["banana", "arroz", "feijão", "frango"]
print(list[1]) #imprime arroz
print(list[-1]) #imprime feijão, contando de trás para frente

#comandos de manipulação
list.append("abacaxi") #adiciona o conteúdo no final do vetor
print(list)
del list[2] #remove o conteúdo da posição desejada
print(list)
list.remove("frango") #remove ítem pelo conteúdo
print(list)
list.insert(3, "batata") #insere item aonde deseja
print(list)
aux=list.pop(0) #joga conteúdo para variável auxiliar a fim de recuperação caso necessário
print(list)
