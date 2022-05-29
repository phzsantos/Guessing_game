import random
import os
import json

def Clear():
    if os.name == 'nt':
        clear = "cls"
    else:
        clear = "clear"

    os.system(clear)
    
def IncrementaMaioresOuMenores(numero, maiores, menores, config):    
    print(maiores)
    print(menores)
    
    if numero >= 5:
        maiores += 1
    else:
        menores += 1
        
    config['Maiores'] = maiores
    config['Menores'] = menores
    
    config_json = json.dumps(config, indent=True)
    
    with open('config.json', 'w+') as file:
        file.write(config_json)

def Game():
    try:
        with open('config.json', 'r') as file:
            config_json = file.read()
            config = json.loads(config_json)
            maiores = config['Maiores']
            menores = config['Menores']
    except IOError:
        config = {'Maiores': 0, 'Menores': 0}
        
        config_json = json.dumps(config, indent=True)
        
        maiores = config['Maiores']
        menores = config['Menores']
        
        with open('config.json', 'x') as file:
            file.write(config_json)
    
    resposta = 0
    tentativas_erradas = []
    menor = 1

    Clear()

    print("1 - Modo padrao 1 a 10")
    print("2 - Modo Personalizado 1 a ?")
    modo = int(input("Como voce quer jogar este game? "))

    Clear()

    if (modo == 1):
        maior = 10
    elif (modo == 2):
        maior = int(input("Qual vai ser o maior numero possivel? "))

        Clear()

        if (maior <= menor):
            resposta = 1
            print("Programa finalizado. So seram permitidos numeros maiores que 1")
    else:
        resposta = 1
        print("Programa finalizado. Essa opcao nao existe.")

    while resposta == 0:
        input(f'Pense em um numero de {menor} a {maior} e depois aperte Enter')
        
        print(maiores)
        print(menores)
        
        if maiores > menores:
            tentativa = random.randint(5,maior)
        elif maiores < menores:
            tentativa = random.randint(menor,5)
        else:
            tentativa = random.randint(menor,maior)
        
        resposta = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))
        
        if resposta == 1:
            print("Acertei!")
            if modo == 1:
                IncrementaMaioresOuMenores(tentativa, maiores, menores, config)
        else:
            while resposta == 0:
                tentativas_erradas.append(tentativa)
                tentativa_anterior = tentativa
                
                if tentativa != menor                    \
                and tentativa != maior                   \
                and tentativa-1 not in tentativas_erradas\
                and tentativa+1 not in tentativas_erradas:
                    maior_ou_menor = int(input("Seu numero é maior ou menor? (0 - Menor/ 1 - Maior): ")) 
                elif tentativa == menor             \
                or tentativa-1 in tentativas_erradas:
                    maior_ou_menor = 1
                else:
                    maior_ou_menor = 0

                if maior_ou_menor == 0:
                    for i in range(tentativa,maior+1):
                        if i not in tentativas_erradas:
                            tentativas_erradas.append(i)

                    while tentativa in tentativas_erradas:
                        tentativa = random.randint(menor,tentativa_anterior-1)
                else:
                    for i in range(tentativa,menor-1,-1):
                        if i not in tentativas_erradas:
                            tentativas_erradas.append(i)

                    while tentativa in tentativas_erradas:
                        tentativa = random.randint(tentativa_anterior+1, maior)
                
                if len(tentativas_erradas) == maior-1:
                    print(f'Então seu numero é {tentativa}!')
                    resposta = 1
                    if modo == 1:
                        IncrementaMaioresOuMenores(tentativa, maiores, menores, config)
                else:
                    resposta = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))
        
                    if resposta == 1:
                        print("Acertei!")
                        
                        if modo == 1:
                            IncrementaMaioresOuMenores(tentativa, maiores, menores, config)

    play_again = int(input("Deseja jogar novamente? (0 - Não / 1 - Sim): "))

    if (play_again):
        Game()
    else:
        Clear()
        print("Nos vemos na proxima ^^")

Game()