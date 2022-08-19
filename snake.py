####Libraries####
#import numpy as np

####Define and initialize grid####
grid=[]

def initGrid(width,height):
    global grid
    grid = [["" for i in range(width)] for a in range(height)]

####Emtpy tile check for apple spawn####
def checkEmptyTiles():
    emptytiles=[]
    for a in range(len(grid)):
        for b in range(len(grid[0])):
            if grid[a][b]==" ":
                emptytiles.append((a,b))
    return emptytiles

####Draw the character tiles####
def drawCharacters():
    global grid
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            if (a,b) in player1.position:
                if (a,b)==player1.position[0]:
                    grid[a][b] = "H"
                else:
                    grid[a][b] = "B"
            else:
                grid[a][b] = " "

####Draw grid to the screen####
def drawGrid():
    case = "  "
    for i in range(len(grid)):
        for a in range(len(grid[i])):
            if a==(len(grid[i])-1):
                if i == (len(grid)-1):
                    case = case+str(grid[i][a])
                else:
                    case = case+str(grid[i][a])+"\n" +"——————"*len(grid[0]) + "\n  "
            else:
                case = case+str(grid[i][a])+"  |  "
    print(case)

####TODO: Apple class####
class apple():
    def __init__(self):
        #self.position =
        return

####Player class initialization####
class player():
    def __init__(self,initialposition):
        self.position = [initialposition]
        self.lenght = len(self.position)
        self.tailPosition = self.position[-1]

    def updatePosition(self):
        self.tailPosition = self.position[-1]
        self.lenght = len(self.position)

    def move(self,direction,willgrow):
        if willgrow:
            self.position += [self.tailPosition]
            self.updatePosition()
        self.position = [self.position[0]] + self.position
        self.position.pop(-1)
        if direction =="right":
            tmpx = self.position[0][0]
            tmpy = self.position[0][1]
            self.position.pop(0)
            self.position.insert(0,(tmpx,tmpy+1))
        elif direction =="left":
            tmpx = self.position[0][0]
            tmpy = self.position[0][1]
            self.position.pop(0)
            self.position.insert(0,(tmpx,tmpy-1))
        elif direction =="up":
            tmpx = self.position[0][0]
            tmpy = self.position[0][1]
            self.position.pop(0)
            self.position.insert(0,(tmpx-1,tmpy))
        elif direction =="down":
            tmpx = self.position[0][0]
            tmpy = self.position[0][1]
            self.position.pop(0)
            self.position.insert(0,(tmpx+1,tmpy))
        self.updatePosition()

####Tests####
player1 = player((1,1))
initGrid(8,5)
drawCharacters()
drawGrid()
##
#player1.grow()
player1.move("right",True)
drawCharacters()
drawGrid()
##
player1.move("right",False)
drawCharacters()
drawGrid()
##
player1.move("right",True)
drawCharacters()
drawGrid()
##
player1.move("down",True)
drawCharacters()
drawGrid()
##
player1.move("down",False)
drawCharacters()
drawGrid()
##
print(checkEmptyTiles())
