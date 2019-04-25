import turtle
window = turtle.Screen()
window.bgcolor("#d12c2c")
window.title("Arvind's cool progam")
turtle_pen = turtle.Pen()
turtle_pen.pencolor("red")
for counter in range(100):
  turtle_pen.circle(counter)
  turtle_pen.left(90)

