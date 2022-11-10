from time import sleep

# Desenvolver um jogo de tomada de decisões.
print('Você está andando em uma floresta e encontra uma bifurcação.')
caminho = input('Para qual lado deseja ir? [direita/esquerda]\n')

if caminho == 'esquerda':
    print('Você foi pego por um monstro e morreu!')
elif caminho == 'direita':
    print('No caminho você avista uma casa aparentemente abandonada.')
    entrar = input('Deseja entrar na casa? [sim/não]\n')
    if entrar == 'sim':
        print('Você não aprendeu nada com filmes de terror? Morreu!')
    elif entrar == 'não':
        print('Garoto esperto, evitou o perigo!')
        sleep(1)
        print('Você deu de cara com um grande tesouro!')
        pegar_tesouro = input('Você deseja pegar uma parte do tesouro? [sim/não]\n')
        if pegar_tesouro == 'sim':
            quantidade = int(input('Quantos porcento do tesouro você pega?\nR: '))
            if quantidade > 15:
                print('Você pegou muito e os piratas perceberam, te caçaram, e o resto, você já sabe...')
            else:
                print('Muito bem, foi pra casa rico! Parabéns! O jogo termina aqui.')
        elif pegar_tesouro == 'não':
            print('Bom, não custava ter pego um pouco... foi para casa de mãos vazias.')
        else:
            print(f'Digitou errado nessa altura do campeonato? Merece a morte! (Você digitou: {pegar_tesouro})')
    else:
        print('O que você tá falando!? Comece de novo!')
else:
    print(f'Você digitou {caminho}, e por isso morreu.')