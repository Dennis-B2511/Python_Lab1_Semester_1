# Lab No 1

'''
Task extra:
Using the console clearing function (os.system("cls") or os.system("clear")), implement a 2–3 frame animation.
'''


import os
import time

# ANSI-defination
ESC = "\x1b["
RED = f'{ESC}41m {ESC}0m'    # red block
GREEN = f'{ESC}42m {ESC}0m'  # green block
RESET = f'{ESC}0m'

def colored_bar(percentage, width=50):
    """
    percentage : absolute percentage deviation (0-100)
    width : lenght of the percentage bar
    """
    if percentage > 100:
        percentage = 100

    num_red = int(width * (percentage / 100))
    num_green = width - num_red

    return RED * num_red + GREEN * num_green

# Frame-amnimation function
def animate_bar(target_percentage, frames=3, width=50, delay=0.3):
    """
    target_percentage : my inputed percentage
    frames : how many animation frames
    """
    for frame in range(1, frames+1):
        os.system('cls')  # delate display for windows 
        current_percentage = target_percentage * (frame / frames)
        bar = colored_bar(current_percentage, width)
        print(f"Progress: {current_percentage:.1f}%")
        print(f"|{bar}|")
        time.sleep(delay)

# main program 
percent = float(input("Enter a percentage (0-100): "))
animate_bar(percent)