import turtle

def draw_square(t, size):
    """Nakreslí štvorec so zadanou veľkosťou."""
    for _ in range(4):
        t.forward(size)
        t.left(90)

def draw_rectangle(t, width, height):
    """Nakreslí obdĺžnik so zadanou šírkou a výškou."""
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def draw_triangle(t, base):
    """Nakreslí rovnostranný trojuholník so zadanou základňou."""
    for _ in range(3):
        t.forward(base)
        t.left(120)

def draw_tower(t, size):
    """Nakreslí vežu so štvorcovým základom a trojuholníkovou strechou."""
    draw_square(t, size)
    t.penup()
    t.goto(t.xcor(), t.ycor() + size)
    t.pendown()
    draw_triangle(t, size)
    t.penup()
    t.goto(t.xcor() - size, t.ycor() - size)
    t.pendown()

def draw_house(t, width, height):
    """Nakreslí dom s obdĺžnikovým základom a trojuholníkovou strechou."""
    draw_rectangle(t, width, height)
    t.penup()
    t.goto(t.xcor(), t.ycor() + height)
    t.pendown()
    draw_triangle(t, width)
    t.penup()
    t.goto(t.xcor() - width, t.ycor() - height)
    t.pendown()

def draw_structures(size, num_towers, num_houses):
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("black")
    t.speed(2)
    
    # Vypočíta počiatočnú pozíciu na základe celkovej šírky štruktúr
    total_structures = num_towers + num_houses
    structure_width = size if num_towers <= num_houses else size * 2
    total_width = total_structures * structure_width + (total_structures - 1) * (2 * structure_width)
    start_x = -total_width / 2
    t.penup()
    t.goto(start_x, 0)
    t.pendown()
    
    # Kreslí striedavo veže a domy
    towers_drawn = 0
    houses_drawn = 0
    while towers_drawn < num_towers or houses_drawn < num_houses:
        if towers_drawn < num_towers:
            draw_tower(t, size)
            t.penup()
            t.forward(size * 3)  # Posunie sa dopredu o trojnásobok veľkosti veže
            t.pendown()
            towers_drawn += 1
        
        if houses_drawn < num_houses:
            draw_house(t, size * 2, size)
            t.penup()
            t.forward(size * 6)  # Posunie sa dopredu o trojnásobok šírky domu
            t.pendown()
            houses_drawn += 1
    
    # Skryje korytnačku a zobrazí výsledok
    t.hideturtle()
    screen.mainloop()

# Príklad použitia: nakresli štruktúry s veľkosťou 30, 3 vežami a 5 domami
draw_structures(30, 3, 5)
