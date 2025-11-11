from pathlib import path
from typing import List
from json import dumps, load #dumps ()
#import json / json.dumps()

def escrever_json(data:List, nome_arquivo:str):
    caminho = path(nome_arquivo).resolve()
    #converte um objet de python para uma string JSON
    json_string = dumps(data, ensure ascii=False) # Serializado
    with open(caminho, mode="w", encoding="utf-8") as arquivo:
        arquivo.write(json_string)
        arquivo.flush()



def ler_json(nome_arquivo:str) -> List| dict:
    caminho = path(nome_arquivo).resolve()
    with open(caminho, mode="r", encoding="utf-8") as arquivo:
        dado_deserializado = load(arquivo)
        return dado_deserializado
    
def exemplos_criar_arquivo():
    produtos = [
        {
            "nome": "Abacadte",
            "preco": 25.00
        },
        {
            "nome": "Banana",
            "preco": 4.50
        },
        {
            "nome": "Uva",
            "preco": 6.70
        }
    ]
    escrever_json(produtos, "produtos.json")

    games=["Minecraft", "Roblox", "Fortnite"]
    escrever_json(games, "games.json")

    mine = {
        "nome": "Minecraft",
        "preco": 350.00
    }
    escrever_json(mine, "mine.json")

# exemplos_criar_arquivo()

# produtos = ler_json("pridutos.json")
# games = ler_json("games.json")
# mine = ler_json("mine.json")

# print(produtos[2].get("nome"))
# prit(games[0])
# print(mine.get("nome"))