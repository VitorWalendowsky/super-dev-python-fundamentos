from dotenv import load_dotenv
from os import getenv

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#Carrega as variaveis de dentro do arquivo .env para as variaveis de ambiente
load_dotenv()

def __obter_login() -> str:
    email = getenv("EMAIL")
    if email is None:
        raise Exception("Login nao esta preenchido no arquivo .env")
    
    return email

def __obter_senha() -> str:
    senha = getenv("SENHA")
    if senha is None:
        raise Exception("Senha nao esta preenchido no arquivo .env")
    
    return senha

def enviar(destinatario: str, corpo: str):
    mensagem = MIMEMultipart()
    mensagem["From"] = __obter_login()
    mensagem["To"] = destinatario
    mensagem["Subject"] = "Pedido Criado"

    mensagem.attach(MIMEText(corpo, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls() #Criptografia de conexao
            servidor.login(__obter_login(), __obter_senha())
            servidor.send_message(mensagem)
            print("Email enviado com sucesso")
    except Exception as e:
        print("Erro ao enviar e-mail: ", e)

def enviar_email_pedido(destinario: str, tamanho: str, sabores: list[str]):
    mensagem = f"""Pedido criado com sucesso!

    Tamanho da pizza: {tamanho}
    Sabores: {",".join(sabores)}
    """
    enviar(destinario, mensagem)

