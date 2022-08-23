####Libraries####
#import numpy as np
import random as rd
import keyboard as kb

####Define and initialize grid####
grid=[]

def initGrid(width,height):
    global grid
    grid = [[" " for i in range(width)] for a in range(height)]

####Emtpy tile check for apple spawn####
def checkEmptyTiles():
    emptytiles=[]
    for a in range(len(grid)):
        for b in range(len(grid[0])):
            if grid[a][b]==" ":
                emptytiles.append((a,b))
    return emptytiles

####TODO: Check possibleMoves####
def checkPossibleMoves():
    return

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
            elif (a,b)==apple1.position[0]:
                grid[a][b] = "A"
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

####Apple class####
class apple():
    def __init__(self):
        self.position = [(-1,-1)]
    def move(self):
        checkEmptyTiles()
        self.position[0] = checkEmptyTiles()[rd.randint(0,len(checkEmptyTiles())-1)]

####Player class initialization####
class player():
    def __init__(self,initialposition):
        self.position = [initialposition]
        self.lenght = len(self.position)
        self.tailPosition = self.position[-1]
        self.lastdirection = "right"

    def updatePosition(self):
        self.tailPosition = self.position[-1]
        self.lenght = len(self.position)

    def move(self,direction):
        if self.checkApple(direction):
            self.position += [self.tailPosition]
            self.updatePosition()
        self.position = [self.position[0]] + self.position
        self.position.pop(-1)
        if direction == "0":
            self.move(self.lastdirection)
            return
        elif direction =="right":
            tmpx = self.position[0][0]
            tmpy = self.position[0][1]
            self.position.pop(0)
            self.position.insert(0,(tmpx,tmpy+1))
            self.lastdirection = "right"
        elif direction =="left":
            tmpx = self.position[0][0]
            tmpy = self.position[0][1]
            self.position.pop(0)
            self.position.insert(0,(tmpx,tmpy-1))
            self.lastdirection = "left"
        elif direction =="up":
            tmpx = self.position[0][0]
            tmpy = self.position[0][1]
            self.position.pop(0)
            self.position.insert(0,(tmpx-1,tmpy))
            self.lastdirection = "up"
        elif direction =="down":
            tmpx = self.position[0][0]
            tmpy = self.position[0][1]
            self.position.pop(0)
            self.position.insert(0,(tmpx+1,tmpy))
            self.lastdirection = "down"
        self.updatePosition()

    def checkApple(self,direction):
        if direction =="right":
            if (self.position[0][0],self.position[0][1]+1)==apple1.position[0]:
                apple1.move()
                return True
        elif direction =="left":
            if (self.position[0][0],self.position[0][1]-1)==apple1.position[0]:
                apple1.move()
                return True
        elif direction =="up":
            if (self.position[0][0]-1,self.position[0][1])==apple1.position[0]:
                apple1.move()
                return True
        elif direction =="down":
            if (self.position[0][0]+1,self.position[0][1])==apple1.position[0]:
                apple1.move()
                return True

####Tests####
player1 = player((1,1))
apple1 = apple()
initGrid(8,5)
apple1.move()
drawCharacters()
drawGrid()
##
####TODO: Game tick and keyboard inputs####
while True:
    direction = input("\n"*(len(grid)*3)+": ")
    player1.move(direction)
    #print(kb.read_key())
    drawCharacters()
    drawGrid()
