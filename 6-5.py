# Draw with Turtle (Python Turtle Graphics)
import turtle

colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink']
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")

for i in range(100):
    t.color(colors[i % 6])
    t.forward(i * 3)
    t.left(59)

turtle.done()
