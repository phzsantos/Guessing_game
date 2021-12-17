import random

resposta = 0
tentativas_erradas = []

while (resposta == 0):
    input('Pense em um numero e depois aperte Enter')

    tentativa = random.randint(0,10)

    resposta = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))
    
    if (resposta == 1):
        print("Acertei!")
    else:
        tentativa_limite = tentativa

        while (resposta == 0):
            tentativas_erradas.append(tentativa)

            if ((tentativa-1 == tentativa_limite) or (tentativa+1 == tentativa_limite)):
                tentativa_limite = tentativa

            maior_ou_menor = int(input("Seu numero é maior ou menor? (0 - Menor/ 1 - Maior)"))

            if (maior_ou_menor == 0):
                while (tentativa in tentativas_erradas):
                    tentativa = random.randint(0,tentativa_limite-1)
            else:
                while (tentativa in tentativas_erradas):
                    tentativa = random.randint(tentativa_limite+1, 10)

            resposta = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))
    
            if (resposta == 1):
                print("Acertei!")
