#ciar um jogo de adivinhação, onde o sistema deve escolher um número entre 1 e 100
#para isso, você terá que pesquisar a função random
#o usuário deve ter direito a três tentativas
#após isso (game over)

import random

i=0
random.randint(1,100)
while i < 3:
    i=i+1
    num=(int(input("Digite um número: ")))
    if num==i:
        print("VENCEU")
    else:
        print("TENTE NOVAMENTE")

print("GAME OVER")
