#brain fuck+ by unknown81311#6616 & NotGrey#2415
debug = True
pointer = 0
pointerTwo = 0
grid= [[0]*1 for _ in range(5)]# 20 x 20 grid
pc = 0
code = "V`^[^][.V]" # set code here
while pc < len(code):
    if code[pc] == "<":
        pointer = pointer - 1
    if code[pc] == ">":
        pointer = pointer + 1
    if code[pc] == "V":
        pointerTwo = pointerTwo - 1
    if code[pc] == "+":# for +
        grid[pointerTwo][pointer] = (grid[pointerTwo][pointer] + 1) % 256
    if code[pc] == "-":# for -
        grid[pointerTwo][pointer] = (grid[pointerTwo][pointer] - 1) % 256
    if code[pc] == "^":
        pointerTwo = pointerTwo + 1
    if code[pc] == "[":
        elif grid[pointerTwo][pointer] == 0:
            pairs = 0
            while pairs or code[pc] != "]":
                if code[pc] == "[":
                    pairs += 1
                elif code[pc] == "]":
                    pairs -= 1
                pc = pc + 1

    if code[pc] == "]":
        elif grid[pointerTwo][pointer] != 0:
            pairs = 0
            while pairs or code[pc] != "[":
                if code[pc] == "]":
                    pairs += 1
                elif code[pc] == "[":
                    pairs -= 1
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
        print (grid," ", code[pc-1])
