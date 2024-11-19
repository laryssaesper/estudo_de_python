import tkinter as tk
import random
import pygame

# Inicialização do Tkinter
jogo = tk.Tk()
jogo.title('Campo Minado')
jogo.geometry('500x600')
jogo.config(bg='#8efab2')

# Configuração do Pygame
pygame.mixer.init()

def tocar_musica_fundo():
    pygame.mixer.music.load('som.mp3')  # Caminho para a música de fundo
    pygame.mixer.music.play(-1)

tocar_musica_fundo()
explosion_sound = pygame.mixer.Sound("explosao.mpeg")  # Altere para o caminho correto

# Conteúdo da parte de cima (frame superior)
superior = tk.Frame(jogo, bg='#8efab2')
superior.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

timer = tk.Label(superior, font='Helvetica, 20', text='10:00', bg='#8efab2')
timer.pack(side=tk.RIGHT)

inicio = tk.Button(superior, text='INICIAR', command=lambda: [reset_jogo(), cronometro()])
inicio.pack(side=tk.LEFT, padx=5)

sair = tk.Button(superior, text='SAIR', command=jogo.destroy)
sair.pack(side=tk.LEFT, padx=5)

# Frame do botão
principal = tk.Frame(jogo)
principal.pack(pady=5)

bombas = []
matriz_botoes = []

# Funções de tempo
def reset_cronometro():
    timer['text'] = '10:00'

def cronometro(tempo=10*60):
    if tempo >= 0:
        minutos = int(tempo / 60) % 60
        segundos = tempo % 60
        formato = f'{minutos:02}:{segundos:02}'
        timer['text'] = formato
        jogo.after(1000, cronometro, tempo-1)
    else:
        recomecar()

# Função para manipular o clique de cada botão
def clicadordebotao(row, col):
    if (row, col) in bombas:  # Verifica se clicou em uma bomba
        recomecar()  # Chama a função de recomecar
    else:
        matriz_botoes[row][col].config(bg='lightgreen')  # Muda a cor se não for bomba

def recomecar():
    janela = tk.Toplevel(jogo)
    janela.title('Campo Minado')
    janela.geometry('300x300')
    janela.config(bg='red', pady=100)

    recomecarLabel = tk.Label(janela, justify='center', fg='white', bg='red', font='Helvetica, 25', text='VOCÊ PERDEU!')
    recomecarLabel.pack()

    recomecarBtn = tk.Button(janela, justify='center', fg='white', bg='black', text='RECOMEÇAR', command=lambda: [janela.destroy(), jogo.destroy()])
    recomecarBtn.pack(pady=10)

    reset_cronometro()

# Função para gerenciar o estado dos botões
def habilitar_botoes():
    for row in matriz_botoes:
        for button in row:
            button.config(state=tk.NORMAL)  # Habilita o botão

def desabilitar_botoes():
    for row in matriz_botoes:
        for button in row:
            button.config(state=tk.DISABLED)  # Desabilita o botão

# Função para reiniciar o jogo
def reset_jogo():
    global bombas, matriz_botoes
    bombas = random.sample([(r, c) for r in range(10) for c in range(10)], 10)  # 10 bombas aleatórias
    matriz_botoes = []

    for widget in principal.winfo_children():
        widget.destroy()

    for row in range(10):
        linha = []
        for col in range(10):
            button = tk.Button(principal, bg='#105e0a', width=4, height=2, state=tk.DISABLED,  # Inicialmente desabilitado
                               command=lambda r=row, c=col: clicadordebotao(r, c))
            button.grid(row=row, column=col, padx=1, pady=1)
            linha.append(button)
        matriz_botoes.append(linha)

    habilitar_botoes()  # Habilita os botões após reiniciar

reset_jogo()  # Chama a função ao iniciar
jogo.mainloop()
