import os
import pathlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template

from dotenv import load_dotenv

load_dotenv()

# Caminho do arquivo HTML
PATH_HTML: Path = pathlib.Path(__file__).parent / 'template' / 'mail_01.html'

# Dados do remetente e destinatário
remetente: str = os.getenv('FROM_EMAIL', '')
destinatario: str = os.getenv('TO_EMAIL', '')

# Dados do servidor SMTP
smtp_server: str = os.getenv('SMTP_SERVER', '')
smtp_port: int = int(os.getenv('SMTP_PORT', '587'))
smtp_username: str = os.getenv('SMTP_USER', '')
smtp_password: str = os.getenv('EMAIL_PASSWORD', '')

# Criando a mensagem
with open(PATH_HTML, 'r') as file:
    texto_arquivo: str = file.read()
    template: Template = Template(texto_arquivo)
    texto_email: str = template.substitute(nome='Naty')

# Trnasformando o HTML em MIMEMultipart
msg_multipart: MIMEMultipart = MIMEMultipart()
msg_multipart['from'] = remetente
msg_multipart['to'] = destinatario
msg_multipart['subject'] = 'Teste de envio de e-mail com Python'

corpo_email: MIMEText = MIMEText(texto_email, 'html', 'utf-8')
msg_multipart.attach(corpo_email)

# Enviando o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.send_message(msg_multipart)

    print('E-mail enviado com sucesso!')
