from typing import Dict, List
import questionary
import requests
from rich.console import Console
from rich.table import Table
import os
import platform

def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def crud_funcionarios():
    opcao = ""
    while opcao != "Sair":
        opcao = questionary.select("Escolha o menu principal", choices=[
            "Funcionários", "Sair"]).ask()
        
        limpar_tela()
        if opcao == "Funcionários":
            menu_funcionarios()


def menu_funcionarios():
    opcao = ""
    while opcao != "Sair":
        opcao = questionary.select("Escolha o menu de funcionários", 
                                   choices=["Listar", "Cadastrar", "Editar", "Excluir", "Sair"]).ask()
        
        limpar_tela()
        if opcao == "Listar":
            listar_funcionarios()
        elif opcao == "Cadastrar":
            cadastrar_funcionario()
        elif opcao == "Editar":
            editar_funcionario()
        elif opcao == "Excluir":
            excluir_funcionario()


def listar_funcionarios():
    url = "https://api.franciscosensaulas.com/api/v1/trabalho/funcionarios-detalhes"
    response = requests.get(url)

    if response.status_code == 200:
        funcionarios: List[Dict[str, str | float | int]] = response.json()
        tabela = Table(title="Funcionários")

        tabela.add_column("ID")
        tabela.add_column("Nome")
        tabela.add_column("Cargo")
        tabela.add_column("Departamento")
        tabela.add_column("Telefone")
        tabela.add_column("Salário")

        for funcionario in funcionarios:
            tabela.add_row(
                str(funcionario.get("id")),
                funcionario.get("nome", ""),
                funcionario.get("cargo", ""),
                funcionario.get("departamento", ""),
                funcionario.get("telefone", ""),
                f"R$ {funcionario.get('salario', 0):.2f}"
            )

        console = Console()
        console.print(tabela)
    else:
        print("Erro ao listar funcionários:", response.text)


def cadastrar_funcionario():
    url = "https://api.franciscosensaulas.com/api/v1/trabalho/funcionarios-detalhes"

    nome = questionary.text("Digite o nome do funcionário:").ask().strip()
    cargo = questionary.text("Digite o cargo:").ask().strip()
    departamento = questionary.text("Digite o departamento:").ask().strip()
    telefone = questionary.text("Digite o telefone:").ask().strip()
    salario = float(questionary.text("Digite o salário:").ask().replace(",", "."))

    payload = {
        "nome": nome,
        "cargo": cargo,
        "departamento": departamento,
        "telefone": telefone,
        "salario": salario
    }

    headers = {"Content-Type": "application/json-patch+json"}
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print("Funcionário cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar funcionário:", response.text)


def editar_funcionario():
    listar_funcionarios()
    id_funcionario = questionary.text("Digite o ID do funcionário a editar:").ask()

    nome = questionary.text("Digite o nome:").ask().strip()
    cargo = questionary.text("Digite o cargo:").ask().strip()
    departamento = questionary.text("Digite o departamento:").ask().strip()
    telefone = questionary.text("Digite o telefone:").ask().strip()
    salario = float(questionary.text("Digite o salário:").ask().replace(",", "."))

    url = f"https://api.franciscosensaulas.com/api/v1/trabalho/funcionarios-detalhes/{id_funcionario}"

    payload = {
        "nome": nome,
        "cargo": cargo,
        "departamento": departamento,
        "telefone": telefone,
        "salario": salario
    }

    headers = {"Content-Type": "application/json-patch+json"}
    response = requests.put(url, json=payload, headers=headers)

    if response.status_code == 204:
        print("Funcionário alterado com sucesso!")
    else:
        print("Erro ao alterar funcionário:", response.text)


def excluir_funcionario():
    listar_funcionarios()
    id_funcionario = questionary.text("Digite o ID do funcionário a excluir:").ask()

    url = f"https://api.franciscosensaulas.com/api/v1/trabalho/funcionarios-detalhes/{id_funcionario}"
    response = requests.delete(url)

    if response.status_code == 204:
        print("Funcionário excluído com sucesso!")
    elif response.status_code == 404:
        print("Funcionário não encontrado.")
    else:
        print("Erro ao excluir funcionário:", response.text)


if __name__ == "__main__":
    crud_funcionarios()
