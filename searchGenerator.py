import random

def searchGenerator(count):
    search = ""
    dart = random.randint(1, count - 1)
    with open("Genie.txt") as file:
        lineNum = 0
        for line in file:
            if (dart == lineNum):
                search = line
            lineNum = lineNum + 1
    return search