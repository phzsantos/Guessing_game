import random

resposta = 0
tentativas_erradas = []
maior = 10
menor = 1

while (resposta == 0):
    input('Pense em um numero de 1 a 10 e depois aperte Enter')

    tentativa = random.randint(menor,maior)
    
    resposta = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))
    
    if (resposta == 1):
        print("Acertei!")
    else:
        while (resposta == 0):
            tentativas_erradas.append(tentativa)
            tentativa_anterior = tentativa
            
            if ((tentativa != menor) and (tentativa != maior) and (tentativa-1 not in tentativas_erradas) and  (tentativa+1 not in tentativas_erradas)):
                maior_ou_menor = int(input("Seu numero é maior ou menor? (0 - Menor/ 1 - Maior): ")) 
            elif ((tentativa == menor) or (tentativa-1 in tentativas_erradas)):
                maior_ou_menor = 1
            else:
                maior_ou_menor = 0

            if (maior_ou_menor == 0):
                for i in range(tentativa,maior+1):
                    if (i not in tentativas_erradas):
                        tentativas_erradas.append(i)

                while (tentativa in tentativas_erradas):
                    tentativa = random.randint(menor,tentativa_anterior-1)
            else:
                for i in range(tentativa,menor-1,-1):
                    if (i not in tentativas_erradas):
                        tentativas_erradas.append(i)

                while (tentativa in tentativas_erradas):
                    tentativa = random.randint(tentativa_anterior+1, maior)
            
            if (len(tentativas_erradas) == maior-1):
                print(f'Então seu numero é {tentativa}!')
                resposta = 1
            else:
                resposta = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))
    
                if (resposta == 1):
                    print("Acertei!")
