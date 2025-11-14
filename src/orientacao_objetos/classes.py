from datetime import date
import os
import platform
from typing import List
import altair as alt         
import questionary
from rich.table import Table
from rich.console import Console
from rich.align import Align




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
    ticket1.descricao = "Problema com login."

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

# exercicio_ticket()



def limpar_tela():
    sistema=platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

console = Console()
desenvolvedoras: list[Desenvolvedora] = []

def menu_sistema():
    menu_geral=questionary.select("Escolha o sistema", choices =["Desenvolvedora", "Sair"]).ask().lower()
    limpar_tela()
    if menu_geral == "desenvolvedora":
        exemplo_crud_lista_objetos()

def exemplo_crud_lista_objetos():
    menu=" "
    while menu != "sair":
        menu = questionary.select("Escolha o menu", choices=["Adicionar, Listar", "Sair"]).ask().lower()
        if menu == "adicionar":
            adicionar_desenvolvedora()
        elif menu == "listar":
            listar_desenvolvedoras()

def adicionar_desenvolvedora():
    #Solicitar os dados, instanciando um objeto de desenvolvedora e adicionar na lista
    console.print(Align.center("Cadastro de desenvolvedora"), style="blue")

    desenvolvedora = Desenvolvedora()
    desenvolvedora.nome = questionary.text("Nome da desenvolvedora: ").ask()
    desenvolvedora.proprietario = questionary.text("Proprietário: ").ask()

    desenvolvedora.sede = Endereco()
    desenvolvedora.sede.cidade = questionary.text("Cidade sede: ").ask()
    desenvolvedora.sede.pais = questionary.text("País sede: ").ask()

    desenvolvedoras.append(desenvolvedora)
    console.print("Desenvolvedora adicionada com sucesso!", style="green")
    input("Pressione Enter para continuar...")
    limpar_tela()

def listar_desenvolvedoras():
    #listar desenvolvedoras
    if len(desenvolvedoras) == 0:
        console.print("Nenhuma desenvolvedora cadastrada.", style="red")
        input("Pressione Enter para continuar...")
        limpar_tela()
        return
    
    table = Table("Nome", "Proprietario", "Endereco")

    for i in range(0, len(desenvolvedoras)):
        desenvolvedora = desenvolvedoras[i]
        table.add_row(
            desenvolvedora.nome,
            desenvolvedora.proprietario,
            f"{desenvolvedora.sede.cidade} - {desenvolvedora.sede.pais}"
        )

        console.print(table)

#exemplo_crud_lista_objetos()

# Ex. 1: Criar uma crud de Animal e seu Dono
# Criar uma classe chamada Dono com os seguintes atributos abaixo:
#   - Nome
#   - CPF
# Criar uma classe chamada Animal com os seguintes atributos abaixo:
# - Raça
# - Dono
# - Data de Nascimento
# Fazer o CR(Create/Read) do Animal solicitando os dados de seu dono também
# console = Console()


# class Dono:
#     def __init__(self, nome, cpf):
#         self.nome = nome
#         self.cpf = cpf


# class Animal:
#     def __init__(self, raca, data_nascimento, nome_dono, cpf_dono):
#         self.raca = raca
#         self.data_nascimento = data_nascimento
#         self.dono = Dono(nome_dono, cpf_dono)


# # LISTA DE ANIMAIS (depois das classes)
# animais: List[Animal] = []
# def menu_sistema():
#     menu = questionary.select(
#         "Escolha o sistema",
#         choices=["Animal", "Sair"]
#     ).ask().lower()

#     limpar_tela()

#     if menu == "animal":
#         crud_animais()


# def crud_animais():
#     menu = ""

#     while menu != "sair":
#         menu = questionary.select(
#             "Escolha o menu",
#             choices=["Adicionar", "Listar", "Sair"]
#         ).ask().lower()

#         if menu == "adicionar":
#             adicionar_animal()
#         elif menu == "listar":
#             listar_animais()


# def adicionar_animal():
#     raca = questionary.text("Raça do animal: ").ask()
#     data_nascimento = questionary.text("Data de nascimento: ").ask()
#     nome_dono = questionary.text("Nome do dono: ").ask()
#     cpf_dono = questionary.text("CPF do dono: ").ask()

#     novo_animal = Animal(raca, data_nascimento, nome_dono, cpf_dono)

#     animais.append(novo_animal)

#     console.print("Animal cadastrado com sucesso!", style="green")
#     input("Pressione Enter para continuar...")
#     limpar_tela()


# def listar_animais():
#     if len(animais) == 0:
#         console.print("Nenhum animal cadastrado.", style="red")
#         input("Pressione Enter para continuar...")
#         limpar_tela()
#         return

#     table = Table("Raça", "Nascimento", "Dono", "CPF")

#     for animal in animais:
#         table.add_row(
#             animal.raca,
#             animal.data_nascimento,
#             animal.dono.nome,
#             animal.dono.cpf
#         )

#     console.print(table)
#     input("Pressione Enter para continuar...")
#     limpar_tela()


# if __name__ == "__main__":
#     while True:
#         menu_sistema()


# Ex. 2: Modificar o conteúdo da classe Dono acrescentando os atributos abaixo:
# -  Bairro, Rua, Número
# Alterar o CR(Create/Read) para solicitar os novos dados do dono
# Modificar o conteúdo da classe Animal acrescentando os atributos abaixo:
#   Peso
#   Altura
#   Sexo
#   Cor
#   Origem da Raça

console = Console()

class Dono:
    def __init__(self, nome, cpf, bairro, rua, numero):
        self.nome = nome
        self.cpf = cpf
        self.bairro = bairro
        self.rua = rua
        self.numero = numero


class Animal:
    def __init__(
        self,
        raca,
        data_nascimento,
        peso,
        altura,
        sexo,
        cor,
        origem_raca,
        nome_dono,
        cpf_dono,
        bairro,
        rua,
        numero,
    ):
        self.raca = raca
        self.data_nascimento = data_nascimento
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.cor = cor
        self.origem_raca = origem_raca
        self.dono = Dono(nome_dono, cpf_dono, bairro, rua, numero)


animais: List[Animal] = []


def crud_animais():
    while True:
        menu = questionary.select(
            "Escolha o menu",
            choices=["Adicionar", "Listar", "Sair"]
        ).ask().lower()

        if menu == "adicionar":
            adicionar_animal()
        elif menu == "listar":
            listar_animais()
        elif menu == "sair":
            break


def adicionar_animal():
    console.print("Cadastro de Animal", style="blue")

    raca = questionary.text("Raça do animal: ").ask()
    data_nascimento = questionary.text("Data de nascimento: ").ask()
    peso = questionary.text("Peso (kg): ").ask()
    altura = questionary.text("Altura (cm): ").ask()
    sexo = questionary.select("Sexo:", choices=["Macho", "Fêmea"]).ask()
    cor = questionary.text("Cor: ").ask()
    origem_raca = questionary.text("Origem da raça: ").ask()

    nome_dono = questionary.text("Nome do dono: ").ask()
    cpf_dono = questionary.text("CPF do dono: ").ask()
    bairro = questionary.text("Bairro: ").ask()
    rua = questionary.text("Rua: ").ask()
    numero = questionary.text("Número: ").ask()

    novo_animal = Animal(
        raca, data_nascimento, peso, altura, sexo, cor, origem_raca,
        nome_dono, cpf_dono, bairro, rua, numero
    )

    animais.append(novo_animal)

    console.print("Animal cadastrado com sucesso!", style="green")
    input("Pressione Enter para continuar...")


def listar_animais():
    if len(animais) == 0:
        console.print("Nenhum animal cadastrado.", style="red")
        input("Pressione Enter para continuar...")
        return

    table = Table(
        "Raça", "Nascimento", "Peso", "Altura", "Sexo", "Cor", "Origem",
        "Dono", "CPF", "Bairro", "Rua", "Número"
    )

    for a in animais:
        table.add_row(
            a.raca,
            a.data_nascimento,
            str(a.peso),
            str(a.altura),
            a.sexo,
            a.cor,
            a.origem_raca,
            a.dono.nome,
            a.dono.cpf,
            a.dono.bairro,
            a.dono.rua,
            str(a.dono.numero)
        )

    console.print(table)
    input("Pressione Enter para continuar...")