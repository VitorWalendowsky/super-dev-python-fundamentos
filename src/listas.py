from typing import List


def exemplo_lista_basica():
    #Criando uma lista de string e armazenando um nome
    nomes: List[str] = ["Joao"]


    #Acrescentar item na lita
    nomes.append("Maria")

    #Obter o nome da posi;'ao zero
    nome_primeira_posicao = nomes[0]

    # Alterar o nome do Joao qu esta na primeira posica
    nomes[0] = "Joao Clebber"

    # Adicionar elemento para depois apagar
    nomes.append("Lucio")

    #Apagar um elemnto da lista
    nomes.remove("Lucio")

    tamanho_lista = len(nomes)

    print(f"""Primeiro nome: {nomes[0]}
Segundo nome: {nomes[1]}
Tamanho da lista: {tamanho_lista}
""")
    


def exemplo_solicitar_dados_usuario():
    valores=[]

    valores.append(float(input("Digite o valor do produto: ")))
    valores.append(float(input("Digite o valor do produto: ")))
    valores.append(float(input("Digite o valor do produto: ")))
    valores.append(float(input("Digite o valor do produto: ")))
    valores.append(float(input("Digite o valor do produto: ")))

    soma = valores[0] + valores[1] + valores[2] + valores[3] + valores[4]

    print(valores)
    print(soma)

    # para i de 0 a 5

    for i in range (0,5):
        valores.append(float(input("Digite o valor do produto: ")))

        soma = 0
        for i in range (0,5):
            valor = valores[i]
            some = soma + valor
        print (f"Soma: {soma}")


def exemplo_lista_com_dicionario():
    # pip install --requirement requirements.txt
    
    # Solicitar cep, valor imóvel, cnpj
    # Fazer requisição para pegar os dados da empresa buscando através do CNPJ
    # Fazer requisição para pegar os dados do endereço buscando através do CEP
    # Cadastrar este imóvel na lsita de imóveis
    # Continuar perguntando até finalizar
    # Salvar em um arquivo json
    # Outro exercício é importar este json
    

    