import turtle


def draw_circle(some_turtle):
        some_turtle.circle(100)
        


def draw_art():
    window=turtle.Screen()
    window.bgcolor("red")
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(50)
    for i in range(0,36):
        draw_circle(brad)
        brad.right(10)
    brad.right(90)
    brad.forward(500)
    window.exitonclick()
draw_art()
draw_circle()
