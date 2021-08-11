from PIL import Image

im = Image.open("cat.jpeg") 
width = im.width
height = im.height

if (width > 300 and height > 300):
    im = im.resize((300, 300))
    width = 300
    height = 300
elif (width > 300):
    im = im.resize((300, height))
    width = 300
elif (height > 300):
    im = im.resize((width, 300))
    height = 300

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
                bdata[i][j] = "  "
            elif (bdata[i][j] >= 25 and bdata[i][j] < 50):
                bdata[i][j] = ".."
            elif (bdata[i][j] >= 50 and bdata[i][j] < 75):
                bdata[i][j] = "::"
            elif (bdata[i][j] >= 75 and bdata[i][j] < 100):
                bdata[i][j] = "--"
            elif (bdata[i][j] >= 100 and bdata[i][j] < 125):
                bdata[i][j] = "=="
            elif (bdata[i][j] >= 125 and bdata[i][j] < 150):
                bdata[i][j] = "++"
            elif (bdata[i][j] >= 150 and bdata[i][j] < 175):
                bdata[i][j] = "**"
            elif (bdata[i][j] >= 175 and bdata[i][j] < 200):
                bdata[i][j] = "##"
            elif (bdata[i][j] >= 200 and bdata[i][j] < 225):
                bdata[i][j] = "%%"
            elif (bdata[i][j] >= 225 and bdata[i][j] <= 255):
                bdata[i][j] = "@@"
    

# gets data from image into a list
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
    #print(*bdata[i], sep='')
    # for j in range(height):
    #     print(bdata[i][j])
    print("".join(str(x) for x in bdata[i]))
    #     #print(bdata, end= "")

# to DO: 
# assign ascii chars to the brightness value and modify the bdata list from that
# print bdata without brackets or commas in the terminal.  if image is too big do ctrl - to zoom out, ctrl + to zoom in
# print(bdata[689]) 69, 63 ascii, 4 for each, some left over


# print(data2D[689]) the last one

#print(len(_data))

#im.show()
