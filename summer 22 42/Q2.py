import random

ArrayData = [[random.randint(1, 100) for j in range(10)] for i in range(10)]

ArrayLength = 10

for x in range(ArrayLength - 1):
    for y in range(ArrayLength - 2):
        for z in range(ArrayLength - y - 2):
            if ArrayData[x][z] > ArrayData[x][z + 1]:
                TempValue = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z + 1]
                ArrayData[x][z + 1] = TempValue
                
for i in range(10):
    line = ""
    for j in range(10):
        line += " " + str(ArrayData[i][j])
    print(line)
    
    
    
