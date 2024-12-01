from datetime import datetime
import pytz

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

    

    def _data_hora():
        fuso_BR = pytz.timezone('America/Sao_Paulo')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')


    def __init__(self, nome, cpf, agencia, nu_conta): # --> metodo construtor
        self.nome = nome # --> atributo nome
        self.cpf = cpf # --> atributo cpf
        self.saldo = 0 # --> atributo saldo
        self.limite = None
        self.agencia = agencia
        self.nu_conta = nu_conta
        self.transacoes = []


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



# Programa escrito manualmente
conta_sergio = ContaCorrente('sergio', '222.444.777-88', 123, 321456) # --> chamando o metodo init
conta_sergio.consultar_saldo()# consulta o primeiro valor do metodo init

# Depositando um dinheiro na conta corrente
conta_sergio.depositar(10000)
conta_sergio.consultar_saldo()

print('Saldo Final')
conta_sergio.consultar_saldo()
conta_sergio.consultar_limite_chequeespecial()


# Conta Sergio Consultar
print('-'*20, 'Histórico de Transações', '-'*20)
conta_sergio.consultar_historico_transacoes()


# Conta Aleteia Consultar
print('-'*20, 'Histórico de Transações', '-'*20)
conta_aleteia = ContaCorrente('Aleteia', '345.875.768-45', 123, 321456) # --> chamando o metodo init
conta_sergio.transferir(1000, conta_aleteia)


conta_sergio.consultar_saldo()
conta_aleteia.consultar_saldo()

print('-'*20, 'Histórico de Transações', '-'*20)
conta_sergio.consultar_historico_transacoes()
conta_aleteia.consultar_historico_transacoes()

