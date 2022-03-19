from turtle import Turtle, Screen

# Set of colours for turtles in race.
colours = ["blue", "red", "yellow", "pink", "purple", "green", "orange", "cyan", "lime"]
screen = Screen()

# Configuring dimensions of the screen.
screen.setup(width=500, height=500)

turtle_a = Turtle(shape="turtle")
turtle_a.color(colours[0])

turtle_b = Turtle(shape="turtle")
turtle_b.color(colours[1])

turtle_c = Turtle(shape="turtle")
turtle_c.color(colours[2])

turtle_d = Turtle(shape="turtle")
turtle_d.color(colours[3])

turtle_e = Turtle(shape="turtle")
turtle_e.color(colours[4])

turtle_f = Turtle(shape="turtle")
turtle_f.color(colours[5])

turtle_g = Turtle(shape="turtle")
turtle_g.color(colours[6])

turtle_h = Turtle(shape="turtle")
turtle_h.color(colours[7])

turtle_i = Turtle(shape="turtle")
turtle_i.color(colours[-1])

# List of variables
vars = [turtle_a, turtle_b, turtle_c, turtle_d, turtle_e, turtle_f, turtle_g, turtle_h, turtle_i]

y_coordinate = 230
for turtle_obj in vars:
    turtle_obj.penup()
    turtle_obj.goto(x=-240, y=y_coordinate)
    y_coordinate -= 500/9
    
   
# Screen continuously runs, until a command is sent to close window.
screen.mainloop()