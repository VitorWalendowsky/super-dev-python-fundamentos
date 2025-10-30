def solicitar_string():
    nome: str = input("Digite seu nome: ")
    print("Nome digitado: " + nome)

def solicitar_float():
        nota_1: float = float(input("Digite a primeira nota: "))
        print("Nota 1 digitada: " + str(nota_1))

def solicitar_int():
            numero1: int = int(input("Digite o numero1: "))
            numero2: int = int(input("Digite o numero2: "))
            print("Numero 1 digitado: " + str(numero1))
            print("Numero 2 digitado: " + str(numero2))
            soma: int = numero1 + numero2
            print("Soma dos numeros: " + str(soma))