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
    if numero >= 5:
        maiores += 1
    else:
        menores += 1
        
    config['Maiores'] = maiores
    config['Menores'] = menores
    
    config_json = json.dumps(config, indent=True)
    
    with open('config.json', 'w+') as file:
        file.write(config_json)

def PerguntaNumero(tentativa):
    try:
        resposta = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))
    except ValueError:
        print("\033[31mERRO:\033[m\nUSE APENAS NUMEROS PARA RESPONDER A PERGUNTA!")
        resposta = int(input(f'Seu numero e {tentativa}? (0 - Não / 1 - Sim): '))
    
    while resposta != 0 and resposta != 1:
        print("\033[31mERRO:\033[m\nRESPONDA COM APENAS 0 OU 1!")
        resposta = PerguntaNumero()
            
    return resposta

def PerguntaMaiorOuMenor(tentativa):
    try:
        maior_ou_menor = int(input(f"Seu numero é maior ou menor que {tentativa}? (0 - Menor/ 1 - Maior): "))
    except ValueError:
        print("\033[31mERRO:\033[m\nUSE APENAS NUMEROS PARA RESPONDER A PERGUNTA!")
        maior_ou_menor = int(input(f"Seu numero é maior ou menor que {tentativa}? (0 - Menor/ 1 - Maior): "))
    
    while maior_ou_menor != 0 and maior_ou_menor != 1:
        print("\033[31mERRO:\033[m\nRESPONDA COM APENAS 0 OU 1!")
        maior_ou_menor = PerguntaMaiorOuMenor()
        
    return maior_ou_menor

def PerguntaMaior(menor):
    try:
        maior = int(input("Qual vai ser o maior numero possivel (sendo 1 o menor numero)? "))
    except ValueError:
        print("\033[31mERRO:\033[m\nUSE APENAS NUMEROS PARA RESPONDER A PERGUNTA!")
        maior = int(input("Qual vai ser o maior numero possivel (sendo 1 o menor numero)? "))
    
    while maior <= menor:
        print("\033[31mERRO:\033[m\nSO SERAM PERMITIDOS VALORES MAIORES QUE O PROPRIO 1!")
        maior = PerguntaMaior(menor)
    
    return maior

def PerguntaModo():
    try:
        print("1 - Modo padrao 1 a 10")
        print("2 - Modo Personalizado 1 a ?")
        modo = int(input("Como voce quer jogar este game (1 ou 2)? "))
    except ValueError:
        print("\033[31mERRO:\033[m\nUSE APENAS NUMEROS PARA ESCOLHER O MODO DE JOGO")
        modo = int(input("Como voce quer jogar este game (1 ou 2)? "))

    while modo != 1 and modo != 2:
        print("\033[31mERRO:\033[m\nRESPONDA COM APENAS 1 OU 2!")
        modo = PerguntaModo()
    
    Clear()
    
    return modo

def PlayAgain():
    try:
        play_again = int(input("Deseja jogar novamente? (0 - Não / 1 - Sim): "))
    except ValueError:
        print("\033[31mERRO:\033[m\nUSE APENAS NUMEROS PARA RESPONDER A PERGUNTA!")
        play_again = int(input("Deseja jogar novamente? (0 - Não / 1 - Sim): "))
    
    while play_again != 0 and play_again != 1:
        print("\033[31mERRO:\033[m\nRESPONDA COM APENAS 0 OU 1!")
        play_again = PlayAgain()
    
    if play_again:
        Game()
    else:
        Clear()
        print("Nos vemos na proxima ^^")
        
    return 0

def Game():
    Clear()
    
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

    modo = PerguntaModo()

    if modo == 1:
        maior = 10
    else:
        maior = PerguntaMaior(menor)

    while resposta == 0:
        Clear()
        input(f'\033[31mPENSE EM UM NUMERO NO INTERVALO DE {menor} E {maior} E DEPOIS APERTE ENTER\033[m')
        
        if maiores > menores and modo == 1:
            tentativa = random.randint(5,maior)
        elif maiores < menores and modo == 1:
            tentativa = random.randint(menor,5)
        else:
            tentativa = random.randint(menor,maior)
        
        resposta = PerguntaNumero(tentativa)
        
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
                    maior_ou_menor = PerguntaMaiorOuMenor(tentativa) 
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
                    resposta = PerguntaNumero(tentativa)
        
                    if resposta == 1:
                        print("Acertei!")
                        
                        if modo == 1:
                            IncrementaMaioresOuMenores(tentativa, maiores, menores, config)

    PlayAgain()

Game()
