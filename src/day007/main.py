from palavras import animais
from random import randint

def jogo_da_forca():
    vidas = 5
    chutes = []
    fim_de_jogo = False
    resposta = animais[randint(0, len(animais)-1)].lower()
    palavra_oculta = "".join(["_" for _ in range(len(resposta))])

    print("JOGO DA FORCA")
    print(resposta)
    print(palavra_oculta)
    
    while not fim_de_jogo:
        chute = input("Digite uma letra: ").lower()

        if len(chute) > 1:
            print("Digite apenas UMA letra!")
            continue

        # Verifica se a letra já foi usada
        if chute in chutes:
            print("Você já chutou essa letra, tente outra.")
            continue
        else:
            chutes.append(chute)

        # Substituir todas as posições pela letra da resposta.
        if chute in resposta:
            for idx, letra in enumerate(resposta):
                if chute == letra:
                    palavra_oculta = palavra_oculta[:idx] + chute + palavra_oculta[idx+1:]
        else:
            # Se não existe a letra na palavra, tira uma vida
            vidas -= 1
            print("Não possui essa letra na palavra.")
            print(f"Você tem {vidas} vidas.")
        
        print(palavra_oculta)
        
        if vidas == 0:
            print("Você perdeu o jogo!")
            fim_de_jogo = True
        
        if not "_" in palavra_oculta:
            print("Parabéns! Você venceu o jogo da forca.")
            fim_de_jogo = True
        

if __name__ == '__main__':
    jogo_da_forca()
