from abc import ABC, abstractmethod


class Comestivel(ABC):
    @abstractmethod
    def comer(self):
        return NotImplemented


class Maca(Comestivel):
    def comer(self):
        print(f"Comendo maça. Transferindo {5} unidades de energia")


class Chocolate(Comestivel):
    def comer(self):
        print(f"Comendo chocolante. Transferindo {10} unidades de energia")


class Robot:
    def get_energy(self, comestivel: Comestivel):
        comestivel.comer()


if __name__ == '__main__':
    robot = Robot()
    robot.get_energy(Maca())
