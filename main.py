from PIL import Image

def calcQuotient(index, height):
    return (index % height)

def calcRemainder(index, height):
    return (index // height)

def calcBrightness(r, g, b):
    return ((r + g + b) // 3)

def brightnessToASCII(bdata, width, height, scale):
    for i in range(width):
        for j in range(height):
            if ((bdata[i][j] // 25) == 10):
                bdata[i][j] = 9
            else:
                bdata[i][j] = scale[bdata[i][j] // 25]
    
def main():
    print("This program takes a specified .jpg/.jpeg image and prints it into ASCII characters (zoom out all the way to see the full picture)!")
    print("Select An Option: ")
    print("0. Exit Program")
    print("1. Example jpg Image")
    print("2. Choose a jpg Image")

    im = Image.open("cat.jpeg")

    choice = int(input())
    if (choice == 0):
        exit()
    elif (choice == 1):
        im = Image.open("cat.jpeg") 
    elif (choice == 2):
        print("Type the image name with the extention")
        imageName = input()
        im = Image.open(imageName)

    width = im.width
    height = im.height
    scale = ["   ", "...", ":::", "---", "===", "+++", "***", "###", "%%%", "@@@"]
    
    if (width > 299 and height > 299):
        im = im.resize((299, 299))
        width = 299
        height = 299
    elif (width > 299):
        im = im.resize((299, 299))
        width = 299
        height = 299
    elif (height > 299):
        im = im.resize((299, 299))
        width = 299
        height = 299

    _data = list(im.getdata())

    # turns _data into a 2D list
    data2D = [[None for _ in range(height)] for _ in range(width)]
    for i in range(len(_data)):
        data2D[calcRemainder(i, height)][calcQuotient(i, height)] = _data[i]
    # brightData is brightness data from data2D
    brightData = [[None for _ in range(height)] for _ in range(width)]
    for i in range(width):
        for j in range(height):
            brightData[i][j] = calcBrightness(data2D[i][j][0], data2D[i][j][1], data2D[i][j][2])
    brightnessToASCII(brightData, width, height, scale)
    for i in range(width):
        print("".join(str(x) for x in brightData[i]))

if __name__ == "__main__":
    main()