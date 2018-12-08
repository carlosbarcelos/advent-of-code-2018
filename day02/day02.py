'''
Advent of Code: Day 2
Inventory Management System
'''

from collections import Counter # Count characters in string

# Read in the data
f = open('day02.txt', 'r')
data = f.read().split()
f.close()

def partOne():
    twoTimes = 0
    threeTimes = 0

    for id in data:
        # Create count of each letter
        letterDict = Counter(id)

        # Are there any letters that appear two or three times?
        appearTwo = False
        appearThree = False

        for k, v in letterDict.items():
            if v == 2 and not appearTwo:
                twoTimes += 1
                appearTwo = True
            elif v == 3 and not appearThree:
                threeTimes += 1
                appearThree = True

    return twoTimes * threeTimes

# Return number of character differences in a string
def numCharDiff(str1, str2):
    numDiff = 0
    for i in range(len(str1)):
        if not str1[i] == str2[i]:
            numDiff += 1
    return numDiff

def partTwo():
    # Reduce to a list of single character difference
    reducedData = set()
    for id1 in data:
        for id2 in data:
            c1 = Counter(id1)
            c2 = Counter(id2)
            # If off by one letter, add to reduced set
            if sum((c1 - c2).values()) == 1 and sum((c2 - c1).values()) == 1:
                reducedData.add(id1)

    # Check for letter positions
    for id1 in data:
        for id2 in data:
            offByOne = False

            if numCharDiff(id1, id2) == 1:
                # TODO Fully automate. This requires a bit of manual work.
                return f'{id1} {id2}'

    return 'No solution found'

if __name__ == '__main__':
    print(partTwo())
