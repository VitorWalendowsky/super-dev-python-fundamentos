def exemplo_strings():
    #variaveis o tipo string
    nome_inquilino = "João"
    sobrenome_inquilino = "da Silva"

    #Concatenacão (junta)
    nome_completo = str = nome_inquilino + " " + sobrenome_inquilino
    print(nome_completo)

def exemplo_int_float():
    salario : int = 1500
    aumento: float = 1.30
    novo_salario = salario * aumento
    #str(novo_salario) => converter float para string
    print("Novo salário: " + str(novo_salario)) 


def exemplo_boolean():
    #Boolean True(verdadeiro) False(falso)
    empregado : bool = True

    # Alterando o valor da variavel empregado
    empregado = False

    print("Empregado: " + str(empregado))





    #criar outra funcao para armazenar os dados do paciente
    # nome do paciente
    # cidade natal
    # tipo sanguineo
    # apresentar tudo
    # idade -> inteiro
    # peso -> real
    # altura -> real
    # calcular IMC (índice de massa corporal)
    # calcular o ano de nascimento (ano atual - idade)
    # Nomenclatura de uma funcao/metodo sempre deve ser uma ação (verbo)
    # exemplo: apresentar_dados_paciente()

def apresentar_dados_paciente():
    nome_do_paciente = "Maria de Souza"
    cidade_natal = "Santa Catarina"
    tipo_sanguineo = "O+"
    idade : int = 32
    peso : float = 89.9
    altura : float = 1.80
    imc : float = peso / (altura * altura)
    ano_atual : int = 2025
    ano_nascimento : int = ano_atual - idade

    print("Nome:", nome_do_paciente)
    print("Cidade natal:", cidade_natal)
    print("Tipo sanguíneo:", tipo_sanguineo)
    print("Idade:", idade)
    print("Peso:", peso)
    print("Altura:", altura)
    print("IMC:", imc)
    print("Ano de nascimento:", ano_nascimento)



   # Ctrl + J > py main.py no linux python3 main.py

