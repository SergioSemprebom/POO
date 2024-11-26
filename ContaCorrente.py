
# Construindo uma classe de conta corrente
class ContaCorrente(): # --> classe

    def __init__(self, nome, cpf): # --> metodo construtor
        self.nome = nome # --> atributo nome
        self.cpf = cpf # --> atributo cpf
        self.saldo = 0 # --> atributo saldo
        self.limite = None


# Criando um função para consulta de Saldo
# A função precisa ser direta e objetiva
    def consultar_saldo(self):
        print(f'O saldo da sua conta é de R$ {self.saldo:,.2f} reais')

    
# Criando uma função para depositar dinheiro
# A função precisa ser direta e objetiva
# Chamando o atributo saldo para ser modificado
    def depositar(self, valor):
        self.saldo += valor

    
    def limite_conta(self):
        self.limite = -1000
        return self.limite


    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self.limite_conta():
            print(f'Voce nao tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
             self.saldo -= valor


# Programa escrito manualmente
conta_sergio = ContaCorrente('sergio', '222.444.777-88') # --> chamando o metodo init
conta_sergio.consultar_saldo()# consulta o primeiro valor do metodo init

# Depositando um dinheiro na conta corrente
conta_sergio.depositar(10000)
conta_sergio.consultar_saldo()

# Sacando um dinheiro da conta
conta_sergio.sacar_dinheiro(10500)


print('Saldo Final')
conta_sergio.consultar_saldo()

