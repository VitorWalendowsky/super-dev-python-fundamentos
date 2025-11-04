from questionary import text, password, select, checkbox, confirm

from src.envios.envio_email import enviar_email_pedido


sabores_pizza = [
    "Calabresa",
    "Mussarela",
    "Frango com Catupiry",
    "Portuguesa",
    "Quatro Queijos",
    "Marguerita",
    "Pepperoni",
    "Bacon",
    "Napolitana",
    "Vegetariana"
]

def __solicitar_text() -> str:
    cliente = text("Digite o nome do cliente").ask()
    return cliente

def __solicitar_senha() -> str:
    senha = password("Digite a senha do cliente").ask()
    return senha


# Questionar o tamanho Pequena, Media, Grande


def __escolher_opcao() -> str:
    opcoes = ["Pequena", "Media", "Grande"]
    opcao_escolhida = select("Escolha o tamanho da pizza", choices=opcoes).ask()
    return opcao_escolhida


#tamano permite escolher a quantidade de sabores diferentes
# pequena 1 sabor
# media 1,2 sabores
# Grande 1,2,3,4 sabores


def __escolher_sabores(tamanho: str) -> list:
    quantidade_maxima_sabores = 1
    if tamanho == "Media":
        quantidade_maxima_sabores = 2
    elif tamanho == "Grande":
        quantidade_maxima_sabores = 4

    sabores = checkbox(
        "Escolha o(s) sabor(es) desejado(s)",
        choices=sabores_pizza,
        validate=lambda elementos: __validar_quantidade_sabores(elementos, quantidade_maxima_sabores)
    ).ask()

    return sabores

def __validar_quantidade_sabores(elementos: list[str], quantidade_maxima: int) -> bool | str:
    if len(elementos) == 0:
        return "No minimo deve conter 1 sabor"
    if len(elementos) > quantidade_maxima:
        return f"A pizza deve contar no maximo {quantidade_maxima} sabor(es)"
    return True


#Perguntar se ele quer efetivar a compra
#Gerar um arquivo Jon com ados do pedido

def __solicitar_confirmacao() -> bool:
    confirmado = confirm("Voce confirma o pedido?").ask()
    return confirmado


def exemplos():
    cliente = __solicitar_text()
    senha = __solicitar_senha()
        
    if cliente.endswith("@gmail.com") and senha == "Batatinha":
        #print("Passou")
        tamanho = __escolher_opcao()
        sabores = __escolher_sabores(tamanho)
        pedido_confirmado = __solicitar_confirmacao()

        if pedido_confirmado == True:
            enviar_email_pedido(cliente, tamanho, sabores)
            print("Pedido confirmado")
        else:
            print("Pedido cancelado")
