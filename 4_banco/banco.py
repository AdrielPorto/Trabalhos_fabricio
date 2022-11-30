import pessoa
import conta_banco

class Banco():
    def __init__(self, _nome: str, _deposito_minimo: float, _taxa_adesao: float):
        self.nome: str = _nome
        self.deposito_minimo: float = _deposito_minimo
        self.taxa_adesao: float = _taxa_adesao
        self.total_no_cofre: float = 0
        self.contas = []

    def calcular_total(self) -> float:
        self.total_no_cofre = 0
        for ac in self.contas:
            self.total_no_cofre += ac.get_saldo()
        return self.total_no_cofre

    def adicionar_conta(self, _nome_conta, _pessoa: pessoa.Pessoa):
        self.contas.append(conta_banco.ContaCorrente(_pessoa.get_nome(), _pessoa.get_nome(), _pessoa.get_idade(), _pessoa.get_genero(), "0123"))
    
    def mostrar_conta(self, conta):
        nome_conta = conta.get_nome_conta()
        nome = conta.get_nome()
        bal = conta.get_saldo()
        idade = conta.get_idade()
        genero = conta.get_genero()
        print(f"Nome Conta: {nome_conta}")
        print(f"Saldo: R${bal} \n")
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"Genero: {genero}")
        

    def get_nome(self):
        return self.nome
    
    def get_totalvalue(self) -> float: return self.total_no_cofre

