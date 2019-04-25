import turtle
window = turtle.Screen()
window.bgcolor("#4283f4")
window.title("Color Square Spiral")

Colors = ["red", "green", "yellow", "black"] 


turtle_pen = turtle.Pen()

for counter in range(100):
  turtle_pen.pencolor(Colors[counter%4])
  turtle_pen.forward(counter)
  turtle_pen.left(145)

