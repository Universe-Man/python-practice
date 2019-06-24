
import os
import test

def printInstructions(instruction):
    print(instruction)

def getUserScore(userName):
    content = []
    # fileDir = os.path.realpath('__file__')
    # fileName = os.path.join(fileDir, 'userScores.txt')
    filepath = os.path.join(os.path.dirname(__file__), 'userScores.txt')
    scores = open(filepath, 'r')
    for line in scores:
        # print(line, end = '')
        lineArray = line.split(", ")
        content.append(lineArray)
        if lineArray[0] == userName:
            x = "%s %s" % (lineArray[0], lineArray[1])
            scores.close()
            return x
        # else:
        #     x = "-1"
    scores.close()
    return "-1"

print(__file__)
test.printme()
score1 = getUserScore("Darren")
score2 = getUserScore("Albert")
score3 = getUserScore("Ann")

print(score1)
print(score2)
print(score3)
