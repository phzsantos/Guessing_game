import random

estado = True

while estado:
    input('Pense em um numero e depois aperte Enter ')

    tentativa = random.randint(0,10)

    resultado = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))

    if resultado:
        print('Adivinhei.')
        estado = False
    else:
        resultado = int(input(f'Seu numero e maior ou menor que {tentativa}? (0 - Menor / 1 - Maior):' ))
        
        if resultado:
            tentativa = random.randint(tentativa+1,10)

            resultado = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))

            while not resultado:
                tentativa = random.randint(tentativa+1,10)

                resultado = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))

            print('Demorou mas eu advinhei rsrsrs')
            estado = False    
        else:
            tentativa = random.randint(0,tentativa-1)

            resultado = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))

            while not resultado:
                tentativa = random.randint(0,tentativa-1)

                resultado = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))

            print('Demorou mas eu advinhei rsrsrs')
            estado = False
