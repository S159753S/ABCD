import turtle

for i in range(5):
    for j in range(5):
        for k in range(4):
            turtle.forward(100)
            turtle.left(90)
        turtle.forward(100)
    turtle.backward(500)
    turtle.left(90)
    turtle.forward(100)
    turtle.setheading(0)
