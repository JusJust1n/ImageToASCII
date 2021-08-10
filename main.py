from PIL import Image

im = Image.open("ImageToASCII/cat.jpeg")
width = im.width
height = im.height

def calcQuotient(index):
    return (index % width)

def calcRemainder(index):
    return (index // width)

def calcBrightness(r, g, b):
    return ((r + g + b) // 3)

# gets data from image into a list
_data = list(im.getdata())

# turns _data into a 2D list
data2D = [[None for _ in range(height)] for _ in range(width)]
for i in range(len(_data)):
    data2D[calcQuotient(i)][calcRemainder(i)] = _data[i]

# bdata is brightness data from data2D
bdata = [[None for _ in range(height)] for _ in range(width)]
for i in range(width):
    for j in range(height):
        bdata[i][j] = calcBrightness(data2D[i][j][0], data2D[i][j][1], data2D[i][j][2])


# to DO: 
# assign ascii chars to the brightness value and modify the bdata list from that
# print bdata without brackets or commas in the terminal.  if image is too big do ctrl - to zoom out, ctrl + to zoom in
# print(bdata[689]) 69, 63 ascii, 4 for each, some left over


# print(data2D[689]) the last one

print(len(_data))

im.show()
