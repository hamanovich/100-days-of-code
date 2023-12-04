import turtle as turtle_module
import random
import colorgram

DOTS = 100
COLORS = 30

rgb_colors = []
colors = colorgram.extract('hirst.jpeg', COLORS)

for color in colors:
    rgb_colors.append(color.rgb)


turtle_module.colormode(255)
t = turtle_module.Turtle()

t.speed("fastest")
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)

for dot_count in range(1, DOTS + 1):
    t.dot(20, random.choice(rgb_colors))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
