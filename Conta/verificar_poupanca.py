from Conta.conta import Conta
from Conta.conta_poupança import ContaPoupanca


class VerificaPoupanca:
    if __name__ == '__main__':
        opcao = int(input("Escolha [1] Conta e [2] Poupanca: "))
        if opcao == 1:
            conta = Conta("21.342-7")

        else:
            conta = ContaPoupanca("21.342-7")

        conta.creditar(500.87)
        conta.debitar(45.00)

        if isinstance(conta, ContaPoupanca):
            conta.render_juros(0.1)
            print("saldo com juros: {}". format(conta.get_saldo()))