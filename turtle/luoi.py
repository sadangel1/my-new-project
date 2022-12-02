import turtle


def make_grid(t, grid_size = 800, sub_divisions = 20):

    #Tạo lưới
    cell_size = grid_size / float(sub_divisions)  # force float for Python 2

    t.hideturtle()
    t.penup()
    t.goto(-grid_size/2, grid_size/2)
    t.pendown()
    t.speed(0)
    t.color('#efefef')
    angle = 90

    for _ in range(4):
        t.forward(grid_size)
        t.right(angle)

    for _ in range(2):
        for _ in range(1, sub_divisions):
            t.forward(cell_size)
            t.right(angle)
            t.forward(grid_size)
            t.left(angle)

            angle = -angle

        t.forward(cell_size)
        t.right(angle)

    t.penup()    
    t.goto(0,grid_size/2)


    t.pendown()  
    t.color("#ccc")
    t.right(90)
    t.forward(grid_size)

    t.penup()    
    t.goto(-grid_size/2,0)
    t.pendown()  
    t.color("#ccc")
    t.left(90)
    t.forward(grid_size)

    t.penup()    
    t.goto(0,0)
    t.pendown()    

    # Vẽ tọa độ
    for i in range(-grid_size//2, grid_size//2, sub_divisions*2):
        t.penup()
        t.goto(i-8, 0)
        t.penup()
        t.write(i, font=("Verdana", 8, "bold"))
        
        if (i == 0):
            continue
        t.penup()
        t.goto(1, i-6)
        t.penup()
        t.write(i, font=("Verdana", 8, "bold"))
    
    
    