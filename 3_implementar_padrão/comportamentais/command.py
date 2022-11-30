from abc import ABC, abstractmethod


class Comando(ABC):

    def __init__(self, receptor):
        self.receptor = receptor

    def processo(self):
        pass


class ComandoImplementa(Comando):

    def __init__(self, receptor):
        self.receptor = receptor

    def processo(self):
        self.receptor.executar_acao()


class Receiver:

    def executar_acao(self):
        print('Ação realizada no receptor.')


class Chamar:

    def comando(self, cmd):
        self.cmd = cmd

    def executar(self):
        self.cmd.processo()


if __name__ == "__main__":
    receptor = Receiver()
    cmd = ComandoImplementa(receptor)
    chamar = Chamar()
    chamar.comando(cmd)
    chamar.executar()
