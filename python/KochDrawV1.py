# 请在...补充一行或多行代码
import turtle
def koch(size, n):
    if n ==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(1/3 *size,n-1)
def main(level):
    turtle.speed(10)
    turtle.colormode(255)
    turtle.color((255,0,0),(0,0,255))
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.begin_fill()
    for i in range(3):
        koch(400,level)
        turtle.right(120)
    turtle.hideturtle()
    turtle.end_fill()
    turtle.done()
try:
    level = eval(input("请输入科赫曲线的阶: "))
    main(level)
except:
    print("输入错误")
