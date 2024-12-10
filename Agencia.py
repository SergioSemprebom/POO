from random import randint

class Agencia:

    def __init__(self, telefone,cnpj, numero) -> None:
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 1000000
        self.emprestimo = []
        self.caixa_paypal = 0

    def verificar_caixas(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nivel recomendado. Caixa Atual: {self.caixa:,.2f}')
        else:
            print(f'O valor de caixa está ok. caixa Atual: R$ {self.caixa:,.2f}')


    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimo.append((valor, cpf, juros))
        else:
            print('Emprestimo não disponivel. Dinheiro não disponivel em caixa.')


    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):
    
    def __init__(self, site, telefone, cnpj):
        self.site =site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1_000_000


    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor


    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor



class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1_000_000


class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10_000_000


    def adicionar_cleintes(self, nome, cpf, patrimonio):
        if patrimonio > 10_000_000:
            super().adicionar_clientes(nome, cpf, patrimonio)
        else:
            print('O cliente não atende aos requisitos')

if __name__=='__main__':
    # Programa_agenciaVirtual
    agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 13_996357080, 37457874534)
    agencia_virtual.verificar_caixas()

    # Agencia_Comum
    agencia_comum = AgenciaComum(13_996357080, 37457874534)

    # Agencia_Premium
    agencia_premium = AgenciaPremium(13_996357080, 37457874534)

    agencia_virtual.depositar_paypal(20_000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)
