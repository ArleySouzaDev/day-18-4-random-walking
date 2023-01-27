import turtle as t
import random

tim = t.Turtle()

colours = ["red", "blue", "orange", "black", "green", "SlateGray"]
directions = [0, 90, 180, 270]
tim.pensize(12)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))











##screen = Screen()
##screen.exitonclick()