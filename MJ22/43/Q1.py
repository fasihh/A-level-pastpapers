players = [["", 0] for i in range(11)]


def ReadHighScores():
    with open("Highscore.txt") as f:
        i = 0
        for l in f:
            players[i] = [l.strip(), int(next(f).strip())]
            i += 1
            
def OutputHighScores():
    for i in range(10):
        print(players[i][0], players[i][1])
        
def Procedure(name, score):
    players[10] = [name, score]
    
    for i in range(len(players)):
        j = i
        while players[j - 1][1] < players[j][1] and j > 0:
             players[j - 1], players[j] = players[j], players[j - 1]
             j -= 1
             
def WriteTopTen():
    with open("NewHighScore.txt", "w") as f:
        for i in range(9):
            f.write(f"{players[i][0]}\n{players[i][1]}\n")
        f.write(f"{players[i][0]}\n{players[i][1]}")
         
def main():  
    ReadHighScores()
    OutputHighScores()
    print()
    
    while True:
        name = input("Enter player name: ")
        
        if len(name) == 3:
            break
        
    while True: 
        score = int(input("Enter player score: "))
        
        if score <= 100000 or score > 0:
            break
        
    Procedure(name, score)
    
    print()
    OutputHighScores()
    WriteTopTen()
        
        
main()
