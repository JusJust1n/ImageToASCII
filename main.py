from PIL import Image

print("Select An Option: ")
print("1. Example jpg Image")
print("2. Choose a jpg Image")

im = Image.open("cat.jpeg")

choice = input()
if (choice == 1):
    im = Image.open("cat.jpeg") 
else:
    print("Type the image name with the extention")
    imageName = input()
    im = Image.open(imageName)




width = im.width
height = im.height

if (width > 299 and height > 299):
    im = im.resize((299, 299))
    width = 299
    height = 299
elif (width > 299):
    im = im.resize((299, height))
    width = 299
elif (height > 299):
    im = im.resize((width, 299))
    height = 299

def calcQuotient(index):
    return (index % height)

def calcRemainder(index):
    return (index // height)

def calcBrightness(r, g, b):
    return ((r + g + b) // 3)

def brightnessToASCII(bdata):

    for i in range(width):
        for j in range(height):
            if (bdata[i][j] < 25):
                bdata[i][j] = "   "
            elif (bdata[i][j] >= 25 and bdata[i][j] < 50):
                bdata[i][j] = "..."
            elif (bdata[i][j] >= 50 and bdata[i][j] < 75):
                bdata[i][j] = ":::"
            elif (bdata[i][j] >= 75 and bdata[i][j] < 100):
                bdata[i][j] = "---"
            elif (bdata[i][j] >= 100 and bdata[i][j] < 125):
                bdata[i][j] = "==="
            elif (bdata[i][j] >= 125 and bdata[i][j] < 150):
                bdata[i][j] = "+++"
            elif (bdata[i][j] >= 150 and bdata[i][j] < 175):
                bdata[i][j] = "***"
            elif (bdata[i][j] >= 175 and bdata[i][j] < 200):
                bdata[i][j] = "###"
            elif (bdata[i][j] >= 200 and bdata[i][j] < 225):
                bdata[i][j] = "%%%"
            elif (bdata[i][j] >= 225 and bdata[i][j] <= 255):
                bdata[i][j] = "@@@"
    
_data = list(im.getdata())

# turns _data into a 2D list
data2D = [[None for _ in range(height)] for _ in range(width)]
for i in range(len(_data)):
    data2D[calcRemainder(i)][calcQuotient(i)] = _data[i]

# bdata is brightness data from data2D
bdata = [[None for _ in range(height)] for _ in range(width)]
for i in range(width):
    for j in range(height):
        bdata[i][j] = calcBrightness(data2D[i][j][0], data2D[i][j][1], data2D[i][j][2])

brightnessToASCII(bdata)

for i in range(width):
    print("".join(str(x) for x in bdata[i]))


