# Criar uma calculadora de gorjeta
# Pedir o valor do pedido
valor_pedido = float(input('Valor do pedido: R$ '))

# Perguntar quantos % deseja pagar de gorjeta
porcentagem_gorjeta = int(input('Porcentagem de gorjeta a ser paga: '))

# Perguntar em quantas pessoas será dividido o pagamento
quantas_pessoas = int(input('Quantidade de pessoas que irão pagar: '))

# Printar o resultado com valores arredondados
valor_total = valor_pedido + (porcentagem_gorjeta / 100 * valor_pedido)
valor_por_cabeca = valor_total / quantas_pessoas
print(f'Valor total: R$ {round(valor_total, 2)}')
print(f'Valor por cabeça: R$ {round(valor_por_cabeca, 2)}')
