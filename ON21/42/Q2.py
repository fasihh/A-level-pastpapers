class Picture:
    def __init__(self, description, width, height, frameColour):
        # DEC __Description : STRING
        # DEC __Width : INTEGER
        # DEC __Height : INTEGER
        # DEC __FrameColour : STRING
        self.__Description = description
        self.__Width = width
        self.__Height = height
        self.__FrameColour = frameColour

    def GetDescription(self):
        return self.__Description

    def GetWidth(self):
        return self.__Width

    def GetHeight(self):
        return self.__Height

    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self, newDescription):
        self.__Description = newDescription


# DEC PictureArray[1:100] : Picture
PictureArray = [Picture for i in range(100)]


def ReadData():
    try:
        pictureFile = open("Pictures.txt", "rt")
    except FileNotFoundError:
        print("File not found")

    count = 0

    for i in range(100):
        description = pictureFile.readline().lower()
        width = pictureFile.readline()
        height = pictureFile.readline()
        frameColour = pictureFile.readline()

        pictureElement = Picture(description.strip(), width.strip(), height.strip(), frameColour.strip())

        PictureArray[i] = pictureElement

        if description != "":
            count += 1

    print(count)


def main():
    ReadData()

    requirement = input("Input your requirements: ").split(sep=", ")

    for i in range(len(PictureArray)):
        if PictureArray[i].GetColour() == requirement[0].lower() and \
                PictureArray[i].GetWidth() == requirement[1] and \
                PictureArray[i].GetHeight() == requirement[2]:
            print(PictureArray[i].GetDescription())


main()


