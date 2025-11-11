from typing import Dict, List
from src.arquivos import ler_json, escrever_json
from rich.console import Console
from rich.table import Table

def resolver():
    #Pegar os dados de algum lugar:
    #Arquivo -> Leitura do arquivo
    #Pegar todos que estao ativos
    #Pegar status
    #Pegar nome
    #Pegar e-mail
    #Pegar tipo
    #Pegar plano
    #pegar pontuacao
    #Adicionar o dado consolidado na lista
    #Salvr o arquivo

    # Ler o arquivo e convertendo para uma lista de dicionarios
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    ativos, suspensos, inativos = [], [], []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]
        conta = usuario.get("conta", {})
        status = conta.get("status")
        tipo = conta.get("tipo")
        pontuacao = conta.get("pontuacao")

        assinatura = usuario.get("assinatura", {})
        plano = assinatura.get("plano", "Sem assinatura")

        dados_pessoais = usuario.get("dados_pessoais", {})
        nome = dados_pessoais.get("nome")
        email = dados_pessoais.get("email")

        dados = {
            "nome": nome,
            "email": email,
            "tipo": tipo,
            "plano": plano,
            "pontuacao": pontuacao
        }

        if status == "ativo":
            #print(nome, "Ativo")
            ativos.append(dados)
        elif status == "suspenso":
            #print(nome, "Suspenso")
            suspensos.append(dados)
        else:
            #print(nome, "Inativo")
            inativos.append(dados)

    escrever_json(ativos, "data/ativos.json")
    escrever_json(suspensos, "data/suspensos.json")
    escrever_json(inativos, "data/inativos.json")

    apresentar_tabela(ativos, "Contas Ativas")
    apresentar_tabela(suspensos, "Contas Suspensas")
    apresentar_tabela(inativos, "Contas Inativas")


def apresentar_tabela(dados: List[Dict[str, str]], titulo: str):
    table = Table(title=titulo)
    table.add_column("Nome", header_style="bold magenta")
    table.add_column("E-mail", style="blue")
    table.add_column("Tipo", header_style="green")
    table.add_column("Pontuação")
    table.add_column("Plano")

    for i in range(0, len(dados)):
        dado = dados[i]
        table.add_row(
            dado.get("nome", ""),
            dado.get("email", ""),
            dado.get("tipo", ""),
            str(dado.get("pontuacao", "")),
            dado.get("plano", "")
        )

    console = Console()
    console.print(table)

#dados para o main
# from src.exercicio_pratico_json import resolucao
# def main():
#     resolucao.resolver()



# Exercício 01
#   Percorrer a lista de usuário, armazenando no arquivo 'free.json' o nome dos usuários que tem o plano Free
# Exercício 02
#   Percorrer a lista de usuário, armazenando no arquivo 'tags.json' todas as tags dos usuários
# Exercício 03
#   Percorrer a lista de usuário, armazenando no arquivo 'enderecos.json' todos os endereços dos usuários
# Ex.: ["Rua - Numero - Bairro - CEP - UF", "Rua - Numero - Bairro - CEP - UF"]
# Exercício 04:
#   Percorrer a lista de usuários agrupando os dados por estado, salvando o telefone e e-mail de cada usuário em uma lista por estado. Deve armazenar uma lista com os usuários conforme abaixo:
#   Ex.: sc.json
#       [{"email": "elisa.rocha@example.com", "telefone": "......"}]


# Exercício 01
#   Percorrer a lista de usuário, armazenando no arquivo 'free.json' o nome dos usuários que tem o plano Free

def exercicio_01():
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")
    free_users = []

    for usuario in usuarios:
        assinatura = usuario.get("assinatura", {})
        plano = assinatura.get("plano", "")
        if plano.lower() == "free":
            dados_pessoais = usuario.get("dados_pessoais", {})
            nome = dados_pessoais.get("nome", "")
            free_users.append(nome)

    escrever_json(free_users, "data/free.json")

    # Exercício 02
#   Percorrer a lista de usuário, armazenando no arquivo 'tags.json' todas as tags dos usuários

def exercicio_02():
    usuarios:list[Dict[str,any]] = ler_json("data/usuarios.json")
    todas_tags = []
    for usuario in usuarios:
        tags = usuario.get("tags", [])
        todas_tags.extend(tags)
        escrever_json(todas_tags, "data/tags.json")

