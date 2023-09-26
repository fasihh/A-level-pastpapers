# DEC QueueArray[1:10] : STRING
# DEC headPointer : INTEGER
# DEC tailPointer : INTEGER
# DEC numberOfItems : INTEGER

QueueArray = ["" for i in range(10)]
numberOfItems = 0
headPointer = 0
tailPointer = 0


def Enqueue(DataToAdd):
    global numberOfItems, tailPointer, QueueArray

    if numberOfItems == 10:
        return False

    QueueArray[tailPointer] = DataToAdd

    if tailPointer >= 9:
        tailPointer = 0
    else:
        tailPointer = tailPointer + 1

    numberOfItems = numberOfItems + 1

    return True


def Dequeue():
    global numberOfItems, headPointer, QueueArray

    if numberOfItems == 0:
        return False

    value = QueueArray[headPointer]

    if headPointer >= 9:
        headPointer = 0
    else:
        headPointer = headPointer + 1

    numberOfItems = numberOfItems - 1

    return value


def main():
    for i in range(11):
        value = input("Input value: ")
        status = Enqueue(value)

        if status:
            print("value added")
        else:
            print("overflow")

    print(QueueArray)

    for i in range(2):
        delValue = Dequeue()
        print(delValue)


main()
