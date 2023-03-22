matrix = []
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
    for i in range(0, 13):
        print(matrix[i])
    matrix[0][12] = "End"
    matrix[12][0] = "St"

print("\n")


def updateMatrix(last, desired, c):
    lastNode = last
    desiredNode = desired
    direction = lastNode - desiredNode
    if (lastNode > desiredNode):
        lowNode = desiredNode
    else:
        lowNode = lastNode
    nodeLocations = [(0, 12, 0), (1, 12, 4), (2, 12, 8), (3, 12, 12),
                     (4, 8, 0), (5, 8, 4), (6, 8, 8), (7, 8, 12),
                     (8, 4, 0), (9, 4, 4), (10, 4, 8), (11, 4, 12),
                     (12, 0, 0), (13, 0, 4), (14, 0, 8), (15, 0, 12)
                     ]

    mList = [-3, -2, -1]
    if (direction == -4 or direction == 4):
        for i in mList:
            matrix[i + nodeLocations[lowNode][1]][nodeLocations[lowNode][2]] = c
    else:
        for i in range(1, 4):
            matrix[nodeLocations[lowNode][1]][i + nodeLocations[lowNode][2]] = c
    for i in range(0, 13):
        print(matrix[i])
    print("\n")


generateMatrix()
updateMatrix(0, 1, "X")
updateMatrix(1, 5, "X")
updateMatrix(5, 9, "X")
updateMatrix(9, 10, "-")

elif direction == "left":
# Standard procedure
if (currentNode % 4) != 0:
    currentNode -= 1
    if currentNode - 1 in nodesUsed:
        if currentNode == nodesUsed[-1]:
            c = "-"
            nodesUsed.remove(currentNode)
            line.remove(lastLink)
            print(line)
            print(f"Current {currentNode} + Last {lastNode}")
            lastLink = line[-1]
            currentNode -= 1
            if (lastLink == (0, 0)):
                lastNode = 0
            else:
                lastNode = nodesUsed[-1]
            print(line)
            print(f"Current {currentNode} + Last {lastNode}")

        else:
            print("That spot is occupied")
    else:
        lastNode = currentNode
        currentNode -= 1
        lastLink = (lastNode, currentNode)
        line.append(lastLink)
        nodesUsed.append(currentNode)
        lastDirection = "left"
