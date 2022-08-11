import random
import os
import json

def clear():
    clear = "cls" if os.name == 'nt' else "clear"
    os.system(clear)
    

def incrementa_maiores_ou_menores(numero, maiores, menores, config):    
    if numero >= 5:
        maiores += 1
    else:
        menores += 1
        
    config['Maiores'] = maiores
    config['Menores'] = menores
    
    config_json = json.dumps(config, indent=True)
    
    with open('config.json', 'w+') as file:
        file.write(config_json)


def pergunta_numero(tentativa):
    try:
        resposta = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))
    except ValueError:
        print("\033[31mERRO:\033[m\nUSE APENAS NUMEROS PARA RESPONDER A PERGUNTA!")
        resposta = pergunta_numero(tentativa)
    
    while resposta != 0 and resposta != 1:
        print("\033[31mERRO:\033[m\nRESPONDA COM APENAS 0 OU 1!")
        resposta = pergunta_numero(tentativa)
            
    return resposta


def pergunta_maior_ou_menor(tentativa):
    try:
        maior_ou_menor = int(input(f"Seu numero é maior ou menor que {tentativa}? (0 - Menor/ 1 - Maior): "))
    except ValueError:
        print("\033[31mERRO:\033[m\nUSE APENAS NUMEROS PARA RESPONDER A PERGUNTA!")
        maior_ou_menor = pergunta_maior_ou_menor(tentativa)
    
    while maior_ou_menor != 0 and maior_ou_menor != 1:
        print("\033[31mERRO:\033[m\nRESPONDA COM APENAS 0 OU 1!")
        maior_ou_menor = pergunta_maior_ou_menor(tentativa)
        
    return maior_ou_menor


def pergunta_maior(menor):
    try:
        maior = int(input("Qual vai ser o maior numero possivel (sendo 1 o menor numero)? "))
    except ValueError:
        print("\033[31mERRO:\033[m\nUSE APENAS NUMEROS PARA RESPONDER A PERGUNTA!")
        maior = pergunta_maior(menor)
    
    while maior <= menor:
        print("\033[31mERRO:\033[m\nSO SERAM PERMITIDOS VALORES MAIORES QUE O PROPRIO 1!")
        maior = pergunta_maior(menor)
    
    return maior


def pergunta_modo():
    try:
        print("1 - Modo padrao 1 a 10")
        print("2 - Modo Personalizado 1 a ?")
        modo = int(input("Como voce quer jogar este game (1 ou 2)? "))
    except ValueError:
        print("\033[31mERRO:\033[m\nUSE APENAS NUMEROS PARA ESCOLHER O MODO DE JOGO")
        modo = pergunta_modo()

    while modo != 1 and modo != 2:
        print("\033[31mERRO:\033[m\nRESPONDA COM APENAS 1 OU 2!")
        modo = pergunta_modo()
    
    return modo


def play_again():
    try:
        play_again = int(input("Deseja jogar novamente? (0 - Não / 1 - Sim): "))
    except ValueError:
        print("\033[31mERRO:\033[m\nUSE APENAS NUMEROS PARA RESPONDER A PERGUNTA!")
        play_again = play_again()
    
    while play_again != 0 and play_again != 1:
        print("\033[31mERRO:\033[m\nRESPONDA COM APENAS 0 OU 1!")
        play_again = play_again()
    
    game() if play_again else clear()

    return 0


def game():
    clear()
    
    try:
        with open('config.json', 'r') as file:
            config_json = file.read()
            config = json.loads(config_json)       
    except IOError:
        config = {'Maiores': 0, 'Menores': 0}
        config_json = json.dumps(config, indent=True)
        
        with open('config.json', 'x') as file:
            file.write(config_json)
    
    menor = 1
    resposta = 0
    tentativas_erradas = []
    maiores = config['Maiores']
    menores = config['Menores']

    modo = pergunta_modo()
    clear()
    
    maior = 10 if modo == 1 else pergunta_maior(menor)

    while not resposta:
        clear()
        input(f'\033[31mPENSE EM UM NUMERO NO INTERVALO DE {menor} E {maior} E DEPOIS APERTE ENTER\033[m')
        
        if maiores > menores and modo == 1:
            tentativa = random.randint(5,maior)
        elif maiores < menores and modo == 1:
            tentativa = random.randint(menor,5)
        else:
            tentativa = random.randint(menor,maior)
        
        resposta = pergunta_numero(tentativa)
        
        if resposta:
            print("Acertei!")
        else:
            while not resposta:
                tentativas_erradas.append(tentativa)
                tentativa_anterior = tentativa
                
                if tentativa != menor                    \
                and tentativa != maior                   \
                and tentativa-1 not in tentativas_erradas\
                and tentativa+1 not in tentativas_erradas:
                    maior_ou_menor = pergunta_maior_ou_menor(tentativa) 
                elif tentativa == menor             \
                or tentativa-1 in tentativas_erradas:
                    maior_ou_menor = 1
                else:
                    maior_ou_menor = 0

                if not maior_ou_menor:
                    [tentativas_erradas.append(i) for i in range(tentativa,maior+1) if i not in tentativas_erradas]

                    while tentativa in tentativas_erradas: tentativa = random.randint(menor,tentativa_anterior-1)
                else:
                    [tentativas_erradas.append(i) for i in range(tentativa,menor-1,-1) if i not in tentativas_erradas]

                    while tentativa in tentativas_erradas: tentativa = random.randint(tentativa_anterior+1, maior)
                
                if len(tentativas_erradas) == maior-1:
                    print(f'Então seu numero é {tentativa}!')
                    resposta = 1
                else:
                    resposta = pergunta_numero(tentativa)
                    if resposta:
                        print("Acertei!")

    if modo == 1:
        incrementa_maiores_ou_menores(tentativa, maiores, menores, config)

    play_again()
