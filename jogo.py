import turtle

screen = turtle.Screen()
screen.setup(800,800)
screen.title("jogo da velha")
screen.setworldcoordinates(-5,-5,5,5)
screen.tracer(0,0) #para não mostrar cada fase dos desenhos


def tabuleiro():
    turtle.pencolor('black')
    turtle.pensize(5)
    turtle.up()
    turtle.goto(-3,-1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-3,1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-1,-3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(1,-3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)

def des_circ(x,y):
    turtle.up()
    turtle.goto(x,y-0.80)
    turtle.seth(0)
    turtle.color('blue')
    turtle.down()
    turtle.circle(0.80, steps=90)

def des_x(x,y):
    turtle.color('red')
    turtle.up()
    turtle.goto(x-0.75,y-0.75)
    turtle.down()
    turtle.goto(x+0.75,y+0.75)
    turtle.up()
    turtle.goto(x-0.75,y+0.75)
    turtle.down()
    turtle.goto(x+0.75,y-0.75)
    
def verif(i,j,p):
    if p==0: return
    x,y = 2*(j-1), -2*(i-1) 
    if p==1: 
        des_x(x,y)
    else: 
        des_circ(x,y)
    
def desen(b): 
    tabuleiro()
    for _ in range(3):
        for x in range(3):
            verif(_,x,b[_][x]) 
    screen.update()

def play(x, y):
    global turn
    i = 3 - int(y + 5) // 2
    j = int(x + 5) // 2 - 1
    if not (0 <= i < 3 and 0 <= j < 3 and b[i][j] == 0):
        return
    player = 1 if turn == 'x' else 2
    turn = 'o' if turn == 'x' else 'x'
    b[i][j] = player
    desen(b)
    
b = [ [ 0,0,0 ], [ 0,0,0 ], [ 0,0,0 ] ]    
desen(b)
turn = 'circle'

screen.onclick(play)
turtle.mainloop()