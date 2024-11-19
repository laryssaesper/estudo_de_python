import tkinter as tk

def sum():
    try:
        n1=float(n1Entry.get())
        n2=float(n2Entry.get())
        result=n1+n2
        resultLabel.config(text=f'O resultado é {result}')
    except Exception as e:
        resultLabel.config(fg='red', text='Digite um número válido')

def sub():
    try:
        n1=float(n1Entry.get())
        n2=float(n2Entry.get())
        result=n1-n2
        resultLabel.config(text=f'O resultado é {result}')
    except Exception as e:
        resultLabel.config(fg='red', text='Digite um número válido')

def mult():
    try:
        n1=float(n1Entry.get())
        n2=float(n2Entry.get())
        result=n1*n2
        resultLabel.config(text=f'O resultado é {result}')
    except Exception as e:
        resultLabel.config(fg='red', text='Digite um número válido')

def div():
    try:
        n1=float(n1Entry.get())
        n2=float(n2Entry.get())
        result=n1/n2
        resultLabel.config(text=f'O resultado é {result}')
    except Exception as e:
        resultLabel.config(fg='red', text='Digite um número válido')

janela=tk.Tk()
janela.title('Calculadora')
janela.geometry('600x300')
janela.config(bg='#C9FFC3', border=20)

n1Label=tk.Label(janela, bg='#C9FFC3', font=10, text='Digite seu primeiro número', padx=10).grid(column=1, row=1)

n1Entry=tk.Entry(janela, font=10)
n1Entry.grid(column=2, row=1)

n2Label=tk.Label(janela, bg='#C9FFC3', font=10, text='Digite seu segundo número', padx=10).grid(column=1, row=2)

n2Entry=tk.Entry(janela, font=10)
n2Entry.grid(column=2, row=2)

#resultado
resultLabel=tk.Label(janela, bg='#C9FFC3', fg='#9901FF', font=16 , text='O resultado é:')
resultLabel.grid(column=1, row=5, pady=20)

#botoes
sumBtn=tk.Button(janela, text='SOMAR', command=sum).grid(column=1, row=6)

subBtn=tk.Button(janela, text='SUBTRAIR', command=sub).grid(column=1, row=7)

multBtn=tk.Button(janela, text='MULTIPLICAR', command=mult).grid(column=1, row=8)

divBtn=tk.Button(janela, text='DIVIDIR', command=div).grid(column=1, row=9)

sair=tk.Button(janela, text='SAIR', command=janela.destroy).grid(column=1, row=10)

janela.mainloop()
