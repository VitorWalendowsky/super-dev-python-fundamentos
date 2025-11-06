


def solicita_filme():
    filme: str = input("Insira o nome do filme: ").strip()
    return filme


def solicitar_tipo_ingresso():
    tipo_ingresso: str = input("Informe o tipo de ingresso (inteira/meia): ").strip().lower()
    return tipo_ingresso


def solicitar_quantidade_ingressos():
    quantidade: int = int(input("Informe a quantidade de ingressos: "))
    return quantidade


def solicitar_preco_ingresso():
    preco: float = float(input("Informe o preço do ingresso (R$): ").replace(",", "."))
    return preco


def solicitar_formato_sessao():
    formato: str = input("Informe o formato da sessao (2D / 3D / IMAX): ").strip().upper()
    return formato


def solicitar_dia_semana():
    dia: str = input("Informe o dia da semana (seg, ter, qua, qui, sex, sáb, dom): ").strip().lower()
    return dia    


def solicitar_publico():
    print("\nTipo de Público")
    print("1 - Estudante")
    print("2 - Idoso")
    print("3 - Professor")
    print("4 - Promo Quarta do Cinema")
    print("5 - Nenhum")

    raw = input("Escolha o público (1 a 5): ").strip().lower()

    if raw in ("1", "estudante", "est"):
        return "Estudante", 5.00
    if raw in ("2", "idoso", "idos"):
        return "Idoso", 7.00
    if raw in ("3", "professor", "prof"):
        return "Professor", 4.00
    if raw in ("4", "quarta", "quarta do cinema", "quarta do cinema", "quarta-feira"):
        return "Quarta do Cinema", 10.00
    if raw in ("5", "nenhum", "nenhuma", ""):
        return "Nenhum", 0.00


def exercicio_cinema():
   
    filme = solicita_filme()
    tipo = solicitar_tipo_ingresso()
    quantidade = solicitar_quantidade_ingressos()
    preco = solicitar_preco_ingresso()
    formato = solicitar_formato_sessao()
    dia_semana = solicitar_dia_semana()
    publico, desconto_unitario = solicitar_publico()

    valor_bruto = quantidade * preco
    desconto_total = desconto_unitario * quantidade
    total_parcial = valor_bruto - desconto_total

    print("\nDados do Ingresso:")
    print(f"Filme: {filme}")
    print(f"Formato: {formato}")
    print(f"Dia da semana: {dia_semana}")
    print(f"Tipo de ingresso: {tipo.capitalize()}")
    print(f"Público: {publico}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço base: R$ {preco:.2f}")
    print(f"Total bruto: R$ {valor_bruto:.2f}")
    print(f"Desconto fixo total: R$ {desconto_total:.2f}")
    print(f"Total parcial após desconto: R$ {total_parcial:.2f}")



