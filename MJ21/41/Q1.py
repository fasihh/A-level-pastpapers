
def main():
    class node:
        def __init__(self, Data, NextNode):
            self.data = Data
            self.nextNode = NextNode


    linkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]
    startPointer = 0
    emptyList = 5

    outputNodes(linkedList, startPointer)
    value = int(input())
    status, emptyList = addNode(linkedList, startPointer, emptyList, value)
    print()
    outputNodes(linkedList, startPointer)


def outputNodes(array, startPtr):
    while startPtr != -1:
        print(array[startPtr].data)
        startPtr = array[startPtr].nextNode


def addNode(linkedlist, startptr, emptylist, value):
    if emptylist != -1:
        linkedlist[emptylist].data = value
        newNode = emptylist
        emptylist = linkedlist[emptylist].nextNode

        thisNode = startptr
        while thisNode != -1:
            prevNode = thisNode
            thisNode = linkedlist[thisNode].nextNode
            if thisNode == -1:
                linkedlist[prevNode].nextNode = newNode

        linkedlist[newNode].nextNode = -1

        return True, emptylist
    else:
        return False, emptylist


main()