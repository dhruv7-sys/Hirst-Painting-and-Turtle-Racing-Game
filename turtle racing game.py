from turtle import Turtle, Screen
import random

race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_input = my_screen.textinput(title="make your bet", prompt="which turtle will win the race? Enter a color:")
colors = ["black", "red", "purple", "green", "yellow", "blue"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_input:
    race_on =True

while race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"you have won!the {winning_color} turtle is your turtle")
            else:
                print("you lose")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

my_screen.exitonclick()