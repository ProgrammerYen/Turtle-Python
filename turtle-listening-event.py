from turtle import Turtle, Screen

turtle_obj = Turtle(shape="turtle")
turtle_obj.color("green")
screen = Screen()

# List of functions and keys
functions = [(lambda: turtle_obj.left(10), "Left"), (lambda: turtle_obj.right(10), "Right"), (lambda: turtle_obj.left(90), "9"),
             (lambda: turtle_obj.right(90), "0"), (lambda: turtle_obj.forward(10), "Up"), 
             (lambda: turtle_obj.backward(10), "Down"), (lambda: turtle_obj.clear(), "c"), (lambda: turtle_obj.penup(), "u"), 
             (lambda: turtle_obj.pendown(), "d"), (lambda: turtle_obj.hideturtle(), "h"), (lambda: turtle_obj.showturtle(), "s")]

# Screen event to bind key controls to the turtle's actions
screen.listen()
for value in functions:
    screen.onkey(fun=value[0], key=value[1])
    

screen.mainloop()

