import smtplib
from tkinter import *
from tkinter import ttk

#criar um mail-sender, utilizando ferramenta visual que permita ao usuário escrever o endereço em texto

def mailsender():
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, "bpyw isbg iwtk icvv")
    server.sendmail(email, emailDestino, mensagem)
    print("E-mail enviado com sucesso para: ", emailDestino)

root=Tk()
root.title("Mail-Sender")
sender=ttk.Frame(root, padding=20)
sender.grid()

remetente=ttk.Label(sender, text="Remetente: ").grid(column=1, row=1)
destino=ttk.Label(sender, text="Destinatario: ").grid(column=1, row=2)
assunto=ttk.Label(sender, text="Assunto: ").grid(column=1, row=3)
corpo=ttk.Label(sender, text="Corpo: ").grid(column=1, row=4)



ttk.Button(sender, text="Sair", command=root.destroy).grid(column=1, row=5)

root.mainloop()
