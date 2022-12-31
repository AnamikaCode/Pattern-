import turtle
import colorsys
turtle.title('Amazing Pattern')
turtle.bgcolor('black')
turtle.tracer(3)
c=10
for i in range(200):
    p=colorsys.hsv_to_rgb(c,1,0.99)
    c+=0.003
    turtle.goto(0,0)
    turtle.pencolor(p)
    turtle.left(150)
    turtle.forward(100-i)
    turtle.left(250)
    turtle.right(160)
    turtle.circle(17,7)
    turtle.forward(160)
    turtle.right(90)
    turtle.forward(i)
    turtle.left(100)
turtle.done()