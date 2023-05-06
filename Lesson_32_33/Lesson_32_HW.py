import turtle

win = turtle.Screen()
win.title("Working window")
win.bgcolor("black")
win.setup(width=900, height=900)
win.tracer(0)

#квадраты
sqr_l = turtle.Turtle()
sqr_l.speed(0)
sqr_l.shape("square")
sqr_l.color("blue")
sqr_l.shapesize(stretch_len=6, stretch_wid=6)
sqr_l.penup()
sqr_l.goto(-350, 0)

sqr_r = turtle.Turtle()
sqr_r.speed(0)
sqr_r.shape("square")
sqr_r.color("yellow")
sqr_r.shapesize(stretch_len=6, stretch_wid=6)
sqr_r.penup()
sqr_r.goto(350, 0)

sqr_c = turtle.Turtle()
sqr_c.speed(0)
sqr_c.shape("square")
sqr_c.color("red")
sqr_c.shapesize(stretch_len=6, stretch_wid=6)
sqr_c.penup()
sqr_c.goto(0, 200)

while True:
    win.update()