from typing import Dict, Union

def exemplo_dicionario_basico():
    # Dicionario e uma forma de armazenar chaves e valores
    # Cada chave esta atrelado a um valor

    # Criamos um dicionario com 2 chaves (apelido, idade)
    cachorro: Dict[str, Union[str, int,bool]] = {
        "apelido": "Tobby",
        "idade": 4,
        "abandonado": True
    }

    # Acrescentar uma nova chave com um valor

    cachorro["raca"] = "Pastor Alemao"

    cachorro["cor"] = "Caramelo"

    # Alterar o valor de uma chave
    cachorro["idade"]= 5

    # Remover uma chave (automaticamente remove o valor)
    cachorro.pop("abandonado")

    #print("Cachorro: ", cachorro["apelido"])

    print(f"""
          Cachorro: {cachorro.get("apelido")}
          Raca: {cachorro.get("raca")}
          Idade: {cachorro.get("idade")}
          Cor: {cachorro.get("cor")}
          Abandonado: {cachorro.get("abandonado")}
          Peso: {cachorro.get("peso")}
          """)
    

    # #Exercicio 01:
    # Criar uma funcao exemplo_dicionario_aluno
    # criar um dicionario chamado aluno com os seguintes dados
    #     nome_completo
    #     nome_mae
    #     nome_pai
    #     jogar (true)
    # apresentar os dados do exemplo_dicionario
    # adicionar a chave idade do aluno
    # apresentar a idade do aluno
    # alterar a idade do aluno para +1
    # remover a chave jogar do aluno
    # apresentar dados

def exemplo_dicionario_aluno():

    
    aluno: Dict[str, Union[str, int, bool]] = {
        "nome_completo": "Claudio Silva",
        "nome_mae": "Maria Silva",
        "nome_pai": "Carlos Silva",
        "jogar": True
    }
        
    print(f"""
Nome Completo: {aluno.get("nome_completo")}
Nome da Mae: {aluno.get("nome_mae")}
Nome do Pai: {aluno.get("nome_pai")}
jogar: {aluno.get("jogar")}
        """)
    
    #Adicionar idade
    aluno["idade"] = 30
    print(f"Idade: {aluno.get("idade")}")

    #Adicionar +1 na idade
    aluno["idade"] +=1
    print(f"Nova idade: {aluno.get("idade")}")

    #Remover o jogar
    aluno.pop("jogar")

    #Novo print
    print(f"""
Nome completo: {aluno.get("nome_completo")}
Nome da mãe: {aluno.get("nome_mae")}
Nome do pai: {aluno.get("nome_pai")}
Idade: {aluno.get("idade")}
Jogar: {aluno.get("jogar")}
         """)