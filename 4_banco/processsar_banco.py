import pessoa
import banco
import conta_banco
from abc import ABC, abstractmethod

class Processo(ABC):
    def __init__(self):
        self.conta = None

    def verificar_conta(self, _banco: banco.Banco, _pessoa: pessoa.Pessoa):
        for acc in _banco.contas:
            if (acc.get_nome() == _pessoa.get_nome()):
                self.conta = acc
                return True
        return False

class ProcessoDeposito(Processo):
    def depositar_dinheiro(self, _deposito_dinheiro: float, _banco: banco.Banco, _pessoa: pessoa.Pessoa):
        if (self.verificar_conta(_banco, _pessoa) and _pessoa.dinheiro >= _deposito_dinheiro):
            _pessoa.pagar_dinheiro(_deposito_dinheiro)
            self.conta.deposito(_deposito_dinheiro)
            _banco.mostrar_conta(self.conta)
            _banco.calcular_total()

class ProcessoSaque(Processo):
    def retirar_dinheiro(self, _sacar_dinheiro: float, _banco: banco.Banco, _pessoa: pessoa.Pessoa):
        if (self.verificar_conta(_banco, _pessoa) and self.conta.get_saldo() >= _sacar_dinheiro):
            self.conta.saque(_sacar_dinheiro)
            _pessoa.receber_dinheiro(_sacar_dinheiro)
            _banco.mostrar_conta(self.conta)
            _banco.calcular_total()