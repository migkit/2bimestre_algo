import time

ligado = False 
tempo = 0
temperatura = 0



def ligar(novo_tempo, nova_temperatura):
    global tempo, temperatura, ligado
    if not ligado:
        ligado = True
        tempo = novo_tempo
        potencia = nova_temperatura
        
        print(f"Lava-louças ligado por {tempo} segundos na temperatura {potencia}")
        iniciar_cronometro(tempo)
        desligar() #desligar automaticamente

    else: 
        print("Lava-louças já está ligado")

def desligar():
    global ligado
    if ligado:
        ligado = False
        print("Lava-louças esta desligado")

    else:
        print("Lava-louças já está desligado")

def status():
    if ligado:
        print(f"tempo: {tempo} segundos \n temperatura: {temperatura}")

    else:       
        print("Lava-louças está desligada")  

def iniciar_cronometro(segundos):
    while segundos>0:
        print(f"tempo restante:{segundos} segundos", end = "\r")
        time.sleep(1)
        segundos -= 1 #segundos = segundos -1 
    print("\n tempo esgotado")

escolha= input("qual modo deseja usar? \n 1 - modo vidro \n 2 - modo plastico \n 3 - modo metal \n coloque a função que deseja usar: ")

def vidro():
    ligar(120,100)

def plastico():
    ligar(60,21)

def metal():
    ligar(120,30)

if escolha == "1":
    vidro()

elif escolha == "2":
    plastico()

elif escolha == "3":
    metal()
