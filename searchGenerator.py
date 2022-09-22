def searchGenerator(count):
    with open("Genie.txt") as file:
        lineNum = 0
        for line in file:
            if (count == lineNum):
                search = line
            lineNum = lineNum + 1
    print(search)
    return search