print("meshMaker")

head = input("header: ")
width = int(input("width: "))
height = int(input("height: "))
tileMap = []
for i in range(height):
    tileRow = []
    for j in range(width):
        print("tile",j,i)
        tileId = int(input("tileId: "))
        tileDepth = int(input("depth: "))
        solid = int(input("tile is solid (0,1): "))
        act = int(input("actionGroup: "))
        tileRow.append(tileId + tileDepth*2**16 + solid*2**20 + act*2**21)
    tileMap.append(tileRow)
    
print(head)
print(str(width)+","+str(height))
data = ""
for l in tileMap:
    for k in l:
        data+=str(k)+","
    data = data[:-1]
    data+="\n"
print(data)
