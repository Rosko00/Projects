import turtle

def draw_square(t, size):
    """Draws a square with the given size."""
    for _ in range(4):
        t.forward(size)
        t.left(90)

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

def draw_tower(t, size):
    """Draws a tower with a square base and a triangular roof."""
    draw_square(t, size)
    t.penup()
    t.goto(t.xcor(), t.ycor() + size)
    t.pendown()
    draw_triangle(t, size)
    t.penup()
    t.goto(t.xcor() - size, t.ycor() - size)
    t.pendown()

def draw_house(t, width, height):
    """Draws a house with a rectangular base and a triangular roof."""
    draw_rectangle(t, width, height)
    t.penup()
    t.goto(t.xcor(), t.ycor() + height)
    t.pendown()
    draw_triangle(t, width)
    t.penup()
    t.goto(t.xcor() - width, t.ycor() - height)
    t.pendown()

def draw_structures(size, num_towers, num_houses):
    # Create a screen and set the background color to white
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    # Create a turtle for drawing
    t = turtle.Turtle()
    t.color("black")
    t.speed(2)
    
    # Calculate the starting x position based on the total width of the structures
    total_structures = num_towers + num_houses
    structure_width = size if num_towers <= num_houses else size * 2
    total_width = total_structures * structure_width + (total_structures - 1) * (2 * structure_width)
    start_x = -total_width / 2
    t.penup()
    t.goto(start_x, 0)
    t.pendown()
    
    # Draw alternating towers and houses
    towers_drawn = 0
    houses_drawn = 0
    while towers_drawn < num_towers or houses_drawn < num_houses:
        if towers_drawn < num_towers:
            draw_tower(t, size)
            t.penup()
            t.forward(size * 3)  # Move forward by 3 times the size of the tower
            t.pendown()
            towers_drawn += 1
        
        if houses_drawn < num_houses:
            draw_house(t, size * 2, size)
            t.penup()
            t.forward(size * 6)  # Move forward by 3 times the width of the house
            t.pendown()
            houses_drawn += 1
    
    # Hide the turtle and display the result
    t.hideturtle()
    screen.mainloop()

# Example usage: draw structures with size 30, 3 towers, and 5 houses
draw_structures(30, 3, 5)
