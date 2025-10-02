# Lab No 1
'''
Task 1.3: 
Generate a function graph (1st quadrant) in the console using escape characters, 
at least 9 rows high (column "Function").
'''

import math
ESC = "\x1b["

dot_character = "\u2022" 

# parameters
height = 20                         # height of the graph (lines = Zeilen)
width = 40                          # width of the graph (colums)
max_x = width                       # max parameter for x-axis
max_y = math.sqrt(max_x)            # max parameter for y-axis depending on the entered max_x

# function / y = x^0.5 == sqrt(x)
def f(x):
    return math.sqrt(x)             

# ANSI Control Sequence to clear the display/ terminal
# so the graph starts always with a clear display in the left upper corner 
print(f"{ESC}2J")

# y-axis and numbers:
'''
I want to scale the y-axis. I know that my row starts with "0" and ends with (height-1). 
Thats why I cant't just divide my max_y/height -----> max_y * (height - row - 1) / (height - 1).
I want to have a the y-label in the same format. Thats why I use an f-String of 4 characters with 1 decimal place
In the print function I want to set the cursor in the first line, first column of the terminal. The problem is
that our terminal starts with "1" and not "0" like a python loop. Thats why row+1. 
"1H" sets the cursor in the first column. 
'''
for row in range(height):
    y_value = max_y * (height - row - 1) / (height - 1)          
    label = f"{y_value:4.1f}"  # 4 characters, 1 decimal place
    print(f"{ESC}{row+1};1H{label} |", end="")

# x-axis and numbers:
'''
first print function draws a Line starting with column 6 and ending with width +1
second print function writes the numbers under the graph in 5-steps 
'''
print(f"{ESC}{height+1};6H" + "-" * (width + 1))
for x in range(0, width+1, 5):  
    print(f"{ESC}{height+2};{x+6}H{x}", end="")

# draw function graph
'''
width + 1 because we want 40 included in range

print("\u2022")  # Ausgabe: •
'''
for x in range(width + 1):
    y = f(x)
    # Zeile von oben nach unten berechnen
    row = height - 1 - int((y / max_y) * (height - 1))
    # Cursor setzen und Stern zeichnen
    print(f"{ESC}{row+1};{x+6}H{dot_character}", end="")

# set the cursor under the graph
print(f"{ESC}{height+4};1H")

