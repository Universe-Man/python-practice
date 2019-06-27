# import pdb; pdb.set_trace()
import os
import test
# from os import remove, rename
filepath = os.path.join(os.path.dirname(__file__), 'userScores.txt')

def printInstructions(instruction):
    print(instruction)

def getUserScore(userName):
    content = []
    # fileDir = os.path.realpath('__file__')
    # fileName = os.path.join(fileDir, 'userScores.txt')

    try:
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
    except IOError:
        print("File is not found.")
        scores = open(filepath, 'w')
        scores.close()
        return "-1"


def updateUserScore(newUser, userName, score):
    content = []
    if newUser == True:
        newUserScore = open(filepath, 'a')
        newUserScore.write([userName, score])
        newUserScore.close()
    else:
        tempFile = open('userScores.tmp', 'w')
        scores = open(filepath, 'r')
        for line in scores:
            lineArray = line.split(", ")
            content.append(lineArray)
            if lineArray[0] == userName:
                lineArray[1] = score
            tempFile.write(lineArray)
        tempFile.close()
        scores.close()
        os.remove(filepath)
        os.rename('userScores.tmp', filepath)


# print(__file__)
# test.printme()


score1 = getUserScore("Darren")
score2 = getUserScore("Albert")
score3 = getUserScore("Ann")
print(score1)

updateUserScore("false", "Darren", "496")


print(score1)
print(score2)
print(score3)
