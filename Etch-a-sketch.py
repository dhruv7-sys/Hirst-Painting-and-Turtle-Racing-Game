from turtle import Turtle,Screen
kachuwa = Turtle()
my_screen = Screen()

def move_forwards():
    kachuwa.forward(10)

def move_backwards():
    kachuwa.backward(10)

def turn_left():
    new_heading = kachuwa.heading() +10
    kachuwa.setheading(new_heading)

def turn_right():
    kachuwa.left(10)

def turn_left():
    kachuwa.right(10)

def clear():
    kachuwa.clear()
    kachuwa.penup()
    kachuwa.home()
    kachuwa.pendown()

my_screen.listen()
my_screen.onkey(move_forwards, "w")
my_screen.onkey(move_backwards, "s")
my_screen.onkey(turn_left, "a")
my_screen.onkey(turn_right, "d")
my_screen.onkey(clear, "c")
my_screen.exitonclick()
