# brain fuck+ by unknown81311#6616 & NotGrey#2415

def color(r=0, g=0, b=0):return f"\033[38;2;{r};{g};{b}m"
    
def get_int(code, pc):
    i = ''
    code_s = len(code)
    while pc < code_s and code[pc].isdigit():
        i += code[pc]
        pc += 1
    return int(i if i else '1'), len(i)
    
    
def preprocess(code):
    code_s = len(code)
    processed = ''
    pc = 0
    frames = []
    
    while pc < code_s:
        i, s = get_int(code, pc)
        if frames:
            processed += i * frames.pop()
        if s:
            pc += s
            continue
    
        if code[pc] in '#V^-+.,><':
            frames.append(code[pc])
        else:
            processed += code[pc]
    
        pc += 1
    
    if frames:
        processed += i * frames.pop()
    
    return processed
    
    
def interpret(code, debug=False):
    pc, pointer, pointerTwo = 0, 0, 0
    grid = [[0] * WIDTH for _ in range(HEIGHT)]
    
    while pc < len(code):
        if code[pc] == "<":
            pointer = (pointer - 1) % WIDTH
        elif code[pc] == ">":
            pointer = (pointer + 1) % WIDTH
        elif code[pc] == "V":
            pointerTwo = (pointerTwo - 1) % HEIGHT
        elif code[pc] == "^":
            pointerTwo = (pointerTwo + 1) % HEIGHT
        elif code[pc] == "-":
            grid[pointerTwo][pointer] = (grid[pointerTwo][pointer] - 1) % 256
        elif code[pc] == "+":
            grid[pointerTwo][pointer] = (grid[pointerTwo][pointer] + 1) % 256
    
        elif code[pc] == "[":
            if grid[pointerTwo][pointer] == 0:
                pairs = 1
                while pairs or code[pc] != "]":
                    pc = pc + 1
                    if code[pc] == "[":
                        pairs += 1
                    elif code[pc] == "]":
                        pairs -= 1
    
        elif code[pc] == "]":
            if grid[pointerTwo][pointer] != 0:
                pairs = 1
                while pairs or code[pc] != "[":
                    pc = pc - 1
                    if code[pc] == "]":
                        pairs += 1
                    elif code[pc] == "[":
                        pairs -= 1
    
        elif code[pc] == "`":
            var = map(ord, input())
            for char in var:
                grid[pointerTwo][pointer] = char
                pointerTwo = pointerTwo - 1
        elif code[pc] == ".":
            print(chr(grid[pointerTwo][pointer]), end='')
        elif code[pc] == ",":
            grid[pointerTwo][pointer] = ord(input()[0])
        elif code[pc] == "#":
            print(color(grid[pointerTwo][pointer], grid[pointerTwo][pointer + 1], grid[pointerTwo][pointer + 2]), end='')

        pc = pc + 1
    
        if debug:
            print(grid, " ", code[pc-1])
    
    
WIDTH, HEIGHT = 20, 20
code = ',>+255>+255>+0<<#<.'

processed = preprocess(code)
interpret(processed)
