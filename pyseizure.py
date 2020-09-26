r, g, b = 255, 0, 0

while True:
    for index, color in enumerate(('g', 'r', 'b') * 2):
	    for i in range(255):
                print(f'\x1B[48;2;{r};{g};{b}m')
                locals()[color] += 1 if index % 2 != 1 else -1
