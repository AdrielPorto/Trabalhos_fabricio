
class Pessoa:
    def __init__(self, _nome: str, _idade: int, _genero: str, _dinheiro: float):
        self.nome: str = _nome
        self.idade: int = _idade
        self.genero: str = _genero
        self.dinheiro: float = _dinheiro

    def get_nome(self) -> str: return self.nome
    def get_idade(self) -> int: return self.idade
    def get_genero(self) -> str: return self.genero

    def pagar_dinheiro(self, valor_pagamento) -> float: self.dinheiro -= valor_pagamento
    def receber_dinheiro(self, rec_dinheiro) -> float: self.dinheiro += rec_dinheiro