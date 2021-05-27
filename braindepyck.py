import sys

print('Braindepyck: fully-working small Brainfuck interpreter written in Python (by R3D) (debug version)\nversion 1\n')
if len(sys.argv) < 2:
    print('Usage: python brainpyck.py <input file>')
    exit()

cptr = 0
iptr = 0
cellarr = []
bracketPos = []
cellCount = 10

for i in range(cellCount):
	cellarr.append(0)

braincode = open(sys.argv[1]).read()

while iptr < len(braincode):
    cmd = braincode[iptr]
    print('"' + cmd + '", ' + str(iptr) + ', ' + str(cptr) + ', ' + str(cellarr) + ', ' + str(bracketPos))
    if cmd == '>': cptr += 1
    elif cmd == '<': cptr -= 1
    elif cmd == '+': cellarr[cptr] += 1
    elif cmd == '-': cellarr[cptr] -= 1
    elif cmd == '.': print(chr(cellarr[cptr]), end="")
    elif cmd == ',': cellarr[cptr] = ord(input("Enter: ")[0])
    elif cmd == '[':
        bracketPos.append(iptr)
    elif cmd == ']':
        if cellarr[cptr] == 0:
            bracketPos.pop()
        else:
            iptr = bracketPos[len(bracketPos) - 1]
    elif cmd in ' \t\n':
        pass
    else:
        print('Invalid syntax.')
        exit()
        
    if cptr > cellCount - 1:
        cptr = 0
    elif cptr < 0:
        cptr = cellCount - 1
    if cellarr[cptr] > 255:
        cellarr[cptr] = 0
    elif cellarr[cptr] < 0:
        cellarr[cptr] = 255
    
    iptr += 1