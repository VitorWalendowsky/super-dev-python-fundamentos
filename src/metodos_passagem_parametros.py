from typing import List

class Aluno:
    def __init__(
        self,
        nome: str,
        notas: List[float],
        frequencia: float = 75,
        turma: str = "SuperDev",
    ):
        self.nome = nome
        self.notas = notas
        self.frequencia = frequencia
        self.turma = turma


def exemplo_passagem_parametros_nomeados():
    # Pedro terá a frequência de 75%, pq foi utilizado o valor default do parâmetro de frequência
    # 2 parâmetros seguindo a ordem do construtor e outro parâmetro pelo nome (turma)
    pedro = Aluno(
        "Pedro Silva",
        [8, 7, 6.5],
        turma="SuperDev 7ª",
    )

    print("---- Dados do Pedro ----")
    print("Nome:", pedro.nome)
    print("Notas:", pedro.notas)
    print("Frequência:", pedro.frequencia)
    print("Turma:", pedro.turma)
    print()

    # Passando todos os parâmetros pelo nome, podendo passar em qualquer ordem
    maria = Aluno(
        nome="Maria",
        notas=[10, 9.75, 3],
        turma="Adas",
        frequencia=100,
    )

    print("---- Dados da Maria ----")
    print("Nome:", maria.nome)
    print("Notas:", maria.notas)
    print("Frequência:", maria.frequencia)
    print("Turma:", maria.turma)


exemplo_passagem_parametros_nomeados()

## Exercício de métodos com parâmetros nomeados
# Criar uma classe chamada Player com os seguintes parâmetros no construtor
# nick com valor default "Geraldão"
# classe com valor default "tanque"
# lane com valor default "meio"
# elo com valor default "bronze"
# maestria com valor default "7"
# main com valor default "Jinx"
# N utilizar os mesmos atributos, mudar a cada instancia nova (utilizar outros)
# Instanciar um objeto com 3 atributos noemados
# Instanciar um objeto com 2 atributos noemados
# Instanciar um objeto com 1 atributo noemado
# Instanciar um objeto com 5 atributos noemados
# Instanciar um objeto com 4 atributos noemados
# Instanciar um objeto com 6 atributos noemados
# Instanciar um objeto com 2 atributos noemados
# Apresentar os dados
# 
# Ex 2: Criar uma classe com 4 parâmetros alguns com valores defaults e outros n
# Instanciar objetos e apresentar
# 
# Ex 3: Criar uma classe com 10 parâmetros alguns com valores defaults 
# e outros n
# Instanciar objetos e apresentar


# Exercício 1 – Classe Player


class Player:
    def __init__(
        self,
        nick: str = "Geraldão",
        classe: str = "tanque",
        lane: str = "meio",
        elo: str = "bronze",
        maestria: str = "7",
        main: str = "Jinx",
    ):
        self.nick = nick
        self.classe = classe
        self.lane = lane
        self.elo = elo
        self.maestria = maestria
        self.main = main


def exercicio_player():
    # 1) Instância com 3 atributos
    p1 = Player(nick="ShadowWolf", classe="atirador", elo="prata")

    # 2) Instância com 2 atributos
    p2 = Player(main="Lux", lane="suporte")

    # 3) Instância com 1 atributo
    p3 = Player(nick="Bruxão")

    # 4) Instância com 5 atributos
    p4 = Player(
        nick="ArqueiroMístico",
        classe="atirador",
        lane="rota superior",
        elo="platina",
        maestria="5",
    )

    # 5) Instância com 4 atributos
    p5 = Player(
        nick="TankerPro",
        classe="tanque",
        lane="selva",
        elo="diamante",
    )

    # 6) Instância com 6 atributos
    p6 = Player(
        nick="DemonLord",
        classe="mago",
        lane="meio",
        elo="desafiante",
        maestria="7",
        main="Annie",
    )

    # 7) Instância com 2 atributos nomeados
    p7 = Player(classe="lutador", elo="ouro")

    lista = [p1, p2, p3, p4, p5, p6, p7]

    print("===== DADOS DOS PLAYERS =====")
    for jogador in lista:
        print("-----------------------------")
        print("Nick:", jogador.nick)
        print("Classe:", jogador.classe)
        print("Lane:", jogador.lane)
        print("Elo:", jogador.elo)
        print("Maestria:", jogador.maestria)
        print("Main:", jogador.main)
        print()


# Exercício 2 – Classe com 4 parâmetros


class Livro:
    def __init__(
        self,
        titulo: str,
        autor: str,
        paginas: int = 100,
        genero: str = "Ficção",
    ):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.genero = genero


def exercicio_livro():
    l1 = Livro("Duna", "Frank Herbert")
    l2 = Livro("1984", "George Orwell", paginas=328)
    l3 = Livro("Clean Code", "Robert Martin", genero="Programação", paginas=464)

    print("===== LIVROS =====")
    for l in [l1, l2, l3]:
        print("-----------------------------")
        print("Título:", l.titulo)
        print("Autor:", l.autor)
        print("Páginas:", l.paginas)
        print("Gênero:", l.genero)
        print()


# Exercício 3 – Classe com 10 parâmetros

class Carro:
    def __init__(
        self,
        modelo: str,
        marca: str,
        ano: int,
        cor: str = "preto",
        motor: str = "1.0",
        portas: int = 4,
        cambio: str = "manual",
        combustivel: str = "gasolina",
        preco: float = 50000.0,
        placa: str = "ABC-1234",
    ):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.portas = portas
        self.cambio = cambio
        self.combustivel = combustivel
        self.preco = preco
        self.placa = placa


def exercicio_carro():
    c1 = Carro("Civic", "Honda", 2020, preco=115000, motor="2.0")
    c2 = Carro("Gol", "VW", 2010)
    c3 = Carro("Corolla", "Toyota", 2022, cor="branco", cambio="automático")

    print("===== CARROS =====")
    for c in [c1, c2, c3]:
        print("-----------------------------")
        print("Modelo:", c.modelo)
        print("Marca:", c.marca)
        print("Ano:", c.ano)
        print("Cor:", c.cor)
        print("Motor:", c.motor)
        print("Portas:", c.portas)
        print("Câmbio:", c.cambio)
        print("Combustível:", c.combustivel)
        print("Preço:", c.preco)
        print("Placa:", c.placa)
        print()


exercicio_player()
exercicio_livro()
exercicio_carro()
