# import turtle

# screen = turtle.Screen()
# screen.setup(800,800)
# screen.title("jogo da velha")
# screen.setworldcoordinates(-5,-5,5,5)
# screen.tracer(0,0) #para não mostrar cada fase dos desenhos


# def tabuleiro():
#     turtle.pencolor('black')
#     turtle.pensize(5)
#     turtle.up()
#     turtle.goto(-3,-1)
#     turtle.seth(0)
#     turtle.down()
#     turtle.fd(6)
#     turtle.up()
#     turtle.goto(-3,1)
#     turtle.seth(0)
#     turtle.down()
#     turtle.fd(6)
#     turtle.up()
#     turtle.goto(-1,-3)
#     turtle.seth(90)
#     turtle.down()
#     turtle.fd(6)
#     turtle.up()
#     turtle.goto(1,-3)
#     turtle.seth(90)
#     turtle.down()
#     turtle.fd(6)

# def des_circ(x,y):
#     turtle.up()
#     turtle.goto(x,y-0.80)
#     turtle.seth(0)
#     turtle.color('blue')
#     turtle.down()
#     turtle.circle(0.80, steps=90)

# def des_x(x,y):
#     turtle.color('red')
#     turtle.up()
#     turtle.goto(x-0.75,y-0.75)
#     turtle.down()
#     turtle.goto(x+0.75,y+0.75)
#     turtle.up()
#     turtle.goto(x-0.75,y+0.75)
#     turtle.down()
#     turtle.goto(x+0.75,y-0.75)
    
# def verif(i,j,p):
#     if p==0: return
#     x,y = 2*(j-1), -2*(i-1) 
#     if p==1: 
#         des_x(x,y)
#     else: 
#         des_circ(x,y)
    
# def desen(b): 
#     tabuleiro()
#     for _ in range(3):
#         for x in range(3):
#             verif(_,x,b[_][x]) 
#     screen.update()

# def play(x, y):
#     global turn
#     i = 3 - int(y + 5) // 2
#     j = int(x + 5) // 2 - 1
#     if not (0 <= i < 3 and 0 <= j < 3 and b[i][j] == 0):
#         return
#     player = 1 if turn == 'x' else 2   
#     turn = 'o' if turn == 'x' else 'x'
#     b[i][j] = player
#     desen(b)
    
# b = [ [ 0,0,0 ], [ 0,0,0 ], [ 0,0,0 ] ]    
# desen(b)
# turn = 'circle'

# screen.onclick(play)
# turtle.mainloop()

from turtle import Turtle, onscreenclick

leo = Turtle()
raio = 80 / 2
X = 1
O = 2
espaco = 0
ocupado = ['','','','','','','','','']
posicaoAtual = 0



def configurar_tela():
    leo.pensize(5)
    leo.penup()
    leo.backward(150)
    leo.pendown()
    leo.forward(300)
    leo.left(90)
    leo.penup()
    leo.forward(100)
    leo.pendown()
    leo.left(90)
    leo.forward(300)
    leo.backward(100)
    leo.left(90)
    leo.backward(100)
    leo.forward(300)
    leo.penup()
    leo.left(90)
    leo.forward(100)
    leo.left(90)
    leo.pendown()
    leo.forward(300)
    leo.right(90)

def goto_and_mark(x, y):
    global posicaoAtual

    leo.penup()
    tr = ((x - 150) // 100) * 100 + 200, (y // 100) * 100 + 50
    posicaoAtual = getPosicao(tr)
    leo.goto(tr)
    leo.pendown()

def desenhe_circulo(x, y):
    leo.color("blue")
    leo.speed(0)
    leo.pensize(10)
    leo.penup()
    x = leo.xcor()
    y = leo.ycor() - raio
    leo.goto(x, y)
    leo.pendown()
    leo.circle(raio)

def desenhe_x(i, j):
    leo.color("red")
    leo.speed(0)
    leo.pensize(20)
    leo.penup()
    x = j * 100 - 150 + 50  # Ajuste para centralizar o "X" na célula
    y = i * 100 - 150 + 50 + 50 # Ajuste para centralizar o "X" na célula
    leo.goto(x, y)
    leo.pendown()
    leo.setheading(45)
    leo.forward(45)
    leo.backward(90)
    leo.forward(45)
    leo.left(90)
    leo.forward(45)
    leo.backward(90)
    leo.forward(45)
    leo.right(135)

def getPosicao(tr):
    ''' 
    POSIÇÕES:
    1 / 2 / 3
    4 / 5 / 6
    7 / 8 / 9
    '''
    if tr == (-100.0, 150.0):
        posicao = 1
    elif tr == (0.0, 150.0):
        posicao = 2
    elif tr == (100.0, 150.0):
        posicao = 3
    elif tr == (-100.0, 50.0):
        posicao = 4
    elif tr == (0.0, 50.0):
        posicao = 5
    elif tr == (100.0, 50.0):
        posicao = 6
    elif tr == (-100.0, -50.0):
        posicao = 7
    elif tr == (0.0, -50.0):
        posicao = 8
    elif tr == (100.0, -50.0):
        posicao = 9
    
    return posicao

def alternar(x, y):
    global espaco, ocupado, posicaoAtual
    
    if -150 <= x <= 150 and -100 <= y <= 200:
        i = int((y + 100) // 100)  # Calcular a linha
        j = int((x + 150) // 100)  # Calcular a coluna

        goto_and_mark(x, y) #A partir daqui, a posição atual é atualizada

        if espaco == X:
            desenhe_x(i, j)
            espaco = O
            ocupado[posicaoAtual-1] = 'X'
        else:
            desenhe_circulo(i, j)
            espaco = X
            ocupado[posicaoAtual-1] = 'O'
    
    checar_vitoria()

def checar_vitoria():
    global ocupado
    if [ocupado[0], ocupado[1], ocupado[2]] == ['O','O','O'] or [ocupado[0], ocupado[1], ocupado[2]] == ['X','X','X']:
        #DESENHAR LINHA
        leo.color("green")
        leo.penup()
        leo.goto(-150, 150)
        leo.pendown()
        leo.goto(150, 150)

    elif [ocupado[3], ocupado[4], ocupado[5]] == ['O','O','O'] or [ocupado[3], ocupado[4], ocupado[5]] == ['X','X','X']:
        #DESENHAR LINHA
        leo.color("green")
        leo.penup()
        leo.goto(-150, 50)
        leo.pendown()
        leo.goto(150, 50)

    elif [ocupado[6], ocupado[7], ocupado[8]] == ['O','O','O'] or [ocupado[6], ocupado[7], ocupado[8]] == ['X','X','X']:
        #DESENHAR LINHA
        leo.color("green")
        leo.penup()
        leo.goto(-150, -50)
        leo.pendown()
        leo.goto(150, -50)

    elif [ocupado[0], ocupado[3], ocupado[6]] == ['O','O','O'] or [ocupado[0], ocupado[3], ocupado[6]] == ['X','X','X']:
        #DESENHAR LINHA
        leo.color("green")
        leo.penup()
        leo.goto(-100, 200)
        leo.pendown()
        leo.goto(-100, -100)

    elif [ocupado[1], ocupado[4], ocupado[7]] == ['O','O','O'] or [ocupado[1], ocupado[4], ocupado[7]] == ['X','X','X']:
        #DESENHAR LINHA
        leo.color("green")
        leo.penup()
        leo.goto(0, 200)
        leo.pendown()
        leo.goto(0, -100)

    elif [ocupado[2], ocupado[5], ocupado[8]] == ['O','O','O'] or [ocupado[2], ocupado[5], ocupado[8]] == ['X','X','X']:
        #DESENHAR LINHA
        leo.color("green")
        leo.penup()
        leo.goto(100, 200)
        leo.pendown()
        leo.goto(100, -100)

    elif [ocupado[0], ocupado[4], ocupado[8]] == ['O','O','O'] or [ocupado[0], ocupado[4], ocupado[8]] == ['X','X','X']:
        #DESENHAR LINHA
        leo.color("green")
        leo.penup()
        leo.goto(-125, 175)
        leo.pendown()
        leo.goto(125, -75)

    elif [ocupado[6], ocupado[4], ocupado[2]] == ['O','O','O'] or [ocupado[6], ocupado[4], ocupado[2]] == ['X','X','X']:
        #DESENHAR LINHA
        leo.color("green")
        leo.penup()
        leo.goto(125, 175)
        leo.pendown()
        leo.goto(-125, -75)


onscreenclick(alternar)

configurar_tela()

leo.screen.mainloop() 