import sys

print('Brainpyck: fully-working small Brainfuck interpreter written in Python (by R3D)\nversion 1\n')
if len(sys.argv) < 2:
    print('Usage: python brainpyck.py <input file>')
    exit()

cptr = 0
iptr = 0
cellarr = []
bracketPos = []

for i in range(10):
	cellarr.append(0)

braincode = open(sys.argv[1]).read()

while iptr < len(braincode):
    cmd = braincode[iptr]
    
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
        
    if cptr > 9:
        cptr = 0
    elif cptr < 0:
        cptr = 9
    
    if cellarr[cptr] > 255:
        cellarr[cptr] = 0
    elif cellarr[cptr] < 0:
        cellarr[cptr] = 255
    
    iptr += 1