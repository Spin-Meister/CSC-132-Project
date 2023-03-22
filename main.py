matrix = []
grid = [["sw", "", ""],
        ["", "sb", ""],
        ["", "", ""]]
nodeLocations = [(0, 12, 0), (1, 12, 4), (2, 12, 8), (3, 12, 12),
                 (4, 8, 0), (5, 8, 4), (6, 8, 8), (7, 8, 12),
                 (8, 4, 0), (9, 4, 4), (10, 4, 8), (11, 4, 12),
                 (12, 0, 0), (13, 0, 4), (14, 0, 8), (15, 0, 12)
                 ]


def generateMatrix():
    for i in range(0, 13):
        matrix.append([])
    nodeNum = 12
    rowNum = 0
    for i in range(0, 13):
        if i % 4 == 0:
            for j in range(0, 13):
                if (j % 4 == 0):
                    matrix[rowNum].append("O")
                    nodeNum += 1
                else:
                    matrix[rowNum].append("-")
            nodeNum -= 8
        else:
            for k in range(0, 13):
                if (k % 4 == 0):
                    matrix[rowNum].append("-")
                else:
                    matrix[rowNum].append(" ")
        rowNum += 1
    matrix[0][12] = "E"
    matrix[12][0] = "S"
    for i in range(0, 13):
        print(' '.join(matrix[i]))


def updateMatrix(last, desired, c):
    lastNode = last
    desiredNode = desired
    direction = lastNode - desiredNode
    if (lastNode > desiredNode):
        lowNode = desiredNode
    else:
        lowNode = lastNode

    mList = [-3, -2, -1]
    if (direction == -4 or direction == 4):
        for i in mList:
            matrix[i + nodeLocations[lowNode][1]][nodeLocations[lowNode][2]] = c
    else:
        for i in range(1, 4):
            matrix[nodeLocations[lowNode][1]][i + nodeLocations[lowNode][2]] = c
    for i in range(0, 13):
        print(' '.join(matrix[i]))
    print("\n")


nodes = range(0, 15)

dotLocals = []
lastNode = 0
currentNode = 0
lastLink = (0, 0)
lastDirection = ""
line = [(0, 0)]
nodesUsed = [0]
generateMatrix()

while True:
    # indicates whether the updateMatrix function will add or subtract from the line drawn in the matrix
    c = "#"
    while True:
        direction = input("Which direction?").lower()
        if direction in ["left", "right", "up", "down"]:
            break
        else:
            print("That is not a valid command")
    # Protocol for moving upwards
    projectedNode = currentNode
    if (direction == "left"):
        projectedNode -= 1
    elif (direction == "right"):
        projectedNode += 1
    elif (direction == "down"):
        projectedNode -= 4
    else:
        projectedNode += 4
    print(projectedNode)
    print(nodesUsed[-1])
    if projectedNode in nodesUsed:
        if projectedNode == nodesUsed[-2]:
            print("Herro")
            c = "-"
            nodesUsed = nodesUsed[:-1]
            lastLink = line[-1]
            line = line[:-1]
            currentNode = projectedNode
            if len(nodesUsed) < 2:
                lastNode = 0
            else:
                lastNode = nodesUsed[-2]

    elif direction == "up":
        # First move snaps to grid
        if lastLink == (0, 0):
            lastLink = (0, 4)
            currentNode = 4
            nodesUsed.append(4)
            line.append(lastLink)
            lastDirection = "up"
        # Removes previous link from list on move that is opposite to last move
        elif currentNode // 4 != 3:
            if currentNode + 4 in nodesUsed:
                print("That spot is occupied")
            else:
                lastNode = currentNode
                currentNode += 4
                lastLink = (lastNode, currentNode)
                nodesUsed.append(currentNode)
                line.append(lastLink)
                lastDirection = "up"
        # Prevents invalid movement
        else:
            print("That is not a valid direction as you are on the top row.")

    # Protocol for moving downwards
    elif direction == "down":
        # Standard procedure
        if currentNode > 3:
            if currentNode - 4 in nodesUsed:
                print("That spot is occupied")
            else:
                lastNode = currentNode
                currentNode -= 4
                lastLink = (lastNode, currentNode)
                line.append(lastLink)
                lastDirection = "down"
                nodesUsed.append(currentNode)
        # Prevents invalid movement
        else:
            print("That is not a valid direction as you are on the bottom row.")

    # Protocol for moving rightwards
    elif direction == "right":
        # First move snaps to grid
        if lastLink == (0, 0):
            lastLink = (0, 1)
            currentNode = 1
            nodesUsed.append(1)
            line.append(lastLink)
            lastDirection = "right"
        # Standard procedure
        elif (currentNode % 4) != 3:
            if currentNode + 1 in nodesUsed:
                print("That spot is occupied")
            else:
                lastNode = currentNode
                currentNode += 1
                lastLink = (lastNode, currentNode)
                line.append(lastLink)
                lastDirection = "right"
                nodesUsed.append(currentNode)
        # Prevents invalid movement
        else:
            print("That is not a valid direction as you are on the rightmost column.")

    # Protocol for moving leftwards
    elif direction == "left":
        # Standard procedure
        if (currentNode % 4) != 0:
            if currentNode - 1 in nodesUsed:
                if currentNode == nodesUsed[-1]:
                    c = "-"
                    nodesUsed = nodesUsed[:-1]
                    lastLink = line[-1]
                    line = line[:-1]
                    currentNode -= 1
                    if (len(nodesUsed) < 2):
                        lastNode = 0
                    else:
                        lastNode = nodesUsed[-2]
                else:
                    print("That spot is occupied")
            else:
                lastNode = currentNode
                currentNode -= 1
                lastLink = (lastNode, currentNode)
                line.append(lastLink)
                nodesUsed.append(currentNode)
                lastDirection = "left"
        # Prevents invalid movement
        else:
            print("That is not a valid direction as you are on the leftmost column row.")
    updateMatrix(lastLink[0], lastLink[1], c)
    print(nodesUsed)
    if currentNode == 15:
        break



######
#Searching Ideas
#Recursively checks nearby squares and adds reachable squares to a color based list
#If White and Black lists intersect the puzzle is failed
#Clear List on Enter
#Checks hashes to see if path is open
#Considers previously occupied squares as blocked off areas
#If it finds a like color item that item doesn't need to check
#Number puzzle elements of like type
#Special way to check if line is border of grid


#Recursion