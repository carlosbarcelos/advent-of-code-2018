'''
Advent of Code: Day 1
Chronal Calibration
'''

from itertools import cycle # For circular list

def partOne():
    # Read in the data
    f = open('day01.txt', 'r')
    data = f.read().split()
    f.close()

    # Iterate over the list to determine the final frequency
    freq = 0
    for i in data:
        # Break apart each line item
        op = i[:1]
        val = int(i[1:])

        # Operate
        if op == '+':
            freq += val
        elif op == '-':
            freq -= val

    return freq

def partTwo():
    # Read in the data
    f = open('day01.txt', 'r')
    data = f.read().split()
    f.close()
    cycData = cycle(data)

    # Iterate over the list forever to determine the repeated frequency
    freq = 0
    listOfFrequencies = [freq]
    for i in cycData:
        # Break apart each line item
        op = i[:1]
        val = int(i[1:])

        # Operate
        if op == '+':
            freq += val
        elif op == '-':
            freq -= val

        # If a frequency has not been seen already, add it to the list
        if freq in listOfFrequencies:
            return freq
        else:
            listOfFrequencies.append(freq)

if __name__ == '__main__':
    print(partTwo())
