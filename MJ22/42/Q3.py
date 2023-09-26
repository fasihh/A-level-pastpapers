class Card:
    def __init__(self, Number, Colour):
        # DEC __Number : INTEGER
        # DEC __Colour : STRING

        self.__Number = Number
        self.__Colour = Colour

    def GetNumber(self):
        return self.__Number

    def SetNumber(self, val):
        self.__Number = val

    def GetColour(self):
        return self.__Colour

    def SetColour(self, val):
        self.__Colour = val


def main():
    # DEC CardArray : Card

    CardArray = [Card(0, ".") for i in range(30)]

    cfile = open("CardValues.txt", "rt")

    for j in range(30):
        number = cfile.readline()
        colour = cfile.readline()
        number.strip()
        colour.strip()

        CardArray[j].SetNumber(number)
        CardArray[j].SetColour(colour)

    #for s in range(30):
    #   print(CardArray[s].GetNumber(), CardArray[s].GetColour(), sep="")

    def ChooseCard():
        choice = int(input("Choose card (1 to 30): "))
        if choice < 1 or choice > 30:
            print("Value outside range")
            ChooseCard()

        return choice - 1

    Player1 = [Card(0, ".") for l in range(4)]

    for p in range(4):
        card = ChooseCard()

        while CardArray[card].GetNumber() == -1:
            card = ChooseCard()

        Player1[p].SetColour(CardArray[card].GetColour())
        Player1[p].SetNumber(CardArray[card].GetNumber())

        CardArray[card].SetNumber(-1)

    for o in range(4):
        print(Player1[o].GetNumber())
        print(Player1[o].GetColour())


main()
