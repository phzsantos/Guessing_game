import random

estado = True

while estado:
    input('Pense em um numero e depois aperte Enter ')

    tentativa = random.randint(0,10)  # variavel sempre tem que ter nome minusculo e separado por _

    resultado = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))

    if resultado == True:
        print('Adivinhei.')
        estado = False 