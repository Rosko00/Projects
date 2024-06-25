import turtle

def draw_square(t, size):
    """Draws a square with the given size."""
    for _ in range(4):
        t.forward(size)
        t.left(90)

def draw_triangle(t, size):
    """Draws an equilateral triangle with the given size."""
    for _ in range(3):
        t.forward(size)
        t.left(120)

def draw_tower_with_roof():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("black")
    t.speed(2)
    
    # Draw the base of the tower
    draw_square(t, 100)
    
    # Move the turtle to the top of the base
    t.penup()
    t.goto(0, 100)
    t.pendown()
    
    # Draw the roof
    draw_triangle(t, 100)
    
    # Hide the turtle and display the result
    t.hideturtle()
    screen.mainloop()

draw_tower_with_roof()
