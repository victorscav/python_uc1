class Conta:
    def __init__(self, numero, titular , limite):
        self.numero = numero
        self.titular = titular
        self.saldo = 0
        self.limite = limite

    def deposito(self, valor):
        print(f"\nOPERAÇÃO DE DEPÓSITO:")
        print(f"Saldo inicial: R${self.saldo}")
        self.saldo = self.saldo + valor
        print(f"Saldo final: R${self.saldo}")
        
    def saque(self, valor):
        if valor > self.limite:
            return print("OPERAÇÃO NEGADA: O saque excede o limite da conta")
        print(f"\nOPERAÇÃO DE SAQUE:")
        print(f"Saldo inicial: R${self.saldo}")
        self.saldo = self.saldo - valor
        print(f"Saldo final: R${self.saldo}")

    def exibir_info(self):
        print(f"\nNúmero da conta: {self.numero} \nNome do titular: {self.titular} \nSaldo disponível: R${self.saldo} \nLimite disponível: R${self.limite} ")

class Banco:
    def __init__(self) :
        self.contas={}


if __name__ == "__main__":
    cc1 = Conta("00001", "Victor", 6000)
    print(f"Criando a primeira conta:")
    cc1.exibir_info()
    valor_deposito=float(input("Digite o valor do depósito: R$"))
    cc1.deposito(valor_deposito)
    valor_saque=float(input("Digite o valor do saque: R$"))
    cc1.saque(valor_saque)