def Unknown(x, y):
    if x < y:
        print(x + y)
        return Unknown(x + 1, y) * 2
    else:
        if x == y:
            return 1
        else:
            print(x + y)
            return Unknown(x - 1, y) // 2


def IterativeUnknown(x, y):
    value = 1
    if x < y:
        for i in range(y - x):
            value = value * 2
        while x != y:
            print(x + y)
            x += 1

        return value
    elif y < x:
        for i in range(x - y):
            value = value // 2
        while x != y:
            print(x + y)
            x -= 1

        return value
    else:
        return 1



def main():
    print("x is 10, y is 15:")
    print(Unknown(10, 15))
    print("x is 10, y is 10:")
    print(Unknown(10, 10))
    print("x is 15, y is 10:")
    print(Unknown(15, 10))
    print("")
    print("x is 10, y is 15:")
    print(IterativeUnknown(10, 15))
    print("x is 10, y is 10:")
    print(IterativeUnknown(10, 10))
    print("x is 15, y is 10:")
    print(IterativeUnknown(15, 10))


main()
