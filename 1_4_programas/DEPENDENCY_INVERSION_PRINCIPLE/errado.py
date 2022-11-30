class Maca:
    def comer(self):
        print(f"Comendo maça. Transferindo {5} unidades de energia")

class Chocolate:
    def comer(self):
        print(f"Comendo chocolante. Transferindo {10} unidades de energia")

class Robo:
    def obter_energia(self, comestivel: str):
        if comestivel == "Maca":
            maca = Maca()
            maca.comer()
        elif comestivel == "Chocolate":
            chocolate = Chocolate()
            chocolate.comer()

if __name__ == '__main__':
    robo = Robo()
    robo.obter_energia("Maca")
