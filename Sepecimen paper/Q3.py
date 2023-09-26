QueueData = ["" for i in range (20)]
startPointer = -1
endPointer = 0

def Enqueue(item):
    global endPointer
    
    if endPointer == len(QueueData):
        return False
    else:
        QueueData[endPointer] = item
        endPointer += 1
        return True
    

def Remove():
    global startPointer
    if len(QueueData) < 2:
        return "No Items"
    else:
        startPointer = startPointer + 1
        firstItem = QueueData[startPointer]
        
        startPointer = startPointer + 1
        secondItem = QueueData[startPointer]
        
        return firstItem + " " + secondItem


def ReadFile():
    fileName = input("Input a proper file name: ")
    
    try:
        with open(fileName) as file:
            for line in file:
                status = Enqueue(line.strip())
                if not status:
                    return 2
            return 1
    except FileNotFoundError:
        return -1
    
    
def main():    
    fileStatus = ReadFile()           
        
    if fileStatus == -1:
        print("file not found")
    elif fileStatus == 1:
        print("items added")
    else:
        print("not all items added. Queue full")
        
    print(Remove())
        
    
main()