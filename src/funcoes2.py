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
#solicitar nota 1(criar funcao)
#solicitar nota 2(criar funcao)
#solicitar nota 3(criar funcao)
#calcular a media e apresentar
#Criar um IF que verifique se o aluno esta ou nao aprovado e apresentar
#solicitar a idade(criar funcao)
#solicitar o peso(criar funcao)
#solicitar a altura(criar funcao)
#calcular o IMC e apresentar a classificação do IMC
#apresentar a geracao de acordo com a idade
#solicitar o cargo (criar funcao)
#Apresentar salario de acordo com o cargo
#estagiario R$ 850.00
#junior R$ 1800.00
#pleno R$ 4000.00
#Senior R$ 6000.00

def solicitar_nome() -> str:
    return input("Digite o nome do aluno: ")


def solicitar_nota(num: int) -> float:
    return float(input(f"Digite a nota {num}: ").replace(",", "."))


def solicitar_idade() -> int:
    return int(input("Digite a idade do aluno: "))


def solicitar_peso() -> float:
    return float(input("Digite o peso (kg): ").replace(",", "."))


def solicitar_altura() -> float:
    return float(input("Digite a altura (m): ").replace(",", "."))


def solicitar_cargo() -> str:
    return input("Digite o cargo (estagiario / junior / pleno / senior): ").strip().lower()


def calcular_media(n1: float, n2: float, n3: float) -> float:
    return (n1 + n2 + n3) / 3


def calcular_imc(peso: float, altura: float) -> float:
    return peso / (altura ** 2)


def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III (mórbida)"


def determinar_geracao(idade: int) -> str:
    if idade <= 12:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 30:
        return "Jovem adulto"
    elif idade <= 59:
        return "Adulto"
    else:
        return "Idoso"


def salario_por_cargo(cargo: str) -> float:
    cargos = {
        "estagiario": 850.00,
        "junior": 1800.00,
        "pleno": 4000.00,
        "senior": 6000.00
    }
    return cargos.get(cargo, 0.00)


def exercicio_aluno():
    # Coleta de dados
    nome = solicitar_nome()
    nota1 = solicitar_nota(1)
    nota2 = solicitar_nota(2)
    nota3 = solicitar_nota(3)
    idade = solicitar_idade()
    peso = solicitar_peso()
    altura = solicitar_altura()
    cargo = solicitar_cargo()

    # Processamentos
    media = calcular_media(nota1, nota2, nota3)
    imc = calcular_imc(peso, altura)
    classificacao_imc = classificar_imc(imc)
    geracao = determinar_geracao(idade)
    salario = salario_por_cargo(cargo)

    # Resultados
    print("\n--- RESULTADO FINAL ---")
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print("Situação: " + ("Aprovado ✅" if media >= 7 else "Reprovado ❌"))
    print(f"Idade: {idade} anos ({geracao})")
    print(f"IMC: {imc:.2f} - {classificacao_imc}")
    if salario > 0:
        print(f"Cargo: {cargo.capitalize()} - Salário: R$ {salario:,.2f}")
    else:
        print(f"Cargo '{cargo}' não reconhecido.")

