import pessoa
import banco

class RegistrarBanco():

    def verificar_registro(self, _banco: banco.Banco, _person: pessoa.Pessoa) -> bool:
        return _person.dinheiro >= _banco.taxa_adesao

    def registrar(self, _banco: banco.Banco, _pesssoa: pessoa.Pessoa):
        if self.verificar_registro(_banco, _pesssoa):
            _pesssoa.dinheiro -= _banco.taxa_adesao
            _banco.adicionar_conta(_pesssoa.get_nome(), _pesssoa)