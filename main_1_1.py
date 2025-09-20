# Lab No 1

'''
Task 1.1: 
Generate an image of a flag in the console using escape characters, 
according to your variant (column "Country").
'''

ESC = "\x1b["

#definition of the funktion draw_line() -> draws a line without offset
def draw_line(width, color):
    line = " " * width
    print(f"{ESC}{color}m{line}{ESC}0m")

'''
Useful information for the definition of flag():
- the polish flag has a aspect ratio of 8:5
- terminal characters are taller than wide (approximately 2:1) --> width * 2
- 107 = white, 101 = red
'''
def flag(scale=2):
    height = 5 * scale
    width = 8 * scale * 2            
    middle = height // 2

    colors = [107, 101]             

    for _ in range(middle):
        draw_line(width, colors[0])
    for _ in range(middle, height):
        draw_line(width, colors[1])

flag(scale=4)