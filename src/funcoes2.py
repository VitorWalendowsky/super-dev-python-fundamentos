# exemplo calculo de compra no paraguai #


def solicitar_cotacao_dolar() -> float:
    cotacao : float = float(input("Digite o valor da cotacao do dolar hoje: ").replace(",","."))
    return cotacao


def solicitar_nome_produto() -> str:
    nome = input("Digite o nome do produto: ")
    return nome

    
def solicitar_valor_produto_dolar() -> float:
    valor : float = float(input("Digite o valor do produto em dolar: ").replace(",","."))
    return valor
    

def solicitar_se_pagara_imposto() -> bool:
    resposta : str = input("Você pagará imposto? (s/n): ").strip().lower()
    if resposta == "s":
        return True
    else:
        return False
        

def solicitar_deseja_utilizar_cota_dolar_mensal() -> bool:
        resposta : str = input("Deseja utilizar a cota dolar mensal? (s/n): ").strip().lower()
        if resposta == "s":
            return True
        else:
            return False
        

#solicitar_valor_produto_dolar -> float:
#solicitar_se_pagara_imposto -> bool:
#solicitar_deseja_utilizar_cota_dolar_mensal -> bool:

def calcular_valor_compra_paraguai():
    cotacao_dolar: float = solicitar_cotacao_dolar()
    nome_produto: str = solicitar_nome_produto()
    valor_produto_dolar: float = solicitar_valor_produto_dolar()
    pagara_imposto: bool = solicitar_se_pagara_imposto()
#Calcular o valor do produto em reais
    valor_produto_em_reais = valor_produto_dolar * cotacao_dolar

    if pagara_imposto == True:
        utilizar_cota_dolar_mensal= solicitar_deseja_utilizar_cota_dolar_mensal()

#Descobri valor do produto para calculo do imposto
        if utilizar_cota_dolar_mensal == True:
            cotacao_mensal = 500.00
            
#Calcular o valor que sera utilizado para descobrir quanto a mais sera pago de imposto
            valor_imposto_dolar = (valor_produto_dolar - cotacao_mensal) / 2
            valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

            valor_total_produto_reais = valor_produto_em_reais + valor_imposto_reais
            print(f"""Valor total do produto com imposto: R${valor_total_produto_reais}
                  Valor total do produto : R${valor_produto_dolar}
                  valor imposto: R${valor_imposto_reais}
                  valor total do produto com imposto: R${valor_total_produto_reais}""")
        
            

            def calcular_valor_produto_acrescentando_imposto(
                valor_produto_dolar: float,
                cotacao_dolar: float,
                valor_produto_reais: float,):

                valor_imposto_dolar = valor_produto_dolar / 2
                valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

                valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
                print("Valor total do produto com imposto: R$" + str(valor_total_produto_reais))





#Ex.1: Criar uma funcao chamado exercicio_aluno
# solicitar o nome (criar funcao)
#solicitar nota 1
#solicitar nota 2
#solicitar nota 3
#calcular a media e apresentar
#Criar um IF que verifique se o aluno esta ou nao aprovado e apresentar

def exercicio_aluno():
    nome_aluno : str = input("Digite o nome do aluno: ")
    nota1 : float = float(input("Digite a nota 1: ").replace(",","."))
    nota2 : float = float(input("Digite a nota 2: ").replace(",","."))
    nota3 : float = float(input("Digite a nota 3: ").replace(",","."))
    media : float = (nota1 + nota2 + nota3) / 3
    print("Média do aluno " + nome_aluno + ": " + str(media))
    if media >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")