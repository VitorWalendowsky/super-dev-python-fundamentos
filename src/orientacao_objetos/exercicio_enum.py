from enum import Enum

from src.orientacao_objetos.classes import exemplo_01

# region console 
class MarcaEnum(Enum):
    SONY = "Sony"
    MICROSOFT = "Microsoft"

class Console:
    def __init__(self):
        self.marca: MarcaEnum
        self.modelo: str


def exemplo_console():
    #instanciar objeto
    play_station = Console()
    play_station.marca = MarcaEnum.SONY
    play_station.modelo = "PS1"

    play_station2 = Console()
    play_station2.marca = MarcaEnum.SONY
    play_station2.modelo = "PS2"

    xbox = Console()
    xbox.marca = MarcaEnum.MICROSOFT
    xbox.modelo = "Xbox"
# endregion

class PessoaTipo(Enum):
    Fisica = "PF"
    Juridica = "PJ"

class Pessoa:
    def __init__(self):
        self.nome: str
        self.tipo: PessoaTipo
        self.cpf_cnpj: str
    

def exemplo_pessoas():
    pessoa1 = Pessoa()
    pessoa1.nome = "Vitor"
    pessoa1.tipo = PessoaTipo.Fisica
    pessoa1.cpf_cnpj = "123.456.789-00"

    pessoa2 = Pessoa()
    pessoa2.nome = "Empresa X"
    pessoa2.tipo = PessoaTipo.Juridica
    pessoa2.cpf_cnpj = "12.345.678/0001-00"

    print(
        "PESSOA:",
        pessoa1.nome,
        "TIPO?",
        pessoa1.tipo.value,
        "CPF/CNPJ:",
        pessoa1.cpf_cnpj
    )



#Criar um enum de persongaemEnum com os seguintes valores
#Batman
#Superman
#Buzz Lightyear
#Homem Formiga
#Bob Esponja
#Catdog

#Criar um enum de statusEnum com os seguintes valores
#Pendente
#Em andamento
#Cancelado
#finalizado

#Criar uma classe chamado Job com os seguintes atributos
# - personagem enum
# - valor 2301.20
# - local atuacao "blumenau"
# - status enum

# Intanciar dois objetos de jobs com personagens e status diferentes
# Apresentar os dados

from enum import Enum

class PersonagemEnum(Enum):
    BATMAN = "Batman"
    SUPERMAN = "Superman"
    BUZZ_LIGHTYEAR = "Buzz Lightyear"
    HOMEM_FORMIGA = "Homem Formiga"
    BOB_ESPONJA = "Bob Esponja"
    CATDOG = "Catdog"

class StatusEnum(Enum):
    PENDENTE = "Pendente"
    EM_ANDAMENTO = "Em andamento"
    CANCELADO = "Cancelado"
    FINALIZADO = "Finalizado"

class Job:
    def __init__(self):
        self.personagem: PersonagemEnum | None = None
        self.valor: float | None = None
        self.local_atuacao: str | None = None
        self.status: StatusEnum | None = None

    def apresentar_dados(self):
        print(
            "JOB:", self.personagem.value,
            "VALOR:", self.valor,
            "LOCAL:", self.local_atuacao,
            "STATUS:", self.status.value
        )

def exemplo_job():
    job1 = Job()
    job1.personagem = PersonagemEnum.BATMAN
    job1.valor = 3500.00
    job1.local_atuacao = "Arkham"
    job1.status = StatusEnum.EM_ANDAMENTO

    job2 = Job()
    job2.personagem = PersonagemEnum.BUZZ_LIGHTYEAR
    job2.valor = 2900.75
    job2.local_atuacao = "Comando Estelar"
    job2.status = StatusEnum.PENDENTE

    job1.apresentar_dados()
    job2.apresentar_dados()

exemplo_job()
