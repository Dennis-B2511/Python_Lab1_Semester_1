# Lab No 1

'''
Task 1.4: 
Using the provided file with a numerical sequence sequence.txt, 
output a percentage ratio chart according to your variant.

"Absolute average of the first 125 and the second 125 numbers"
'''
import numpy as np

# ANSI-defination
ESC = "\x1b["
RED = f'{ESC}41m {ESC}0m'    # red block
GREEN = f'{ESC}42m {ESC}0m'  # green block
RESET = f'{ESC}0m'

# read sequence.txt   
with open("sequence.txt", "r") as number_file:
    number_file.seek(0)
    numbers = []
    for line in number_file:
        number = float(line)  
        numbers.append(number)
    
    first_125 = numbers[:125]
    second_125 = numbers[125:]
    all_250 = numbers[0:]
    
    

    #absolut avarage first and second 125 numbers. for this we have to put the numbers in absolute value = abs() function
    average_first_125_abs = sum(abs(x) for x in first_125) / len(first_125)
    average_second_125_abs = sum(abs(x) for x in second_125) / len(second_125)
    average_all_250_abs = sum(abs(x) for x in all_250) / len(all_250)

    print(f"\n\nThe absolute avarage of all numbers in sequence.txt is:            {average_all_250_abs}")
    print(f"The absolute avarage of the first 125 numbers in sequence.txt is:  {average_first_125_abs}")
    print(f"The absolute avarage of the second 125 numbers in sequence.txt is: {average_second_125_abs}\n\n")

     # absolute percentage deviation
    deviation_first = (abs(average_first_125_abs - average_all_250_abs) / average_all_250_abs) * 100
    deviation_second = (abs(average_second_125_abs - average_all_250_abs) / average_all_250_abs) * 100

    print("The absolut percentage deviasion of average_first_125_abs to average_all_250_abs ist:", deviation_first, "%")
    print("The absolut percentage deviasion of average_second_125_abs to average_all_250_abs ist:", deviation_second, "%\n\n")
    


def colored_bar(percentage, width=50):
    """
    percentage : absolute percentage deviation (0-100)
    width : lenght of the percentage bar
    """
    # limit of 100%
    if percentage > 100:
        percentage = 100
        

   
    num_red = int(width * (percentage / 100))
    num_green = width - num_red

    bar = RED * num_red + GREEN * num_green
    return bar



print("Absolute Average Deviations (0-100%)")
print(f"First 125  |{colored_bar(deviation_first)}| {deviation_first:.1f}%\n\n")
print(f"Second 125 |{colored_bar(deviation_second)}| {deviation_second:.1f}%")

  









