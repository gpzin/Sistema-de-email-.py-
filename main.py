import smtplib
import email.message

def enviar_email(): 
    
    corpo_email = '''
    <!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Document</title>
  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      background-color: rgb(255, 255, 255);
      text-align: center;
      margin: 0;
      padding: 0;
    }

    .mensagem {
      max-width: 730px;
      margin: 50px auto;
      padding: 50px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    .mensagem > img {
        max-width: 730px;
        padding-top: 10px;
    }

    .button-link {
      background-color: rgb(255, 231, 13);
      padding: 10px 10px;
      border: none;
      border-radius: 10px;
      cursor: pointer;
    }

    .button-link > a {
      color: #000000;
      text-decoration: none;
    }
  </style>
</head>
<body>
  <div class="mensagem">
    <h1>Olá, este é um e-mail de verificação !</h1>
    <p>
      Para confirmar que tem acesso e validar seu cadastro, clique no botão
      abaixo:
    </p>
    <button class="button-link">
      <a href="https://github.com/gpzin">Clique aqui</a>
    </button>
    <img
      src="https://img.freepik.com/vetores-gratis/ilustracao-de-conceito-confirmada_114360-5400.jpg?w=740&t=st=1715016559~exp=1715017159~hmac=097f033e64d19c2d7d27ce7a1291b57938e3357affbaea3625d7737d61fc60f4"
    />
  </div>
</body>
</html>
    '''

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'pgv621@gmail.com'
    msg['To'] = 'glaucosantos@faeterj-petropolis.edu.br'
    password = 'gdfppnwatfcpmmvp' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('E-mail enviado')
enviar_email()