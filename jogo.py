import random
def jogo():
    numero_secreto = random.randint(1,20)
    tentativas_max = 5

    for tentativas in range(tentativas_max):
        palpite = int(input("insira seu palpite"))
        if palpite == numero_secreto :                                              
            print("acertou")
            break
        elif palpite < numero_secreto:
            print("um pouco maior")
        else :
            print('um pouco menor')    
    else : 
        print("você perdeu, o numero era:" + str(numero_secreto))
jogo()