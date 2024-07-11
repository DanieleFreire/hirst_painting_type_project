# Extract the colours of the image.jpg
# After extracting copy the tuple format of colours as output and save it to a colour list
# import colorgram
#
# rgb_colors = []
# colours = colorgram.extract('image.jpg', 30)
#
# for color in colours:
#     # colours = color.rgb
#     # rgb_colors.append(colours)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
#
# print(rgb_colors)

import turtle as t
import random

tom = t.Turtle()
t.colormode(255)
t.setup(1000, 2000, 0, 0)
tom.hideturtle()

colour_list = [(0, 0, 0), (225, 236, 229), (142, 176, 208), (25, 32, 48), (235, 229, 214), (24, 107, 160),
               (208, 163, 113), (142, 30, 63), (235, 221, 233), (230, 212, 92), (3, 163, 197), (218, 58, 82),
               (229, 80, 42), (54, 167, 115), (27, 61, 118), (195, 127, 167), (170, 53, 97), (107, 181, 86),
               (109, 99, 87), (240, 204, 2), (193, 187, 47), (1, 103, 119), (18, 21, 20), (48, 152, 109),
               (174, 212, 170), (117, 38, 37), (54, 38, 61), (222, 173, 188), (153, 206, 219)]


count = 0
for i in range(1, 11):
    for i in range(10):
        tom.dot(20, random.choice(colour_list))
        tom.penup()
        tom.fd(50)
    count += 1
    pos = tom.setposition(0.0, 50.00 * count)
    tom.hideturtle()




t.getscreen()
t.exitonclick()




