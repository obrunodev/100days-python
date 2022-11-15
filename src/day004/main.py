from random import randint


def main(options):
    # Apresentação
    print('Vamos jogar Pedra, Papel, Tesoura?')
    print('Escolha entre 1(Pedra), 2(Papel), 3(Tesoura).')
    
    # Tratamento de erros.
    try:
        my_choice = int(input('Digite uma opção: '))
    except:
        return "Essa opção é inválida!"
    if my_choice not in options:
        return "Essa opção não existe!"
    
    # Apresentando escolhas
    print('Você escolheu %s' % (options[my_choice],))
    opponent_choice = randint(1, 3)
    print('O oponente escolheu %s' % (options[opponent_choice]))
    
    # Calculando e apresentando resultado
    if my_choice == opponent_choice:
        result = "Deu empate!"
    elif my_choice == 3 and opponent_choice == 2:
        result = "Você venceu!"
    elif my_choice == 2 and opponent_choice == 1:
        result = "Você venceu!"
    elif my_choice == 1 and opponent_choice == 3:
        result = "Você venceu!"
    else:
        result = "Você perdeu!"
    return result


if __name__ == '__main__':

    options = {1: 'Pedra',
                2: 'Papel',
                3: 'Tesoura'}
    result = main(options)
    print(result)