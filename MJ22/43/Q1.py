# DEC playerScore[1:11] : INTEGER
# DEC playerName[1:11] : STRING
playerScore = ["" for a in range(11)]
playerName = [0 for b in range(11)]


def ReadHighScore():
    global playerScore, playerName

    playerFile = open("HighScore.txt", "rt")

    for i in range(10):
        name = playerFile.readline()
        score = playerFile.readline()

        playerName[i] = name.strip()
        playerScore[i] = int(score.strip())


def OutputHighScores():
    for i in range(10):
        print(playerName[i], playerScore[i])


def main():
    global playerScore, playerName

    def WriteTopTen():
        try:
            newScoreFile = open("NewHighScore.txt", "x")
        except FileExistsError:
            newScoreFile = open("NewHighScore.txt", "wt")

        for i in range(10):
            name = playerName[i] + "\n"
            score = str(playerScore[i]) + "\n"
            newScoreFile.write(name)
            newScoreFile.write(score)

    def adjustScores(name, score):
        for i in range(10):
            if score > playerScore[i]:
                tempScore = playerScore[i]
                tempName = playerName[i]
                playerScore[i] = score
                playerName[i] = name
                score = tempScore
                name = tempName

    ReadHighScore()
    OutputHighScores()

    userName = input("Input 3 character player name: ")
    while len(userName) != 3:
        userName = input("Input 3 character player name: ")

    userScore = int(input("input player score: "))
    while 1 > userScore < 100000:
        userScore = int(input("input player score: "))

    adjustScores(userName, userScore)

    OutputHighScores()

    WriteTopTen()


main()
