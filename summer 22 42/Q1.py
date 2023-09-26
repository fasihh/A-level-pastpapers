#StackData As Array[10] : INTEGER
#StackPointer : INTEGER    
StackData = [0 for x in range(10)]
StackPointer = 0

def outputAll():
    for x in range(10):
        print(StackData[x])
        
def Push(value):
    if StackPointer == len(StackData):
        return False
    else:
        StackData[StackPointer] = value
        StackPointer += 1
        return True
    
def main():
    for i in range(11):
        value = int(input("Input: "))
        if Push(value):
            print("successful")
        else:
            print("overflow")
        
        
    