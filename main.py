#brain fuck+ by unknown81311#6616
debug = False
pointer = 0
pointerTwo = 0
grid= [[0]*20 for _ in range(20)]# 20 x 20 grid
pc = 0
code = "`" # set code here
while pc < len(code):
    if code[pc] == "<":
        pointer = pointer - 1
    if code[pc] == ">":
        pointer = pointer + 1
    if code[pc] == "V":
        pointerTwo = pointerTwo - 1
    if code[pc] == "+":
        if grid[pointerTwo][pointer] == 255:
            grid[pointerTwo][pointer] = 0
        else:
            grid[pointerTwo][pointer] = grid[pointerTwo][pointer] + 1
    if code[pc] == "-":
        if grid[pointerTwo][pointer] == 0:
            grid[pointerTwo][pointer] = 255
        else:
            grid[pointerTwo][pointer] = grid[pointerTwo][pointer] - 1
    if code[pc] == "^":
        pointerTwo = pointerTwo + 1
    if code[pc] == "[":
        if grid[pointerTwo][pointer] == 0:
            while code[pc] != "]":
                pc = pc + 1
    if code[pc] == "]":
        if grid[pointerTwo][pointer] != 0:
            while code[pc] != "[":
                pc = pc - 1
    if code[pc] == "`":
        var = map(ord, input())
        for char in var:
            grid[pointerTwo][pointer] = char
            pointerTwo = pointerTwo - 1
    if code[pc] == ".":
        print(chr(grid[pointerTwo][pointer]))
    if code[pc] == ",":
        grid[pointerTwo][pointer] = input(ord(var))
    pc = pc + 1
    if debug == True:
        print (grid)
