#Peat Image Standard 2 (.pis2)

import turtle

name = ""
name = str(input("Enter the name of the .pis2 file you would like to view: "))

screen = turtle.Screen()
screen.setup(height=1000, width=1000)
screen.bgcolor('black')
screen.title('Square Grid')
screen.tracer(False)
screen.colormode(255)

def read_from_file():
    big_string = b""
    colour_values_f = []
    
    with open(name, "rb") as file:
        big_string = file.read()
        big_string = big_string.hex()

    while len(big_string) > 0:
        spec_string = big_string[:2]
        big_string = big_string[2:]

        first_char = spec_string[0]
        second_char = spec_string[1]

        def letter_getter(char):
            if char == "a":
                value = 11
            elif char == "b":
                value = 12
            elif char == "c":
                value = 13
            elif char == "d":
                value = 14
            elif char == "e":
                value = 15
            elif char == "f":
                value = 16

            return value

        if first_char.isnumeric():
            first_char_val = int(first_char)
        else:
            first_char_val = letter_getter(first_char)

        if second_char.isnumeric():
            second_char_val = int(second_char)
        else:
            second_char_val = letter_getter(second_char)

        total_sum = (first_char_val * 16) + second_char_val

        if total_sum > 255:
            total_sum = 255
        
        total_sum = str(total_sum)
        total_sum = total_sum + "," + total_sum + "," + total_sum

        colour_values_f.append(total_sum)

    return colour_values_f

colour_values = read_from_file()
#print(colour_values)

def colour_finder(string_f):
    r_f = ""
    g_f = ""
    b_f = ""
    
    while string_f[0] != ",":
        r_f = r_f + string_f[0]
        string_f = string_f[1:]

    string_f = string_f[1:]

    while string_f[0] != ",":
        g_f = g_f + string_f[0]
        string_f = string_f[1:]

    string_f = string_f[1:]

    b_f = string_f

    r_f = int(r_f)
    g_f = int(g_f)
    b_f = int(b_f)

    return r_f, g_f, b_f

array_of_lines = []

def trace_line(y_level_f, array_of_lines_f, counter_f, colour_values_f):
    line_of_turtles = [""] * 100
    
    x = -500

    for loop in range(100):
        r, g, b = colour_finder(colour_values_f[counter_f])
        #print(r, g, b)
        
        line_of_turtles[loop] = turtle.Turtle()
        line_of_turtles[loop].color(r, g, b)
        line_of_turtles[loop].shape('square')
        line_of_turtles[loop].shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        line_of_turtles[loop].penup()
        line_of_turtles[loop].goto(x, y_level_f)

        x = x + 10
        counter_f = counter_f + 1

    array_of_lines.append(line_of_turtles)

    return array_of_lines_f, counter_f

y_level = 500
counter = 0

for loop in range(100):
    array_of_lines, counter = trace_line(y_level, array_of_lines, counter, colour_values)
    screen.update()

    y_level = y_level - 10
