from abc import ABC, abstractmethod

class ContaBanco(ABC):
    def __init__(self, _nome_conta: str, _nome: str, _idade: int, _genero: str):
        self.nome_conta: str = _nome_conta
        self.nome: str = _nome
        self.idade: int = _idade
        self.genero: str = _genero
        self.saldo: float = 0
    
    def deposito(self, _amount) -> float: self.saldo += _amount
    def saque(self, _amount) -> float: self.saldo -= _amount
    def get_nome(self) -> str: return self.nome
    def get_nome_conta(self) -> str: return self.nome_conta
    def get_idade(self) -> int: return self.idade
    def get_genero(self) -> str: return self.genero
    def get_saldo(self) -> float: return self.saldo

class ContaCorrente(ContaBanco):
    def __init__(self, _nome_conta: str, _nome: str, _idade: int, _genero: str, _numero_pin: str):
        super().__init__(_nome_conta, _nome, _idade, _genero)
        self.numero_pin: str = _numero_pin

    def get_pin(self) -> str: return self.numero_pin
    def set_pin(self, _novo_pin: str) -> str: self.numero_pin = _novo_pin

class SavingsAccount(ContaBanco):
    def __init__(self, _nome_conta: str, _nome: str, _idade: int, _genero: str, _juros: float):
        super().__init__(_nome_conta, _nome, _idade, _genero)
        self.taxa_juros: float = _juros
    
    def get_juros(self) -> float: return self.juros