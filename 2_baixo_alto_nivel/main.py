class Cozinheiro:
    @staticmethod
    def cozinhar(prato: str, menu=None) -> None:
        print(menu.cozinhar(prato=prato))


class Jantar:
    @staticmethod
    def cozinhar(prato: str) -> None:
        print(f'Cozinhando: {prato}')


class Sobremesa:
    @staticmethod
    def cozinhar(prato: str) -> None:
        print(f'Cozinhando: {prato}')

if __name__ == '__main__':
    teste = Cozinheiro()
    teste.cozinhar("Lasanha", Jantar())
    teste.cozinhar("Pudim", Sobremesa())
