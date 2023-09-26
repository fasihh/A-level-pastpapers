class Balloon:
    # DEC __Health : INTEGER
    # DEC __Colour : STRING
    # DEC __DefenceItem : STRING

    def __init__(self, defenceItem, colour):
        self.__DefenceItem = defenceItem
        self.__Colour = colour
        self.__Health = 100

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, health):
        self.__Health = self.__Health + health

    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False


def Defend(balloon):
    opponentStrength = int(input("Input strength of the balloon opponent: "))

    balloon.ChangeHealth(-opponentStrength)
    print(balloon.GetDefenceItem())

    status = balloon.CheckHealth()
    if status:
        print("No health remaining")
    else:
        print("Health still remaining")

    return balloon


def main():
    defenceItem = input("Input your defence item: ")
    colour = input("Input your colour: ")
    Balloon1 = Balloon(defenceItem, colour)

    Defend(Balloon1)


main()
