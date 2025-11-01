def funcao_sem_retorno():
    print("Olá mundo")

def funcao_com_retorno() -> str:
    produto : str = "iPhone 17 Pro Max"
    return produto

def funcao_executar():
    funcao_sem_retorno()

    nome = funcao_com_retorno()
    print("Nome do produto: " + nome)




def solicitar_nome_jogo() -> str:
    nome : str = input("Digite o nome do jogo: ").strip()
    return nome

def solicitar_preco_jogo() -> float:
    preco : float = float(input("Digite o preço: "))
    return preco

def solicitar_quantidade_jogo() -> int:
    quantidade : int = int(input("Digite a quantidade: "))
    return quantidade

def solicitar_pedido_fechado() -> bool:
    pedido_fechado : str = input("Pedido fechado (s/n): ").strip().lower()
    if pedido_fechado == "s":
        return True
    else:
        return False

def solicitar_valor_pagamento():
    valor_pagamento : float = float(input("Digite o valor pago: "))
    return valor_pagamento

def processar_pedido():
    nome : str = solicitar_nome_jogo()
    preco : float = solicitar_preco_jogo()
    quantidade : int = solicitar_quantidade_jogo()
    pedido_fechado: bool = solicitar_pedido_fechado()

    valor_pedido : float = quantidade * preco
    print("\n\nValor pedido: " + str(valor_pedido))

    if pedido_fechado == True:
        valor_pagamento = solicitar_valor_pagamento()
        if valor_pagamento > valor_pedido:
            valor_troco = valor_pagamento - valor_pedido
            print("Troco: " + str(valor_troco))
            print("Status: Pedido realizado")
        elif valor_pagamento == valor_pedido:
            print("Pedido sem troco")
            print("Status: Pedido realizado")
        else:
            valor_faltante = valor_pedido - valor_pagamento
            print("Valor faltante: " + str(valor_faltante))
            print("Status: Pedido cancelado")

# exemplo calculo de compra no paraguai #

def solicitar_cotacao_dolar() -> float:
    return float(input("Digite o valor da cotação do dólar hoje: ").replace(",", "."))


def solicitar_nome_produto() -> str:
    return input("Digite o nome do produto: ")


def solicitar_valor_produto_dolar() -> float:
    return float(input("Digite o valor do produto em dólar: ").replace(",", "."))


def solicitar_se_pagara_imposto() -> bool:
    resposta = input("Você pagará imposto? (s/n): ").strip().lower()


def solicitar_deseja_utilizar_cota_dolar_mensal() -> bool:
    resposta = input("Deseja utilizar a cota mensal de isenção de US$500? (s/n): ").strip().lower()


def calcular_valor_compra_paraguai():
    # Solicita informações básicas
    cotacao_dolar = solicitar_cotacao_dolar()
    nome_produto = solicitar_nome_produto()
    valor_produto_dolar = solicitar_valor_produto_dolar()
    pagara_imposto = solicitar_se_pagara_imposto()

    # Converte valor em reais
    valor_produto_reais = valor_produto_dolar * cotacao_dolar

    print(f"\nProduto: {nome_produto}")
    print(f"Valor do produto em reais (sem imposto): R$ {valor_produto_reais:.2f}")

    # Caso o usuário precise pagar imposto
    if pagara_imposto:
        utilizar_cota = solicitar_deseja_utilizar_cota_dolar_mensal()

        if utilizar_cota:
            cota_mensal_dolar = 500.00
            # Se o produto ultrapassar a cota, aplica imposto sobre o excedente
            if valor_produto_dolar > cota_mensal_dolar:
                excedente_dolar = valor_produto_dolar - cota_mensal_dolar
                imposto_dolar = excedente_dolar * 0.5  # 50% de imposto
                imposto_reais = imposto_dolar * cotacao_dolar
                total_reais = valor_produto_reais + imposto_reais

                print(f"Valor excedente: US$ {excedente_dolar:.2f}")
                print(f"Imposto devido (50% sobre o excedente): R$ {imposto_reais:.2f}")
                print(f"Valor total com imposto: R$ {total_reais:.2f}")
            else:
                print("O valor está dentro da cota de US$500. Nenhum imposto será cobrado.")
        else:
            # Se não usar cota, paga imposto sobre todo o valor
            imposto_dolar = valor_produto_dolar * 0.5
            imposto_reais = imposto_dolar * cotacao_dolar
            total_reais = valor_produto_reais + imposto_reais

            print(f"Imposto sobre o valor total (50%): R$ {imposto_reais:.2f}")
            print(f"Valor total com imposto: R$ {total_reais:.2f}")

    else:
        print("Nenhum imposto será cobrado.")
        print(f"Valor final do produto: R$ {valor_produto_reais:.2f}")
