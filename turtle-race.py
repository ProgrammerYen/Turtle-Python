from turtle import Turtle, Screen
import random

# Set of colours for turtles in race.
colours = ["blue", "red", "yellow", "pink", "purple", "green", "orange", "cyan", "lime"]
screen = Screen()

screen.setup(width = 700, height=700)
y_coordinate = -150

turtles = []
for i in range(9):
    my_turtle = Turtle(shape="turtle")
    my_turtle.penup()
    my_turtle.color(colours[i])
    my_turtle.goto(x=-300, y=y_coordinate)
    y_coordinate += 150/4
    turtles.append(my_turtle)
   
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?") 

while True:
    for i in turtles:
        i.forward(random.randint(100, 150))
    
        if i.xcor() > 300:
            if i.color == user_bet:
                print(f"You won. The {i.color()[0]} turtle won the race.")
                break
                
                
            else:
                print(f"You lose. The {i.color()[0]} turtle lost the race.")
                break
                
