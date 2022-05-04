from Conta.conta import Conta
from Conta.conta_poupança import ContaPoupanca
'''
class Criarpoupanca:
    if __name__ == '__main__':
        poupanca = ContaPoupanca("21.342-7")
        poupanca.creditar(500.87)
        poupanca.debitar(45.00)

        print(poupanca.get_saldo())

        poupanca.render_juros(0.01)
        print(poupanca.get_saldo())
    '''

class CriarPoupanca:
    if __name__ == '__main__':
        conta = Conta("21.342-7")
        print(type(conta))
        conta = ContaPoupanca("21.342-7")
        print(type(conta))

        conta.creditar(500.87)
        conta.debitar(45.00)
        print(conta.get_saldo())