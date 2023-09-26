class HiddenBox:
    # __BoxName : STRING
    # __Creator : STRING
    # __DateHidden : STRING
    # __GameLocation : STRING
    # __LastFinds[10][2] : STRING
    # __Active : BOOLEAN
    
    def __init__(self, boxname, creator, datehidden, gamelocation):
        self.__BoxName = boxname
        self.__Creator = creator
        self.__DateHidden = datehidden
        self.__GameLocation = gamelocation
        
        self.__Active = False
        
        self.__LastFinds = [["" for i in range(2)] for i in range(10)]
        
    def GetBoxName(self):
        return self.__BoxName

    def GetGameLocation(self):
        return self.__GameLocation
    

class PuzzleBox(HiddenBox):
    # __PuzzleText : STRING
    # __Solution : STRING
    
    def __init__(self, boxname, creator, datehidden, gamelocation, puzzletext, solution):
        super().__init__(boxname, creator, datehidden, gamelocation)
        self.__PuzzleText = puzzletext
        self.__Solution = solution
        

def NewBox(theBoxes, NewBoxes):
    name = input("Name: ")
    creator = input("Creator: ")
    dateHidden = input("Date hidden: ")
    gameLocation = input("Game location: ")
    boxObj = HiddenBox(name, creator, dateHidden, gameLocation)
    theBoxes[NewBoxes] = boxObj
    return NewBoxes + 1
           
           
def main():
    TheBoxes = [HiddenBox("", "", "", "") for i in range(10000)]
    
    NewBoxes = 0
    NewBoxes = NewBox(TheBoxes, NewBoxes)
    
    
main()


