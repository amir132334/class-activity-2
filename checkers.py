import turtle


PIXEL_SIZE = 30 

ROWS = 20

COLUMNS = 20

win = turtle.Screen()
win.title(" chess board ")
win.bgcolor("white")


pencil = turtle.Turtle()
def initialization():

    pencil.speed(0)
    pencil.shape("square")
    pencil.pencolor("black")
    pencil.pensize(1)
    pencil.up()
    
    x_top_left = - PIXEL_SIZE * COLUMNS/2 
    y_top_left = PIXEL_SIZE * ROWS/2 


    pencil.goto(x_top_left, y_top_left)





def draw_pixel(color="black"):
    pencil.down()
    pencil.begin_fill()
    pencil.fillcolor(color)
    counter = 1

    while counter<= 4 :
        pencil.fd(PIXEL_SIZE)
        pencil.right(90)
        counter = counter +1

    pencil.up()
    pencil.fd(PIXEL_SIZE)
    pencil.down
    pencil.end_fill()
    

def move (rows, colums):
    xcor= pencil.xcor()
    ycor= pencil.ycor()
    ycor = ycor - rows *PIXEL_SIZE
    xcor = xcor +colums * PIXEL_SIZE
    pencil.goto(xcor, ycor)


def draw_pixels (number_of_rows, number_of_columns, number_pixels):
    move (number_of_rows, number_of_columns)

    for x in range (0, number_pixels):
        draw_pixel()
       

def odd_rows ():
    range = 0 

    while range <=20:

        if range%2 ==0:
            draw_pixel("black")
            range = range+1

        elif range%2 !=0:
            draw_pixel("red")
            range= range+1



def even_rows ():
    range = 0 

    while range <=20:

        if range%2 ==0:
            draw_pixel("red")
            range = range+1

        elif range%2 !=0:
            draw_pixel("black")
            range= range+1
   
        


def chess_board ():
    for i in range (10):
         
        odd_rows()
        move(1,-21)
        even_rows()
        move(1,-21)
    


        



def main():
    initialization()
    chess_board()
   
    

    win.exitonclick()






if __name__ == "__main__":
    main()