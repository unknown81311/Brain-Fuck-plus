#brain fuck+ by unknown81311#6616 & NotGrey#2415
debug = False# if you are cool
pc, pointer, pointerTwo = 0, 0, 0
WIDTH, HEIGHT = 20, 20
grid= [[0] * WIDTH for _ in range(HEIGHT)]# make grid

code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."# set code here, here is an example

    def left(t):
    	if code[pc] == "<" or t:# <
    		tmp == "<"
    	    pointer = (pointer - 1) % WIDTH
    def right(t):
    	elif code[pc] == ">" or t:# >
    		tmp == ">"
    	    pointer = (pointer + 1) % WIDTH
    def down(t):
    	elif code[pc] == "V" or t:# V
    	    pointerTwo = (pointerTwo - 1) % HEIGHT
    def up(t):
    	elif code[pc] == "^" or t:# ^
    		tmp == "^"
    	    pointerTwo = (pointerTwo + 1) % HEIGHT
    def sub(t):
    	elif code[pc] == "-" or t:# -
    		tmp == "-"
    	    grid[pointerTwo][pointer] = (grid[pointerTwo][pointer] - 1) % 256
   	def add(t):
    	elif code[pc] == "+" or t:# +
    		tmp == "+"
    	    grid[pointerTwo][pointer] = (grid[pointerTwo][pointer] + 1) % 256
    def stringInput(t):
    	elif code[pc] == "`" or t:# `
    		tmp == "`"
    	    var = map(ord, input())
    	    for char in var:
    	        grid[pointerTwo][pointer] = char
    	        pointerTwo = pointerTwo - 1
   	def pri(t):
    	elif code[pc] == "." or t:# .
    	    print(chr(grid[pointerTwo][pointer]), end='')
   	def inp(t):
    	elif code[pc] == "," or t:# ,
    		tmp == ","
    	    grid[pointerTwo][pointer] = ord(input()[0])
    elif code[pc] == "[":# [

while pc < len(code):# loop over code
        if grid[pointerTwo][pointer] == 0:
            pairs = 1
            while pairs or code[pc] != "]":
                pc = pc + 1
                if code[pc] == "[":
                    pairs += 1
                elif code[pc] == "]":
                    pairs -= 1

    elif code[pc] == "]":# ]
        if grid[pointerTwo][pointer] != 0:
            pairs = 1
            while pairs or code[pc] != "[":
                pc = pc - 1
                if code[pc] == "]":
                    pairs += 1
                elif code[pc] == "[":
                    pairs -= 1
   	left()
   	up()
   	down()
   	right()
   	add()
   	sub()
   	stringInput()
   	pri()
   	inp()
    elif code[pc].isdigit():# if char is a number repeat last function
        times = ""
        while code[pc + 1].isdigit():#for each number
            pc += 1
            times += code[pc]
        times = int(times)
        for _ in range(times):
        	if tmp = "<":
        		left()
        	if tmp = "^":
				up()
			if tmp = "V":
        		down()
			if tmp = ">":
        		right()
			if tmp = "+":
        		add()
			if tmp = "-":
        		sub()
			if tmp = "`":
        		stringInput()
			if tmp = ".":
        		pri()
			if tmp = ",":
        		inp()
    pc = pc + 1
    if debug == True:# if you are cool
        print (grid," ", code[pc-1])
