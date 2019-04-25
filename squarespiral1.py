import turtle
window = turtle.Screen()
window.bgcolor("#4283f4")
window.title("Arvind's cool progam")
turtle_pen = turtle.Pen()

colors=["red", "yellow", "blue", "green"]

your_name = turtle.textinput("Enter your name",  "What is your name? ")

for counter in range(100):
  turtle_pen.pencolor(colors[counter% 4])

  turtle_pen.penup()
  
  turtle_pen.forward(counter*4)
  turtle_pen.pendown()

  turtle_pen.write(your_name, font=("Cambria", int((counter+4)/4),"bold"))

  turtle_pen.left(90)


