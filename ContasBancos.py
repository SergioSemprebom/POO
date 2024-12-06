from datetime import datetime
import pytz
from random import randint


# Construindo uma classe de conta corrente
class ContaCorrente():
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.


    Atributos:
        nome (str): Nome do Cliente.
        cpf (str): CPF do cliente. Deve ser inseridos com pontos e traços.
        agencia (int): Agencia Responsavel pela conta do cliente.
        nu_conta (int): Número da Conta Corrente do cliente.
        saldo : Saldo disponivel na conta do cliente.
        limite: limite de Cheque especial daquele cliente.
        transacoes: Histórico de transacoes do cliente.
    """


    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('America/Sao_Paulo')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')


    def __init__(self, nome, cpf, agencia, nu_conta): # --> metodo construtor
        self._nome = nome # --> atributo nome
        self._cpf = cpf # --> atributo cpf
        self._saldo = 0 # --> atributo saldo
        self._limite = None
        self._agencia = agencia
        self._nu_conta = nu_conta
        self._transacoes = []
        self.cartoes = []


    def consultar_saldo(self):
        """
            Exibe o saldo atual da conta do cliente.
            Não ha parametros necessarios.
        :return:
        """
        print(f'O saldo da sua conta é de R$ {self.saldo:,.2f} reais')

    
# Criando uma função para depositar dinheiro
# A função precisa ser direta e objetiva
# Chamando o atributo saldo para ser modificado
    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    
    def limite_conta(self):
        self.limite = -1000
        return self.limite


    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self.limite_conta():
            print(f'Voce nao tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
             self.saldo -= valor
             self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))


    def consultar_limite_chequeespecial(self):
        print(f'Seu limite de cheque especial é de R$ {self.limite_conta():,.2f} reais')



    def consultar_historico_transacoes(self):
        print('Histórico de transações:')
        print('valor, saldo, Data e Hora')
        for transacoes in self.transacoes:
            print(transacoes)

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('America/Sao_Paulo')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR


    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)


    @property
    def senha(self):
        return self._senha
    
    @senha.getter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Nova Senha Inválida')
        