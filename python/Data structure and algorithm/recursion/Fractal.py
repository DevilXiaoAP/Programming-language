import turtle


def tree(branch_len):
    if branch_len > 5:
        if branch_len < 30:
            t.pencolor('green')
        t.forward(branch_len)#小于15为基本终止条件
        t.right(20)
        tree(branch_len - 15)
        t.left(40)
        tree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)



t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('brown')
t.pensize(2)
tree(100)
t.hideturtle()
turtle.done()