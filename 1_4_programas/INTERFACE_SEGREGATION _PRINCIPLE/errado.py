from abc import ABC, abstractmethod


class Carro(ABC):
    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def turbo_acelerar(self, turbo):
        pass


class CarroNormal(Carro):
    def __init__(self, name):
        self.name = name
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
        print("Carro %s está acelerando" % self.name)

    def turbo_acelerar(self, turbo):
        raise Exception("Carro normal não tem turbo")


class CarroEsportivo(Carro):
    def __init__(self, name):
        self.name = name
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
        print("Carro %s está acelerando" % self.name)

    def turbo_acelerar(self, turbo):
        self.velocidade += turbo
        print("Carro %s está acelerando com turbo %d" % (self.name, turbo))


if __name__ == '__main__':
    carro = CarroNormal('Ford KA')
    carro.acelerar()
    autoCaro = CarroEsportivo('L200')
    autoCaro.turbo_acelerar(2)
    carro.turbo_acelerar(2)
