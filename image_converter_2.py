#Peat Image Standard 2 (.pis2)

from PIL import Image

name = ""
width = 0
height = 0
pis_name = ""

name = str(input("Enter the full filepath of the image (only .png): "))
width = int(input("Enter the width of the image in pixels: "))
height = int(input("Enter the height of the image in pixels: "))
pis_name = str(input("Enter the filepath you want to give the converted image (include '.pis2' extension): "))

width = width / 100
height = height / 100

im = Image.open(name)
px = im.load()
#print(pixels[0, 0])

pixels = [""] * 10000
counter = 0

def scan_pixel(x_f, y_f, counter_f, pixels_f):
    #print(counter)
    pixels_f[counter_f] = (px[x_f, y_f])[0:3]

    counter_f = counter_f + 1

    return pixels_f, counter_f

for y_axis in range(100):
    for x_axis in range(100):
        pixels, counter = scan_pixel(x_axis * width, y_axis * width, counter, pixels) #scans the image into a 100x100 pixel image. Make sure the x and y axes are multiples of ten and adjust numbers on this line accordingly

    #print(counter)
    #print(pixels)

def dec_to_bin(integer):
    integer = integer + 1
    final = ""

    for loop in range(8):
        if integer > (2 ** (8 - (loop + 1))):
            final = final + "1"
            integer = integer - (2 ** (8 - (loop + 1)))
        else:
            final = final + "0"

    return final

final_pixels = ""

for loop in range(10000):
    spec_tuple = pixels[loop]
    
    r = spec_tuple[0]
    g = spec_tuple[1]
    b = spec_tuple[2]

    avg = int((r + g + b) / 3)

    avg_binary = dec_to_bin(avg)

    final_pixels = final_pixels + avg_binary

def bits_to_hex(bits_f):
    bytes_str_list = []

    while len(bits_f) >= 8:
        bytes_str_list.append(bits_f[0:8])

        bits_f = bits_f[8:]
    else:
        length_f = len(bits_f)

        if length_f > 0:
            bits_f = ("0" * (8 - length_f)) + bits_f
            bytes_str_list.append(bits_f)

    #print(bytes_str_list)

    integer_values = [0] * len(bytes_str_list)

    for loop in range(len(bytes_str_list)):
        byte = bytes_str_list[loop]

        sum_value = 0
        for character in range(8):
            if byte[character] == "1":
                sum_value = sum_value + (2 ** (8 - (character + 1)))

        integer_values[loop] = sum_value
        
    first_chars = [0] * len(bytes_str_list)
    second_chars = [0] * len(bytes_str_list)

    for loop in range(len(integer_values)):
        while integer_values[loop] >= 16:
            first_chars[loop] = first_chars[loop] + 1
            integer_values[loop] = integer_values[loop] - 16

        second_chars[loop] = integer_values[loop]

    chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    hexadecimals = ""

    for loop in range(len(integer_values)):
        hexadecimals = hexadecimals + chars[first_chars[loop]] + chars[second_chars[loop]]

    return hexadecimals

final_pixels_h = bits_to_hex(final_pixels)
final_pixels_b = bytes.fromhex(final_pixels_h)

print(final_pixels_h)

file = open(pis_name, "wb")
file.write(final_pixels_b)
file.close()
