TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]
firstElement = 0


def InsertionSort(TheData):
    for count in range(firstElement, 9):
        DataToInsert = TheData[count]
        Inserted = 0
        NextValue = count - 1
        
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1
                
def OutputArray(TheData):
    for element in TheData:
        print(element)
        

def searchInput(TheData):
    number = int(input("Enter a number: "))
    
    for element in TheData:
        if element == number:
            print("found")
            return True
        else:
            print("not found")
            return False 
        

def main():
    print("Unsorted data:\n")
    OutputArray(TheData)
    InsertionSort(TheData)
    print("\nSorted data:\n")
    OutputArray(TheData)
    
    searchInput(TheData)
    
    
main()
