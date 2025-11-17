from rich.console import Console
from rich.table import Table

class Cachorro:
    # Construtor com 4 parametros (sendo 3 sem valor default e 1 com valor default)
    def __init__(self, raca_param: str, peso: float, idade: int, cor: str = "caramelo"):
        # Atributos são preenchidos com os dados dos parâmetros
        # O parametro cor tem um valor default (padrão) que é caramelo
        self.raca = raca_param
        self.peso = peso
        self.idade = idade
        self.cor = cor
        
        # Atributo com valor pré-definido
        self.cidade_natal = "Blumenau"


def exemplo_construtor_cachorro():
    # Cachorro(raca, peso, idade, cor)
    toby = Cachorro("Dobermann", 45.20, 15, "Preto")
    print("raça:", toby.raca)
    print("peso:", toby.peso)
    print("idade:", toby.idade)
    print("cidade natal:", toby.cidade_natal)
    print("cor:", toby.cor)

    print("\n--- Segundo cachorro ---")
    daschund = Cachorro("Salsicha", 70.00, 5)  # aqui cor fica "caramelo" (valor padrão)
    print("raça:", daschund.raca)
    print("peso:", daschund.peso)
    print("idade:", daschund.idade)
    print("cidade natal:", daschund.cidade_natal)
    print("cor:", daschund.cor)


exemplo_construtor_cachorro()


# Exercício de Construtores
# Criar uma classe chamada Passagem com um construtor que contenha os parâmetros abaixo:
# - destino
# - quantidade dias
# - data inicio
# Instanciar dois objetos para desinos diferentes, preenchendo os parâmetros
# Apresentar os dados em uma tabela
# Adicionar os parâmetros abaixo no construtor da classe Passagem
# - quantidade pessoas com valor default 2
# - partida çom valor default 'São Paulo'
# Instanciar outro objeto passando: destino, qtd dias, data inicio, quantidade pessoas
# Apresentar na tabela tbm o novo objeto
# Instanciar outro objeto passando: destino, qtd dias, data inicio, quantidade pessoas, partida
# Apresentar na tabela tbm o novo objeto

class Passagem:
    def __init__(self, destino: str, qtd_dias: int, data_inicio: str,
        qtd_pessoas: int = 2, partida: str = "São Paulo"):
        self.destino = destino
        self.qtd_dias = qtd_dias
        self.data_inicio = data_inicio
        self.qtd_pessoas = qtd_pessoas
        self.partida = partida


def tabela_passagens(lista_passagens):
    console = Console()
    tabela = Table(title="Tabela de Passagens")

    tabela.add_column("Destino", style="cyan", no_wrap=True)
    tabela.add_column("Qtd Dias", style="yellow")
    tabela.add_column("Data Início", style="green")
    tabela.add_column("Qtd Pessoas", style="magenta")
    tabela.add_column("Partida", style="blue")

    for p in lista_passagens:
        tabela.add_row(
            p.destino,
            str(p.qtd_dias),
            p.data_inicio,
            str(p.qtd_pessoas),
            p.partida
        )

    console.print(tabela)


# Dois objetos iniciais (somente destino, dias e data)
p1 = Passagem("Rio de Janeiro", 5, "10/01/2025")
p2 = Passagem("Salvador", 7, "20/02/2025")

# Objeto com quantidade pessoas informada
p3 = Passagem("Florianópolis", 4, "05/03/2025", 3)

# Objeto com todos os parâmetros, inclusive partida
p4 = Passagem("Curitiba", 6, "15/04/2025", 4, "Campinas")

# Lista final
lista = [p1, p2, p3, p4]

tabela_passagens(lista)
