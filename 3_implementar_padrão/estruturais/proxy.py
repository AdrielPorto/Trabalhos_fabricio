from abc import ABC, abstractmethod


class Cliente:

    def __init__(self, idade):
        self.__idade = idade

    def get_idade(self):
        return self.__idade


class PlayboyTV(ABC):

    @abstractmethod
    def fornecer_transmissao(self):
        pass


class Canal(PlayboyTV):

    def fornecer_transmissao(self):
        print("Transmissão iniciada")


class ProxyCanal(PlayboyTV):

    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.canal = Canal()

    def fornecer_transmissao(self):
        cliente_idade = self.cliente.get_idade()
        if cliente_idade > 18:
            self.canal.fornecer_transmissao()
            print("Este serviço está registrado para cobrança.")
        else:
            print("Desculpe, este serviço não é permitido para clientes menores de 18 anos.")

if __name__ == '__main__':
    D = Cliente(17)
    P = ProxyCanal(D)
    P.fornecer_transmissao()
