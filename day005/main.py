from random import randint, shuffle

# Criar um gerador de senhas
def main(letras_minusculas, letras_maiusculas, numeros, caracteres):
    # Perguntas
    numero_letras = int(input('Quantas letras terá a senha?\n'))
    numero_caracteres = int(input('Quantos caracteres você gostaria?\n'))
    numero_numeros = int(input('Quantos números você gostaria?\n'))

    # gerar senha
    password = []
    for _ in range(numero_letras):
        tipo_letra = [letras_minusculas, letras_maiusculas]
        tipo_escolhido = randint(0, 1)
        password.append(tipo_letra[tipo_escolhido][randint(0, len(tipo_letra[tipo_escolhido])-1)])

    for _ in range(numero_numeros):
        password.append(numeros[randint(0, len(numeros)-1)])
        
    for _ in range(numero_caracteres):
        password.append(caracteres[randint(0, len(caracteres)-1)])
    
    # Unir itens da lista para formar a senha
    shuffle(password)
    return ''.join(password)

if __name__ == '__main__':
    letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
    letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    caracteres = '!@#$%&*()'
    numeros = '0123456789'

    senha_gerada = main(letras_minusculas, letras_maiusculas, numeros, caracteres)
    print(senha_gerada)
