# brain fuck+ by unknown81311#6616 & NotGrey#2415
import re

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
    
        if code[pc] in 'V^-+.,><':
            frames.append(code[pc])
        else:
            processed += code[pc]
    
        pc += 1
    if frames:
        processed += i * frames.pop()
    
    return processed
    
    
def interpret(code, debug=False):
    lib = {"r": "-#[-]"}
    read = False
    string=""
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
                    pc+=1
                    if code[pc] == "[":
                        pairs += 1
                    elif code[pc] == "]":
                        pairs -= 1
    
        elif code[pc] == "]":
            if grid[pointerTwo][pointer] != 0:
                pairs = 1
                while pairs or code[pc] != "[":
                    pc-=1
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
          if not read:
            print(chr(grid[pointerTwo][pointer]), end='')
          else:
            string += chr(grid[pointerTwo][pointer])
        elif code[pc] == ",":
            grid[pointerTwo][pointer] = ord(input()[0])
        elif code[pc] == "#":
            print(color(grid[pointerTwo][pointer], grid[pointerTwo][pointer + 1], grid[pointerTwo][pointer + 2]), end='')
        elif code[pc] == "\\":
          pc+=1
        elif code[pc] in lib:
          code = code[:pc] + preprocess(lib[code[pc]]) + code[pc+1:]
          if debug:
            print(code)
        elif code[pc] == "$":
          if read:
            s= open(string,"r").read()
            for pair in s.split(';'):
              if pair:
                a, b = pair.split(':')
                lib[a] = b
            string=""
            read = False
          else:
            read = True
        pc+=1
        if debug:
            print(grid, " ", code[pc-1])
    
    
WIDTH, HEIGHT = 10, 1
code = '\$\-\-\[\-\5\>\+\<\]\>\-\3\.\+\1\2\.\-\3\.\+\3\.\+\3\.\$r+[-5>+3<]>+.---.+7..+3[-3>+<]>-5.--[->+4<]>-.-8.+3.-6.-8.-[-3>+<]>.'

processed = preprocess(code)
interpret(processed)
