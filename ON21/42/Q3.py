"""""
myList = [4, 5, 2, 1, 6, 3, 0]


for i in range(1, len(myList)):
    j = i
    while myList[j - 1] > myList[j] and j > 0:
        myList[j - 1], myList[j] = myList[j], myList[j - 1]
        j -= 1

print(myList)


for i in range(len(myList) - 1):
    isSorted = True
    for j in range(1, len(myList)):
        if myList[j - 1] > myList[j]:
            myList[j - 1], myList[j] = myList[j], myList[j - 1]
            isSorted = False

    if isSorted:
        print("sorted")
        break

print(myList)


def BinarySearch(array, upper, lower, value):
    mid = (upper + lower) // 2

    if upper < lower:
        return -1
    elif array[mid] == value:
        return mid
    elif array[mid] > value:
        return BinarySearch(array, mid - 1, lower, value)
    else:
        return BinarySearch(array, upper, mid + 1, value)

print(BinarySearch(myList, len(myList) - 1, 0, 6))


value = 6
upper = len(myList) - 1
lower = 0
found = False

while not found:
    middle = (upper + lower) // 2

    if myList[middle] == value:
        print(middle)
        found = True
    else:
        if upper < lower:
            break
        else:
            if myList[middle] > value:
                upper = middle - 1
            else:
                lower = middle + 1
"""""


class ListNode:
    def __init__(self):
        self.data = ""
        self.ptr = -1


linkedList = []
freePtr = 0
startPtr = 0
null = -1


def InitializeLinkedList():
    for i in range(10):
        linkedList.append(ListNode())
        linkedList[i].ptr = i + 1
    linkedList[i].ptr = -1


def AddIntoList(value):
    global freePtr, startPtr
    if freePtr != null:
        newPtr = freePtr
        linkedList[newPtr].data = value
        freePtr = linkedList[freePtr].ptr

        thisPtr = startPtr
        prevPtr = null

        while thisPtr != null and linkedList[thisPtr].data < value:
            prevPtr = thisPtr
            thisPtr = linkedList[thisPtr].ptr

        if thisPtr == null:
            linkedList[newPtr].ptr = null
            startPtr = newPtr
        else:
            startPtr = newPtr
            linkedList[prevPtr].ptr = newPtr
            linkedList[newPtr].ptr = prevPtr

    else:
        print("overflow")


def ShowList():
    line = ""
    for i in range(len(linkedList)):
        line = str(linkedList[i].ptr) + " " + linkedList[i].data
        print(line)
        line = ""

InitializeLinkedList()
AddIntoList("b")
AddIntoList("a")
ShowList()