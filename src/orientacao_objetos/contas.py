class Conta:

    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.saldo = saldo_inicial 
    

    def depositar(self, valor_deposito: float):
        """"Adiciona um valor ao saldo da conta."""
        if valor_deposito <= 0:
            print(f"DEPOSITO: Valor de deposito invalido R${valor_deposito:.2f}")
            return
        

        self.saldo = self.saldo + valor_deposito
        print(f"DEPOSITO: Deposito de R${valor_deposito:.2f} realizado com sucesso")



    def sacar(self, valor_saque: float):
        """Remove um valor do saldo da conta, se houver dinheiro suficiente."""
        if valor_saque > self.saldo:
            print(f"SAQUE: Saldo insuficiente para realizar o saque de R${valor_saque:.2f}")

        self.saldo=self.saldo - valor_saque
        print(f"SAQUE: Saque de R${valor_saque:.2f} realizado com sucesso")


    def exibir_saldo(self):
        """Mostra o status atual da conta."""
        print(f"EXTRATO: Saldo atual de R${self.saldo:.2f}")



def exemplo_conta():
    """Metodo para testar a funcionalidade da conta"""
    conta_bradesco = Conta("Vitor", 3900.22)

    conta_bradesco.exibir_saldo()
    conta_bradesco.sacar(800) #3100.22


    conta_bradesco.exibir_saldo()
    conta_bradesco.depositar(100.78)
    conta_bradesco.depositar(-10)

    conta_bradesco.sacar(4000) #Nao permitir pois saldo insuficiente

    conta_bradesco.sacar(3500) #Nao permitir pois saldo insuficiente
    conta_bradesco.sacar(3201)
    conta_bradesco.exibir_saldo()

# exemplo_conta()


# criar uma classe aluno com o um construtor que receba o nome do aluno
# Dentro do construtor deve criar uma lista vazia de notas

# Criar um metodo adicionar qe recebe como parametro a nota e adicionar a lista de notas
# Criar um metodo que apresenta as notas
# criar um metodo calcular media que percorre cada uma das notas e apresenta a media para o usuario

class Aluno:
    def __init__(self, nome:str):
        self.nome = nome
        self. notas = [] #lista vazia construtor

    
    def adicionar_nota(self, nota: float):
        self.notas.append(nota)

    
    def apresentar_notas(self):
        print(f"Notas de {self.nome}: {self.notas}")


    def calcular_media(self):
        if len(self.notas) == 0:
            print("Nenhuma nota cadastrada.")
            return
        
        soma = 0
        for n in self.notas:
            soma += n

        media = soma / len(self.notas)
        print (f"Media de {self.nome}: {media:.2f}")

aluno1 = Aluno("Roberto")

aluno1.adicionar_nota(8)
aluno1.adicionar_nota(7.5)
aluno1.adicionar_nota(9)

aluno1.apresentar_notas()
aluno1.calcular_media()