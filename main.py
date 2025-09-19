import turtle
turtle.speed(0)

z = 1  # Preset patterns, 1 - flower pattern, 2 - spiral pattern, 3 - star pattern (x must be set to 0)
y = 9  # Change y (1-8) to alter the color profile of the pattern, 5, 6 - rainbow colors
x = 0  # Change x any angle (1-360) to create a custom pattern 


if x > 0:
    z = 0

def BasePattern():
    for i in range(500):
        turtle.forward(i)
        turtle.left(x)
def RainbowPattern():
    for i in range(500):
        turtle.color(colors[i % len(colors)])
        turtle.forward(i)
        turtle.left(x)
def BackgroundBlack():
    turtle.bgcolor("black")
def BackgroundWhite():
    turtle.bgcolor("white")

if z == 1:
    x = 67
if z == 2:
    x = 45
if z == 3:
    x = 144
if z < 0 or z > 3:
    print("z must be between 0 and 3")

if y == 1:
    turtle.color("red")
    BackgroundBlack()
    BasePattern()
if y == 2: 
    turtle.color("blue")
    BackgroundWhite()
    BasePattern()
if y == 3:
    turtle.color("green")
    turtle.bgcolor("yellow")
    BasePattern()
if y == 4:
    turtle.color("purple")
    BackgroundWhite()
    BasePattern()
if y == 5:
    BackgroundBlack()
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "white"]
    RainbowPattern()
if y == 6:
    BackgroundWhite()
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "black"]
    RainbowPattern()
if y == 7:
    turtle.bgcolor("white")
    colorsBW = ["Black", "white"]
    for i in range(500):
        turtle.color(colorsBW[i % len(colorsBW)])
        turtle.forward(i)
        turtle.left(x)
if y == 8:
    turtle.bgcolor("black")
    colorsWB = ["white", "black"]
    for i in range(500):
        turtle.color(colorsWB[i % len(colorsWB)])
        turtle.forward(i)
        turtle.left(x)
if y < 1 or y > 8:
    print("y must be between 1 and 8")

turtle.exitonclick()