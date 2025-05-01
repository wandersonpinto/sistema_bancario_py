from datetime import datetime, timedelta

class ContaBancaria:
    def __init__(self, numero_conta):
        self.numero_conta = numero_conta
        self.saldo = 0
        self.historico = []  # Lista para armazenar todas as transações
        self.saques_diarios = 0
        self.ultimo_dia_saque = None

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append((datetime.now(), "Depósito", valor))
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso. Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("Valor de depósito inválido. O valor deve ser positivo.")

    def saque(self, valor):
        hoje = datetime.now().date()
        if self.ultimo_dia_saque is None or self.ultimo_dia_saque < hoje:
            self.saques_diarios = 0
            self.ultimo_dia_saque = hoje

        if self.saques_diarios < 3:
            if 0 < valor <= 500 and valor <= self.saldo:
                self.saldo -= valor
                self.historico.append((datetime.now(), "Saque", valor))
                self.saques_diarios += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso. Novo saldo: R$ {self.saldo:.2f}")
            else:
                print("Valor de saque inválido (limite diário de R$ 500,00 ou saldo insuficiente).")
        else:
            print("Limite de 3 saques diários atingido.")

    def extrato(self):
        print("\nEXTRATO:")
        print(f"Número da conta: {self.numero_conta}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        if self.historico:
            print("\nHistórico de Transações:")
            for data, tipo, valor in self.historico:
                print(f"{data.strftime('%d/%m/%Y %H:%M:%S')} - {tipo}: R$ {valor:.2f}")
        else:
            print("\nNão há transações registradas.")


def main():
    numero_conta = input("Digite o número da conta: ")
    conta = ContaBancaria(numero_conta)

    while True:
        print("\nEscolha uma opção:")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Sair")

        opcao = input("Sua escolha: ")

        if opcao == '1':
            valor = float(input("Digite o valor a depositar: "))
            conta.deposito(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a sacar: "))
            conta.saque(valor)
        elif opcao == '3':
            conta.extrato()
        elif opcao == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
