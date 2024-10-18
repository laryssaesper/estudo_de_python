import smtplib
import tkinter as tk

def mailsender():
    emailOrigem=origem.get()
    emailDestino=destino.get()
    assunto=assuntoTexto.get()
    corpo=corpoTexto.get('1.0', tk.END) #para o text
    mensagem = f"Subject: {assunto}\n\n{corpo}" #'subject' necessário

    #conexão
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls() #inicio
        server.login(emailOrigem, "senha")
        server.sendmail(emailOrigem, emailDestino, mensagem)
        server.quit() #fim
        print("E-mail enviado com sucesso para: ", emailDestino)

    except Exception as e:
        print("Falha ao enviar o e-mail para: ", emailDestino, e)

root=tk.Tk() #cria janela
root.title("Mail-Sender") #nome da janela
root.geometry('1000x500') #tamanho
root.configure(bg='pink', border=20)

#origem = tk.Entry(root).grid(column=2, row=1) retorna none
origemLb = tk.Label(root, bg='pink', fg='purple', font='Georgia 12', text='Seu e-mail').grid(column=1, row=1)
origem = tk.Entry(root, width=50, font='Georgia 12', fg='Hot pink')
origem.grid(column=2, row=1, pady=10)

destinoLb = tk.Label(root, bg='pink', fg='purple', font='Georgia 12', text='Email do Remetente').grid(column=1, row=2)
destino = tk.Entry(root, width=50, font='Georgia 12', fg='Hot pink')
destino.grid(column=2, row=2, pady=10)

assuntoLb = tk.Label(root, bg='pink', fg='purple', font='Georgia 12', text='Assunto').grid(column=1, row=3)
assuntoTexto = tk.Entry(root, width=50, font='Georgia 12', fg='Hot pink')
assuntoTexto.grid(column=2, row=3, pady=10)

corpoLb = tk.Label(root, bg='pink', fg='purple', font='Georgia 12', text='Corpo do Texto').grid(column=1, row=4)
corpoTexto = tk.Text(root, width=50, height=10, font='Georgia 12', fg='Hot pink')
corpoTexto.grid(column=2, row=4, pady=10)

#botoes
btnEnviar = tk.Button(root, bg='hot pink', fg='white', text='ENVIAR', command=mailsender).grid(column=1, row=7, pady=10)
btnSair = tk.Button(root, bg='hot pink', fg='white', text='SAIR', command=root.destroy).grid(column=2, row=7, pady=10)

root.mainloop() #inicia a janela