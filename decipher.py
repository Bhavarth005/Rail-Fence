from math import floor
from sys import argv
def decipher(str, key):
    strlen = len(str)
    tick_elements = ((2*key)-2)
    peaks = floor(strlen/tick_elements)
    remainder = strlen%tick_elements

    elements = [peaks]
    for i in range(key-2):
        elements.append(peaks*2)
    elements.append(peaks)

    for i in range(min(remainder, key)):
        elements[i] += 1

    if remainder>key:
        count = remainder-key
        for i in range(0, count):
            # print("r = " , remainder, " r-k = ", count, "i = ", i)
            elements[(key-2)-i] += 1
            
    # print(strlen, tick_elements, peaks, remainder, elements)
            
    indices = [0]
    total = 0
    for i in elements[:-1]:
        indices.append(total + i)
        total += i

    i = 0
    pt = []
    direction = 1

    while len(pt) < len(str):
        index = indices[i]
        pt.append(str[index])
        indices[i] += 1

        if i == 0: direction = 1
        elif i == len(indices) - 1: direction = -1

        i += direction
    return "".join(pt)

if __name__ == "__main__":
    print(decipher(argv[1], int(argv[2])))