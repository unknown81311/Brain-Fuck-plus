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
    
        if code[pc] in 'V^-+.,><':
            frames.append(code[pc])
        elif code[pc] in "(":
            tmp=""
            pc += 1
            while code[pc] != ")":
              tmp += code[pc]
              pc += 1
            pc += 1
            i, j = get_int(code, pc)
            pc += j
            frames.append(tmp * i)
        else:
          processed += code[pc]
    
        pc += 1
    if frames:
        processed += i * frames.pop()
    
    return processed
 
def interpret(code, debug=False):
    lib = {}#example: {"r": "-#[-]"} so when "r" is called it will then do "-#[-]"
    read = False
    string=""

    stringTwo=""

    pc, pointer, pointerTwo = 0, 0, 0
    grid = [[0] * WIDTH for _ in range(HEIGHT)]

    while pc < len(code):
        if code[pc] == "<":#go left
            pointer = (pointer - 1) % WIDTH
        elif code[pc] == ">":#go right
            pointer = (pointer + 1) % WIDTH
        elif code[pc] == "V":#go down
            pointerTwo = (pointerTwo - 1) % HEIGHT
        elif code[pc] == "^":#go up
            pointerTwo = (pointerTwo + 1) % HEIGHT
        elif code[pc] == "-":#subtract 1 
            grid[pointerTwo][pointer] = (grid[pointerTwo][pointer] - 1) % 256
        elif code[pc] == "+":#add 1
            grid[pointerTwo][pointer] = (grid[pointerTwo][pointer] + 1) % 256

        elif code[pc] == "[":#loop
            if grid[pointerTwo][pointer] == 0:
                pairs = 1
                while pairs or code[pc] != "]":
                    pc+=1
                    if code[pc] == "[":
                        pairs += 1
                    elif code[pc] == "]":
                        pairs -= 1

        elif code[pc] == "]":# end of loop
            if grid[pointerTwo][pointer] != 0:
                pairs = 1
                while pairs or code[pc] != "[":
                    pc-=1
                    if code[pc] == "]":
                        pairs += 1
                    elif code[pc] == "[":
                        pairs -= 1

        elif code[pc] == "`":# get string of charicters
            var = map(ord, input())
            for char in var:
                grid[pointerTwo][pointer] = char
                pointerTwo = pointerTwo - 1

        elif code[pc] == ".":#print char or define a char for a library or define a char to run a script
          if not read:
            print(chr(grid[pointerTwo][pointer]), end='')
          else:
            string += chr(grid[pointerTwo][pointer])

        elif code[pc] == ",":# get 1 charicter input
            grid[pointerTwo][pointer] = ord(input()[0])

        elif code[pc] == "#":#change color
            print(color(grid[pointerTwo][pointer], grid[pointerTwo][pointer + 1], grid[pointerTwo][pointer + 2]), end='')

        elif code[pc] == "\\":#skip next char
          pc+=1

        elif code[pc] in lib:#run a function in the library
          code = code[:pc] + preprocess(lib[code[pc]]) + code[pc+1:]
          if debug:#for cool people
            print(code)

        elif code[pc] == "$":#read libraries
          if read:
            s= open(string,"r").read()
            for pair in s.split(';'):
              if pair:
                a, b = pair.split(':')
                lib[a] = b
                if debug:#for cool people
                  print(a,b)
            string=""
            read = False
          else:
            read = True
        elif code[pc] == "!":#run some py code
          if read:
            exec(string)
            if debug:#for cool people
              print("code:",string)
            read = False
          else:
            read = True
        pc+=1
        if debug:#for cool people
            print(grid, " ", code[pc-1])

WIDTH, HEIGHT = 10, 10 #width and height of grid 
code = '\$\-\-\[\-\5\>\+\<\]\>\-\3\.\+\1\2\.\-\3\.\+\3\.\+\3\.\$r+[-5>+3<]>+.---.+7..+3[-3>+<]>-5.--[->+4<]>-.-8.+3.-6.-8.-[-3>+<]>.'# the code with an example.

processed = preprocess(code)
interpret(processed)
