import turtle
window = turtle.Screen()
window.bgcolor("blue")
window.title("Arvind's cool progam")
turtle_pen = turtle.Pen()
turtle_pen.pencolor("green")
for counter in range(100):
  turtle_pen.circle(counter)
  turtle_pen.left(90)

