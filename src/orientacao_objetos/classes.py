from datetime import date,
from typing import List
from rich.table import Table
from rich.console import Console

class Endereco:
    def __init__(self):
        self.cidade: str = None
        self.pais: str = None


class Desenvolvedora:
    def __init__(self):
        self.nome: str = None
        self.sede: Endereco = None
        self.proprietario: str = None
        self.jogos: List[Jogo] = []
        

# Classe [e uma represntacao de objeto do mundo real
class Jogo:
    def __init__(self):
        #Atributos de classe
        self.titulo: str = None
        self.data_lancamento: date = None
        self.preco: float = None
        self.genero: str = None
        self.classificacao: str = None
        self.desenvolvedora: Desenvolvedora = None


def exemplo_01():

    #Titulo = "GTA VI"
#data_lancamento = date(2027, 2, 28)
#preco = 650.00
#genero = "Ação"
#classificacao = "M"

    endereco_rockstar = Endereco()
    endereco_rockstar.cidade = "New York"
    endereco_rockstar.pais = "US"

    rockstar_games= Desenvolvedora()
    rockstar_games.nome = "Rockstar Games"
    rockstar_games.proprietario = "Take-Two Interactive"
    rockstar_games.sede = endereco_rockstar

    gta_vi_dict = {
            "titulo": "GTA VI",
            "data_lancamento": "2027-02-28",
            "preco": 650.00,
            "genero": "Ação",
            "classificacao": "M"
        }

    # Instanciando um objeto chamado gta_vi da classe Jogo
    gta_vi = Jogo() # nome_objetio = NomeClasse()
    # Definindo valor para as propriedades do objeto
    gta_vi.titulo = "GTA VI"
    gta_vi.data_lancamento = date(2027, 2, 28)
    gta_vi.preco = 650.00
    gta_vi.genero = "Ação"
    gta_vi.classificacao = "M"
    gta_vi.desenvolvedora = rockstar_games

    gta_vi.preco = 669.99

    the_witcher = Jogo()
    the_witcher.titulo = "The Witcher 4"
    the_witcher.data_lancamento = date(2027, 12, 31)
    the_witcher.preco = 500
    the_witcher.genero = "RPG"
    the_witcher.classificacao = "M"

    league_of_legends = Jogo()
    league_of_legends.titulo = "League of Legends"
    league_of_legends.data_lancamento = date(2009, 10, 27)
    league_of_legends.preco = 0.00
    league_of_legends.genero = "MOBA"
    league_of_legends.classificacao = "12"

    #adicionar jogos a desenvolveradora
    rockstar_games.jogos.append(gta_vi)
    rockstar_games.jogos.append(the_witcher)
    rockstar_games.jogos.append(league_of_legends)


    colunas = ["Desenvolvedora", "Título", "Data de Lançamento", "Preço", "Gênero", "Classificação"]
    # Instanciado um objeto chamado tabela na classe Table
    tabela = Table(*colunas)

    tabela.add_row(
        gta_vi.desenvolvedora.nome, gta_vi.titulo, str(gta_vi.data_lancamento), str(gta_vi.preco), gta_vi.genero, gta_vi.classificacao
    )
    tabela.add_row(
        "N/A", the_witcher.titulo, str(the_witcher.data_lancamento), str(the_witcher.preco), the_witcher.genero, the_witcher.classificacao
    )
    tabela.add_row(
        "N/A", league_of_legends.titulo, str(league_of_legends.data_lancamento), str(league_of_legends.preco), league_of_legends.genero, league_of_legends.classificacao
    )


    # Instanciando um objeto chamado console da classe Console
    console = Console()
    console.print(tabela)


#Criar uma classe chamado Marca com os seguintes atributos:
#Nome
#Id (1,2,3,4,5...)
# Fundador - string
# data de fundacao
# Faturamento - float
#criar uma funcao "exercicio_marca"
# instaciar 2 objetos da classe Marca, atribuindo valor para todos os atributos
# Exemplo:batatinha = produto()
# batatinha.valor - 1.30
#Apresetar os dados das duas marcas (print ou table)

class Marca:
    def __init__(self):
        self.nome: str = None
        self.id: int = None
        self.fundador: str = None
        self.data_fundacao: date = None
        self.faturamento: float = None


def exercicio_marca():
    Shogun = Marca()
    Shogun.nome = "Shogun"
    Shogun.id = 1
    Shogun.fundador = "Vitor Hugo"
    Shogun.data_fundacao = date(2020, 5, 15)
    Shogun.faturamento = 1500000.00

    atlantis = Marca()
    atlantis.nome = "Atlantis"
    atlantis.id = 2
    atlantis.fundador = "Marias Clara"
    atlantis.data_fundacao = date(2018, 8, 20)
    atlantis.faturamento = 1200000.00

    for marca in [Shogun, atlantis]:
        print(f"""
              nome: {marca.nome}
              id: {marca.id}
              fundador: {marca.fundador}
              data_fundacao: {marca.data_fundacao}
              faturamento: {marca.faturamento}
              """)
        

    # # Criar tabela
    # tabela = Table(title="📊 Tabela de Marcas")

    # # Adicionar colunas
    # tabela.add_column("ID", justify="center", style="cyan", no_wrap=True)
    # tabela.add_column("Nome", style="magenta")
    # tabela.add_column("Fundador", style="yellow")
    # tabela.add_column("Data de Fundação", justify="center", style="green")
    # tabela.add_column("Faturamento (R$)", justify="right", style="bold blue")

    # # Adicionar linhas (dados)
    # for marca in [shogun, atlantis]:
    #     tabela.add_row(
    #         str(marca.id),
    #         marca.nome,
    #         marca.fundador,
    #         str(marca.data_fundacao),
    #         f"{marca.faturamento:,.2f}"
    #     )

    # # Exibir tabela
    # console = Console()
    # console.print(tabela)
        
#exercicio_marca()




# Exercicio_02 Criar uma classe chamado usuario com os seguintes atributos:
# ID (1,2,3,4,5....)
#Nome completo
#Login
#Data de nascimento
#Criar uma classe chamado ticket com os seguintes atributos
# Numero (1000, 1001, 1002...)
#usuario do tipo Usuario
#data de abertura
#status (Em analise, Finalizado, Pendente)
#data de fechamento
#descricao
#criar uma funcao chamada exercicio_ticket
# instanciar dois usuarios e preencher os atributos
#criar um ticket para o primeiro usuario com stauts "Em analise" preenchendo todas as propriedades com excecao da tata de fecament, a data de abertura deve ser hoje (12/11/2025
# Criar um ticket para o primeiro usuario com status "Finalizado" preenchendo todas as propriedades. A data de abertura deve ser 10 dias atras e a data de fechamento a data de hoje
#apresentar dados do ticket e seus usuarios

class Usuario:
    def __init__(self):
        self.id: int = None
        self.nome_completo: str = None
        self.login: str = None
        self.data_nascimento: date = None


class Ticket:
    def __init__(self):
        self.numero: int = None
        self.usuario: Usuario = None
        self.data_abertura: date = None
        self.status: str = None
        self.data_fechamento: date = None
        self.descricao: str = None



def exercicio_ticket():    
    usuario1 = Usuario()
    usuario1.id = 1
    usuario1.nome_completo = "Vitor Hugo"
    usuario1.login = "vitorhugo"
    usuario1.data_nascimento = date(1995, 4, 20)

    usuario2 = Usuario()
    usuario2.id = 2
    usuario2.nome_completo = "Maria Clara"
    usuario2.login = "mariaclara"
    usuario2.data_nascimento = date(1998, 7, 15)

    ticket1 = Ticket()
    ticket1.numero = 1000
    ticket1.usuario = usuario1
    ticket1.data_abertura = date(2025, 11, 12)
    ticket1.status = "Em análise"
    ticket1.descricao = "Problema com o sistema de login."

    ticket2 = Ticket()
    ticket2.numero = 1001
    ticket2.usuario = usuario1
    ticket2.data_abertura = date(2025, 11, 2)
    ticket2.status = "Finalizado"
    ticket2.data_fechamento = date(2025, 11, 12)
    ticket2.descricao = "Erro na geração de relatórios."

    tabela = Table(title= "Status tickets")

    tabela.add_column("Numero")
    tabela.add_column("Usuario")
    tabela.add_column("Login")
    tabela.add_column("Data Abertura")
    tabela.add_column("Status")
    tabela.add_column("Data Fechamento")
    tabela.add_column("Descricao")
    
    for ticket in [ticket1, ticket2]:
        tabela.add_row(
            str(ticket.numero),
            ticket.usuario.nome_completo,
            ticket.usuario.login,
            str(ticket.data_abertura),
            ticket.status,
            str(ticket.data_fechamento) if ticket.data_fechamento else "N/A",
            ticket.descricao
        )

        console= Console()
        console.print(tabela)

#executar_ticket()