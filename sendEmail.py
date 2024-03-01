import smtplib

def getEmail(datasetEmail):
    try:
        servidor_gmail = smtplib.SMTP('smtp.gmail.com', 587)
        servidor_gmail.starttls()
        
        # Substitua pela sua senha de aplicativo se a autenticação de dois fatores estiver ativada
        servidor_gmail.login('dmls@cin.ufpe.br', 'pqjpsbzaaeqwizgx')
        remetente = 'dmls@cin.ufpe.br'
        destinatarios = datasetEmail
        conteudo = 'Olá, Pauline, Caio e Emmanuel. Este é um email de teste.'.encode('utf-8')
        servidor_gmail.sendmail(remetente, destinatarios, conteudo)
        servidor_gmail.quit()

        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")




