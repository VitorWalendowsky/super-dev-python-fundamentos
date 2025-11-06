from datetime import datetime, date
import questionary
import os

def solicitar_nome_produto():
    nome: str = input("Digite o nome do produto: ").strip()
    return nome


def solicitar_quantidade():
    quantidade: int = int(input("Digite a quantidade do produto: "))
    return quantidade


def solicitar_preco_unitario():
    preco: float = float(input("Digite o preço da unidade: ").replace(",", "."))
    return preco


def solicitar_categoria():
    categoria: str = input("Informe a categoria do produto: ").strip().lower()
    return categoria


def solicitar_data_vencimento():
    data_str = input("Digite a data de vencimento (formato DD/MM/AAAA): ").strip()
    try:
        return datetime.strptime(data_str, "%d/%m/%Y").date()
    except ValueError:
        print("Data inválida! Tente novamente no formato DD/MM/AAAA.")
        return solicitar_data_vencimento()
    
def solicitar_regiao():
    return input("Informe a região de entrega (Sul, Sudeste, Centro-Oeste, Norte, Nordeste): ").strip().lower()


def solicitar_cupom():
    return input("Digite o cupom de desconto (ou pressione Enter para pular): ").strip().upper()


def calcular_desconto_por_categoria(categoria: str) -> float:
    """Retorna um valor fixo de desconto em reais (simulado)."""
    categoria = categoria.lower()
    if categoria == "esportes":
        return 10.00
    elif categoria == "roupas esportivas":
        return 15.00
    elif categoria == "calçados":
        return 20.00
    elif categoria == "acessórios" or categoria == "acessorios":
        return 12.00
    elif categoria == "equipamentos":
        return 8.00
    elif categoria == "suplementos e nutrição" or categoria == "suplementos e nutricao":
        return 5.00
    elif categoria == "marcas":
        return 7.00
    elif categoria == "ofertas e categorias especiais":
        return 25.00
    else:
        return 0.00


def calcular_percentual_por_categoria(categoria: str) -> float:
    """Retorna o percentual de desconto (%)"""
    categoria = categoria.lower()
    if categoria == "esportes":
        return 10
    elif categoria == "roupas esportivas":
        return 15
    elif categoria == "calçados":
        return 20
    elif categoria == "acessórios" or categoria == "acessorios":
        return 12
    elif categoria == "equipamentos":
        return 8
    elif categoria == "suplementos e nutrição" or categoria == "suplementos e nutricao":
        return 5
    elif categoria == "marcas":
        return 7
    elif categoria == "ofertas e categorias especiais":
        return 25
    else:
        return 0
    

def calcular_frete(regiao: str) -> float:
    regiao = regiao.lower()
    if regiao == "sul":
        return 25.00
    elif regiao == "sudeste":
        return 35.00
    elif regiao == "centro-oeste":
        return 45.00
    elif regiao == "norte":
        return 55.00
    elif regiao == "nordeste":
        return 50.00
    else:
        print("Região inválida. Considerando frete de R$ 50,00.")
        return 50.00
    

def calcular_cupom(cupom: str, total: float, frete: float):
    cupom = cupom.upper()
    desconto_cupom = 0
    frete_gratis = False

    if cupom == "":
        return desconto_cupom, frete_gratis
    
    if cupom == "SUPER10":
        desconto_cupom = 10
    elif cupom == "PRIME20":
        desconto_cupom == 20
    elif cupom == "CLIENTEVIP":
        desconto_cupom == 25
    elif cupom == "FRETEGRATIS":
        desconto_cupom == True
    else:
        print ("Cupom Invalido")
    return desconto_cupom, frete_gratis


def cadastrar_produto():
    nome: str = solicitar_nome_produto()
    quantidade: int = solicitar_quantidade()
    preco: float = solicitar_preco_unitario()
    categoria: str = solicitar_categoria()
    data_vencimento = solicitar_data_vencimento()

    hoje = datetime.today().date()

    if data_vencimento < hoje:
        print("\n Produto Vencido! Compra bloqueada")

    valor_total: float = quantidade * preco
    desconto_fixo: float = calcular_desconto_por_categoria(categoria)
    percentual_desconto: float = calcular_percentual_por_categoria(categoria)
    valor_desconto_percentual: float = valor_total * (percentual_desconto / 100)

    desconto_extra = 0.00
    if data_vencimento.month == hoje.month and data_vencimento.year == hoje.year:
        desconto_extra += 20.00
    if data_vencimento == hoje:
        desconto_extra += valor_desconto_percentual * 0.70  # 70% sobre o desconto da categoria

    valor_com_descontos = valor_total - valor_desconto_percentual - desconto_fixo - desconto_extra

    # Região e frete
    regiao = solicitar_regiao()
    frete = calcular_frete(regiao)

    # Cupom de desconto
    cupom = solicitar_cupom()
    desconto_cupom, frete_gratis = calcular_cupom(cupom, valor_com_descontos, frete)

    valor_cupom = valor_com_descontos * (desconto_cupom / 100)
    valor_final = valor_com_descontos - valor_cupom

    # Frete grátis se total > 500 ou cupom FRETEGRATIS
    if valor_final > 500 or frete_gratis:
        frete = 0.00

    valor_final_com_frete = valor_final + frete

    # -------------------------------
    # 🧮 Apresentação dos resultados
    # -------------------------------
    print("\n🧾 RESUMO DO PEDIDO")
    print("------------------------------------")
    print(f"Produto: {nome}")
    print(f"Categoria: {categoria.capitalize()}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço Unitário: R$ {preco:.2f}")
    print(f"Total Bruto: R$ {valor_total:.2f}")
    print(f"Desconto Categoria ({percentual_desconto}%): R$ {valor_desconto_percentual:.2f}")
    print(f"Desconto Cupom: R$ {valor_cupom:.2f}")
    print(f"Desconto Extra: R$ {desconto_extra:.2f}")
    print(f"Frete: R$ {frete:.2f}")
    print("------------------------------------")
    print(f"Total a Pagar: R$ {valor_final_com_frete:.2f}")
    print(f"Vencimento: {data_vencimento.strftime('%d/%m/%Y')}")
    print(f"Região: {regiao.capitalize()}")
    print("------------------------------------")
    print("Obrigado por comprar conosco!\n")


 # ------------------------------------
 # Perguntar se deseja salvar o resumo
 # ------------------------------------
 

    salvar = questionary.confirm("Deseja salvar o resumo do pedido em um arquivo de texto?").ask()

    if salvar:
        caminho_area_trabalho = os.path.join(os.path.expanduser("~"), "Área de trabalho")
        caminho_arquivo = os.path.join(caminho_area_trabalho, "resumo_pedido.txt")

        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(
                f"🧾 RESUMO DO PEDIDO\n"
                f"------------------------------------\n"
                f"Produto: {nome}\n"
                f"Categoria: {categoria.capitalize()}\n"
                f"Quantidade: {quantidade}\n"
                f"Preço Unitário: R$ {preco:.2f}\n"
                f"Total Bruto: R$ {valor_total:.2f}\n"
                f"Desconto Categoria ({percentual_desconto}%): R$ {valor_desconto_percentual:.2f}\n"
                f"Desconto Cupom: R$ {valor_cupom:.2f}\n"
                f"Desconto Extra: R$ {desconto_extra:.2f}\n"
                f"Frete: R$ {frete:.2f}\n"
                f"------------------------------------\n"
                f"💰 Total a Pagar: R$ {valor_final_com_frete:.2f}\n"
                f"📅 Vencimento: {data_vencimento.strftime('%d/%m/%Y')}\n"
                f"📦 Região: {regiao.capitalize()}\n"
                f"------------------------------------\n"
                f"Obrigado por comprar conosco! 😄\n"
            )

        print("\n✅ Arquivo 'resumo_pedido.txt' foi salvo com sucesso na sua Área de Trabalho!\n")
    else:
        print("\nResumo não foi salvo. Obrigado por usar o sistema! 😄\n")

