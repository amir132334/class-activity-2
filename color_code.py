import turtle 

def draw_square(color, size):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

def drawing(star, square_size, start_x, start_y):
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()

    for row in star:
        for col in row:
            if col == "0":
                draw_square("black", square_size)
            elif col == "1":
                draw_square("white", square_size)
            elif col == "2":
                draw_square("red", square_size)
            elif col == "3":
                 draw_square("yellow", square_size)
            elif col == "4":
                 draw_square("orange", square_size)
            elif col == "5":
                 draw_square("green", square_size)
            elif col == "6":
                 draw_square("yellowgreen", square_size)
            elif col == "7":
                 draw_square("sienna", square_size)
            elif col == "8":
                 draw_square("tan", square_size)
            elif col == "9":
                 draw_square("gray", square_size)
            elif col == "A":
                 draw_square("darkgray", square_size)
                 
            turtle.penup()
            turtle.forward(square_size)
            turtle.pendown()

        turtle.penup()
        turtle.goto(start_x, turtle.ycor()- square_size)
        turtle.pendown()

    turtle.done()

turtle.speed(0)
turtle.hideturtle()

star= [
    "00000000000000000000",
    "01111111111111111110",
    "01111111111111111110",
    "01111111100111111110",
    "01111111033011111110",
    "01111110333301111110",
    "01000000333300000010",
    "01033333333333333010",
    "01104333033033340110",
    "01110433033033401110",
    "01111043033034011110",
    "01111043333334011110",
    "01110433333333401110",
    "01110433333333401110",
    "01104334400443340110",
    "01104440011004440110",
    "01044001111110044010",
    "01000111111111100010",
    "01111111111111111110",
    "00000000000000000000",
]

drawing(star, 20,-300, 295)