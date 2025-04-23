import turtle

def gradient_color(start_color, end_color, step, max_steps):
    r = start_color[0] + (end_color[0] - start_color[0]) * step / max_steps
    g = start_color[1] + (end_color[1] - start_color[1]) * step / max_steps
    b = start_color[2] + (end_color[2] - start_color[2]) * step / max_steps
    return (r / 255, g / 255, b / 255)

# Setup
screen = turtle.Screen()
screen.bgcolor("#f0faff")
pen = turtle.Turtle()
pen.pensize(12)
pen.speed(0)
turtle.colormode(1.0)

# Draw "C"
pen.penup()
pen.goto(-90, 0)
pen.setheading(180)
pen.pendown()
for i in range(60):
    pen.color(gradient_color((255, 0, 0), (0, 0, 0), i, 60))
    pen.circle(60, 3)

pen.forward(20)

# Draw "L"
pen.penup()
pen.goto(30, 60)
pen.setheading(-90)
pen.pendown()
for i in range(30): 
    pen.color(gradient_color((255, 0, 0), (0, 0, 0), i, 30))
    pen.forward(4)

pen.left(90)
for i in range(30): 
    pen.color(gradient_color((255, 0, 0), (0, 0, 0), i, 30))
    pen.forward(2)

pen.hideturtle()
turtle.done()

