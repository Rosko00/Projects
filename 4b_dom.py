import turtle

def draw_rectangle(t, width, height):
    """Draws a rectangle with the given width and height."""
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def draw_triangle(t, base):
    """Draws an equilateral triangle with the given base size."""
    for _ in range(3):
        t.forward(base)
        t.left(120)

def draw_house_with_roof():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("black")
    t.speed(2)
    
    # Draw the base of the house
    width = 200
    height = 100
    draw_rectangle(t, width, height)
    
    # Move the turtle to the top of the base
    t.penup()
    t.goto(0, height)
    t.pendown()
    
    # Draw the roof
    draw_triangle(t, width)
    
    # Hide the turtle and display the result
    t.hideturtle()
    screen.mainloop()

draw_house_with_roof()
