import random

resposta = 0

while (resposta == 0):
    input('Pense em um numero e depois aperte Enter')

    tentativa = random.randint(0,10)

    resposta = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))
    
    if (resposta == 1):
        print("Acertei!")
    else:
        while (resposta == 0):
            maior_ou_menor = int(input("Seu numero é maior ou menor? (0 - Menor/ 1 - Maior)"))

            if (maior_ou_menor == 0):
                tentativa = random.randint(0,tentativa)

            else:
                tentativa = random.randint(tentativa, 10)
 
            resposta = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))
    
            if (resposta == 1):
                print("Acertei!")
