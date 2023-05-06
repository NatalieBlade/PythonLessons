import turtle

win = turtle.Screen()
win.title("My game")
win.bgcolor("black")
win.setup(width=800, height=600) #высота и ширина
win.tracer(0)

#ракетки
racket_l = turtle.Turtle()
racket_l.speed(0)
racket_l.shape("square")
racket_l.color("blue")
racket_l.shapesize(stretch_len=1, stretch_wid=5)
racket_l.penup() #при передвижении ракетки она не будет оставлять за собой следов
racket_l.goto(-350, 0)

racket_r = turtle.Turtle()
racket_r.speed(0)
racket_r.shape("square")
racket_r.color("yellow")
racket_r.shapesize(stretch_len=1, stretch_wid=5)
racket_r.penup() #при передвижении ракетки она не будет оставлять за собой следов
racket_r.goto(350, 0)

#шарик

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

#Подсчет очков
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle() #скрывает отрисовку объекта
pen.goto(0, 260)
pen.write("Player A: 0 |**| Player B: 0", align="center", font=("Verdana", 22, "normal"))

#score
score_a = 0
score_b = 0

#функции

def racket_l_up():
    y = racket_l.ycor() #возвращает кординату y
    if y > 250:
        pass
    else:
        y += 20 #добавляем 20 рх
    racket_l.sety(y) #задаем значение у по новой

def racket_l_down():
    y = racket_l.ycor() #возвращает кординату y
    if y < -250:
        pass
    else:
        y -= 20 #добавляем 20 рх
    racket_l.sety(y) #задаем значение у по новой

def racket_r_up():
    y = racket_r.ycor() #возвращает кординату y
    if y > 250:
        pass
    else:
        y += 20 #добавляем 20 рх
    racket_r.sety(y) #задаем значение у по новой

def racket_r_down():
    y = racket_r.ycor() #возвращает кординату y
    if y < -250:
        pass
    else:
        y -= 20 #добавляем 20 рх
    racket_r.sety(y) #задаем значение у по новой

#keyboard
win.listen()
win.onkeypress(racket_l_up, "w")
win.onkeypress(racket_l_down, "s")
win.onkeypress(racket_r_up, "p")
win.onkeypress(racket_r_down, "l")

while True:
    win.update()

    #движение мячика
    ball.setx(ball.xcor() + ball.dx) #текущая позиция плюс 2 пикселя
    ball.sety(ball.ycor() + ball.dy) #текущая позиция плюс 2 пикселя

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} |**| Player B: {}".format(score_a, score_b), align="center", font=("Verdana", 22, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} |**| Player B: {}".format(score_a, score_b), align="center", font=("Verdana", 22, "normal"))

    if ball.xcor() > 340 and ball.ycor() < racket_r.ycor() + 50 and ball.ycor() > racket_r.ycor() - 50:
        #ball.ycor() < racket_r.ycor() + 50 and ball.ycor() > racket_r.ycor() - 50 - проверяют позицию ракетки
        ball.dx *= -1

    if ball.xcor() < -340 and ball.ycor() < racket_l.ycor() + 50 and ball.ycor() > racket_l.ycor() - 50:
        ball.dx *= -1