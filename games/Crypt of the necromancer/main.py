##si a cote:
##    joueur - 1pv
##    squelette reste sur case
##si joeur avance contre mur:
##    passe le tour
##tous les 5 tours:
##    squelette de généré

from turtle import Turtle

def print_board(board):
    for i in board:
        print(i)
        print()

def get_board():
    size_x=int(input("Enter the size of x: (4) "))
    size_y=int(input("Enter the size of y: (4) "))
    board=[]
    for x in range(size_x+2):
        line=[]
        for y in range(size_y+2):
            if x==0 or y==0 or x==size_x+1 or y==size_y+1:
                line.append("WALL")
            else:
                line.append(4*" ")
        board.append(line)

    print_board(board)
    return(board)
    
class Point:
    def __init__(self,xcoord=0,ycoord=0):
        self.x=xcoord
        self.y=ycoord

    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy

    def get(self):
        return (self.x,self.y)

    def setx(self,xcoord,ycoord):
        self.x=xcoord
        self.y=ycoord

    def __eq__(ob1,ob2):
        '''use p=Point() then do dir(p)'''
        return ob1.x==ob2.x and ob1.y==ob2.y

    def __repr__(self):
        return "Point("+str(self.x)+","+str(self.y)+")"

class Mob:
    def __init__(self,attack=0,defense=0):
        self.attack=attack
        self.defense=defense

    def adventurer(self):
        print("\u2650")

    def squeleton(self):
        pass

board=get_board()
player=Point(1,1)
squeleton=Point(2,4)
for x in range(len(board)):
    for y in range(len(board[x])):
        if (x,y)== (player.get()):
            board[x][y]="player"
        if (x,y)== (squeleton.get()):
            board[x][y]="squeleton"

print_board(board)
