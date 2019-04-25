import turtle
window = turtle.Screen()
window.bgcolor("#4283f4")
window.title("Color Square Spiral")

Colors = ["red", "green", "yellow", "black", "blue", "white", "gray", "orange"]
sides = int(turtle.numinput("number of sides", "How many sides do you want (1-8)?", 4, 1, 8))



turtle_pen = turtle.Pen()

for counter in range(100):
  turtle_pen.pencolor(Colors[counter%sides])
  turtle_pen.forward(counter)
  turtle_pen.left(145)

