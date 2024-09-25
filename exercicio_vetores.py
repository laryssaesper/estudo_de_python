#utilizando vetores, crie um programa que leia o nome, n1 e n2 de x alunos, confore o interesse do usuário
#e após a digitação mostre a média dos alunos
#nome e notas
#nome e média

media=float
nomes=[]
nota1=[]
nota2=[]
medias=[]
const=int(input("Quantos alunos você quer cadastrar? "))
for i in range(const):
    nome=str(input("Digite o nome do aluno: "))
    nota_1=float(input("Digite sua primeira nota: "))
    nota_2=float(input("Digite sua segunda nota: "))
    nomes.append(nome)
    nota1.append(nota_1)
    nota2.append(nota_2)
    media=(nota_1+nota_2)/2
    medias.append(media)
    print("-"*50)
print(nomes, medias)
