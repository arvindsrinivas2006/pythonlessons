import turtle
window = turtle.Screen()
window.bgcolor("blue")
window.title("Color Square Spiral")

Colors = ["red"] 


turtle_pen = turtle.Pen()

for counter in range(100):
  turtle_pen.pencolor(Colors[counter%4])
  turtle_pen.forward(counter)
  turtle_pen.left(145)

