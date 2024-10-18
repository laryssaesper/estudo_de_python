import smtplib
#pobretech@gmail.com
def mailsender():
    email=str(input("Remetente: "))
    emailDestino=str(input("Destinatário: "))
    assunto=str(input("Assunto: "))
    corpo=str(input("Corpo: "))

    mensagem=f"Subject: {assunto}\n\n{corpo}"

    try:
        server=smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, "google password")
        server.sendmail(email, emailDestino, mensagem)
        print("E-mail enviado com sucesso para: ", emailDestino)

    except Exception as e:
        print("E-mail enviado com sucesso para: ", emailDestino, e)
