
# Lab No 1
'''
Task 1.2: 
Generate a repeating pattern in the console (column "Pattern").
'''


# height and width of a block
block_width = 2
block_height = 1

# Creating a matrix, which we will fill with our unicode block symbols (1 = Block, 0 = empty string)
pattern_matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# unicode block symbol
BLOCK = "\u2588"

# user input 
repeat_horizontal = int(input("How many times should the pattern repeat horizontally?"))
repeat_vertical = int(input("How many times should the pattern repeat vertically?"))

# Muster ausgeben
for _ in range(repeat_vertical):  # Vertikale Wiederholung
    for row in pattern_matrix:
        # Zeile für das Muster aufbauen
        line = ""
        for cell in row:
            if cell == 1:  # explizit prüfen, ob die Zelle 1 ist
                line += BLOCK * block_width
            elif cell == 0:  # explizit prüfen, ob die Zelle 0 ist
                line += " " * block_width
        # Zeile horizontal wiederholen
        line *= repeat_horizontal
        # Höhe des Blocks wiederholen
        for i in range(block_height):
            print(line)



  