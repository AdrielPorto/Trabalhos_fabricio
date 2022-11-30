import banco
import pessoa
import registrar_banco
import processsar_banco


def main():
    br = registrar_banco.RegistrarBanco()
    bpd = processsar_banco.ProcessoDeposito()
    bps = processsar_banco.ProcessoSaque()
    Banco = banco.Banco("Nubank", 20, 13.75)
    print(f"Nome do Banco: {Banco.get_nome()} \n"
          f"Taxa de Adesão: {Banco.taxa_adesao} \n"
          f"Depósito Mínimo: R${Banco.deposito_minimo} \n")
    Pessoa = pessoa.Pessoa("Adriel", 22, "Masculino", 2050.00)
    br.registrar(Banco, Pessoa)
    bpd.depositar_dinheiro(200.00, Banco, Pessoa)
    bpd.depositar_dinheiro(120.00, Banco, Pessoa)
    bpd.depositar_dinheiro(90.00, Banco, Pessoa)
    bpd.depositar_dinheiro(310.00, Banco, Pessoa)
    bpd.depositar_dinheiro(100.00, Banco, Pessoa)
    bpd.depositar_dinheiro(80.00, Banco, Pessoa)
    bpd.depositar_dinheiro(415.00, Banco, Pessoa)
    bps.retirar_dinheiro(100.00, Banco, Pessoa)
    print(f"Saldo de {Pessoa.nome}: R${Pessoa.dinheiro}")
    pass


if __name__ == '__main__':
    main()
