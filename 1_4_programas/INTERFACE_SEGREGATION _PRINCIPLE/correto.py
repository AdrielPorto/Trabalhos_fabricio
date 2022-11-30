from abc import ABC, abstractmethod


class SemTurbo(ABC):
    @abstractmethod
    def __init__(self, nome):
        pass

    @abstractmethod
    def acelerar(self):
        pass


class ComTurbo(SemTurbo):
    @abstractmethod
    def turbo_acelerar(self):
        pass


class CarroNormal(SemTurbo):
    def __init__(self, nome):
        self.nome = nome
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
        print("O carro %s está acelerando" % self.nome)


class CarroEsportivo(ComTurbo):
    def __init__(self, nome):
        self.nome = nome
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
        print("O carro %s está acelerando" % self.nome)

    def turbo_acelerar(self, turbo):
        self.velocidade += turbo
        print("O carro %s está acelerando com turbo %d" % (self.nome, turbo))


if __name__ == '__main__':
    carro = CarroNormal('Ford KA')
    carro.acelerar()

    autoCarro = CarroEsportivo('L200')
    autoCarro.turbo_acelerar(2)
