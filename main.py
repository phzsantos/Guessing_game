import random

resposta = 0
tentativas_erradas = []

while (resposta == 0):
    input('Pense em um numero de 1 a 10 e depois aperte Enter')

    tentativa = random.randint(1,10)

    resposta = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))
    
    if (resposta == 1):
        print("Acertei!")
    else:
        while (resposta == 0):
            tentativas_erradas.append(tentativa)
            tentativa_anterior = tentativa
                
            maior_ou_menor = int(input("Seu numero é maior ou menor? (0 - Menor/ 1 - Maior): "))

            if (maior_ou_menor == 0):
                for i in range(tentativa,11):
                    if (i not in tentativas_erradas):
                        tentativas_erradas.append(i)

                while (tentativa in tentativas_erradas):
                    tentativa = random.randint(1,tentativa_anterior-1)
            else:
                for i in range(tentativa,0,-1):
                    if (i not in tentativas_erradas):
                        tentativas_erradas.append(i)

                while (tentativa in tentativas_erradas):
                    tentativa = random.randint(tentativa_anterior+1, 10)

            resposta = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))
    
            if (resposta == 1):
                print("Acertei!")
