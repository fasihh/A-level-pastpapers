class Node:
    def __init__(self, Pointer, Data) -> None:
        self.pointer = Pointer
        self.data = Data
        

linkedList = [Node(0, 0) for i in range(10)]
for j in range(len(linkedList)):
    linkedList[j].pointer = j + 1
linkedList[len(linkedList) - 1].pointer = -1

freeNode = 0
startNode = -1

def AddItem(value):
    global freeNode, startNode
    
    if freeNode == -1:
        return False
    else:
        newNode = freeNode
        linkedList[newNode].data = value
        freeNode = linkedList[newNode].pointer
        
        currentNode = startNode
        while currentNode != -1 and linkedList[currentNode].data < value:
            previousNode = currentNode
            currentNode = linkedList[currentNode].pointer
            
        if startNode == currentNode:
            linkedList[newNode].pointer = startNode 
            startNode = newNode
        else:
            linkedList[newNode].pointer = linkedList[previousNode].pointer
            linkedList[previousNode].pointer = newNode
        
        return True

for element in linkedList:
    print(element.data, element.pointer)

AddItem(5)
AddItem(2)
AddItem(9)
AddItem(6)
AddItem(1)

print()
for element in linkedList:
    print(element.data, element.pointer)
print(startNode)
