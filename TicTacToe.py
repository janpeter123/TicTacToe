import random 
 
row =  [' ',' ',' ',' ',' ',' ',' ',' ',' ']
playerPlaying = 0
playerChoice = ''
botChoice = ''
possibleRows = []
 
def chooseSymbol():
    global playerChoice
    global botChoice
    playerChoice = (input('Deseja ser X ou O?').upper())
    if(playerChoice=='X'):
        botChoice = 'O'
    else:
        botChoice = 'X'
    print(f'Player is {playerChoice}')
    print(f'Bot is {botChoice}')
 
def display():
    print(row[0:3])
    print(row[3:6])
    print(row[6:9])
    
def fazescolha(matrixPossivel):
    limite = len(matrixPossivel)-1
    return matrixPossivel[round(random.random()*limite)]
    
    
def restart():
    global row
    row =  [' ',' ',' ',' ',' ',' ',' ',' ',' ']  
 
    
#Definindo o Bot
 
def bot():
    global playerPlaying
    global playerChoice
    global botChoice
    global row
    global possibleRows
 
    
    
    availablePositions = []
    
    if(playerPlaying==0):
 
        
        # Looking for available Positions to Play
        for i,item in enumerate(row):
            if(item!=playerChoice and item!=botChoice):
                availablePositions.append(i)
        
 
 
        possibleRows=availablePositions
        #print(possibleRows)
        row[fazescolha(possibleRows)]=str(botChoice)


        
def start():
    restart()
    global playerChoice
    global row
    plaaying = 0
    print('Instruções: Basta escolher o Numero onde quer colocar o simbolo')
    print('  0    1    2\n')
    print(row[0:3],'\n')
    print('  3    4    5\n')
    print(row[3:6],'\n')
    print('  6    7    8\n')
    print(row[6:9],'\n')
    
    chooseSymbol()
    continuar = 0
    while(continuar==0):
        playing = 1
        row[int(input(f'Onde deseja inserir {playerChoice} '))]=str(playerChoice)
        playing = 0
        if(playing==0):
            bot()
        display()
        
        
#row[int(input('Onde vai querer colocar o seu Símbolo?'))] = playerChoice
#display()
start()

