from ContasBancos import ContaCorrente, CartaoCredito

conta_sergio = ContaCorrente('sergio', '222.444.777-88', 123, 321456) # --> chamando o metodo init
cartao_sergio = CartaoCredito('Sergio', conta_sergio)
cartao_sergio.senha = '1235'

print(f'Ag: {cartao_sergio.conta_corrente._nu_conta}')
print(f'CC: {cartao_sergio.numero}')
print(f'CVV: {cartao_sergio.cod_seguranca}')
print(f'Validade: {cartao_sergio.validade}')
print(f'Limite: {cartao_sergio.limite}')

print(f'Senha: {cartao_sergio.senha}')

#print(conta_sergio.__dict__)
#print(cartao_sergio.__dict__)