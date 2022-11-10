# Gerador de nomes para bandas

# Boas-vindas ao usuário
print('Olá, seja bem-vindo ao gerador de nomes para bandas!')

# Pedir o nome da cidade em que nasceu
cidade = input('Digite o nome da cidade em que nasceu: ')

# Pedir o nome de um pet
animal = input('Digite o nome de um animal: ')

# Combinar ambos e printar
nome_da_banda = '%s %s' % (cidade, animal)
print(f'O que você acha de {nome_da_banda}?')