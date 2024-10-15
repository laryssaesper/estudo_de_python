import smtplib
#pobretech@gmail.com

email=str(input("Remetente: "))
emailDestino=str(input("Destinatário: "))

assunto=str(input("Assunto: "))
corpo=str(input("Corpo: "))

mensagem=f"Assunto: {assunto}\n\n{corpo}"

server=smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "bpyw isbg iwtk icvv")

server.sendmail(email, emailDestino, mensagem)

print("E-mail enviado com sucesso para: ", emailDestino)
