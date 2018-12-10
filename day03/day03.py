'''
Advent of Code: Day 3
No Matter How You Slice It
'''

# Read in the data
f = open('day03.txt', 'r')
data = f.readlines()
f.close()

# Parse a line of input into its parts
def parseInput(ln):
    splitLn = ln.split()
    ID = splitLn[0] # 0: ID Number
    inD = splitLn[2] # 2: Inner dimmensions Number
    inD = [int(inD.split(',')[0]), int(inD.split(',')[1][:-1])]
    outD = splitLn[3] # 3: Outer dimmensions Number
    outD = [int(outD.split('x')[0]), int(outD.split('x')[1])]
    return (ID, inD, outD)

def partOne():
    fabricDim = 1000
    fabric = [[0 for x in range(fabricDim)] for y in range(fabricDim)]

    # Place the claims on the master template
    for d in data:
        ID, inD, outD = parseInput(d)
        for i in range(outD[0]):
            for j in range(outD[1]):
                fabric[inD[0]+i][inD[1]+j] += 1

    # Iterate over each block of the master template to find overlaps
    cnt = 0
    for i in range(fabricDim):
        for j in range(fabricDim):
            if fabric[i][j] >= 2: cnt += 1

    return cnt

def partTwo():
    fabricDim = 1000
    fabric = [[0 for x in range(fabricDim)] for y in range(fabricDim)]

    # Place the claims on the master template
    for d in data:
        ID, inD, outD = parseInput(d)
        for i in range(outD[0]):
            for j in range(outD[1]):
                fabric[inD[0]+i][inD[1]+j] += 1

    # Go back over the completed template and look for the single overlap
    noOverlap = []
    for d in data:
        hasOverlap = False
        ID, inD, outD = parseInput(d)
        for i in range(outD[0]):
            for j in range(outD[1]):
                if fabric[inD[0]+i][inD[1]+j] > 1:
                    hasOverlap = True
        if not hasOverlap:
            noOverlap.append(ID)

    return noOverlap

if __name__ == '__main__':
    print(partOne())
    print(partTwo())
