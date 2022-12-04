# import colorgram
# colors = colorgram.extract('image.png', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as t
import random
t.colormode(255)
kachuwa = t.Turtle()
kachuwa.speed("fastest")
kachuwa.penup()
kachuwa.hideturtle()
color_list = [(201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]

kachuwa.setheading(225)
kachuwa.forward(300)
kachuwa.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    kachuwa.dot(20, random.choice(color_list))
    kachuwa.forward(50)

    if dot_count % 10 == 0:
        kachuwa.setheading(90)
        kachuwa.forward(50)
        kachuwa.setheading(180)
        kachuwa.forward(500)
        kachuwa.setheading(0)


my_screen = t.Screen()
my_screen.exitonclick()

