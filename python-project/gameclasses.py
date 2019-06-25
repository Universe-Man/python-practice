import random

# def captalize(function):
#     def myfunc(arguments):
#         a = arguments.captalize()
#         rv =  function(a)
#         return rv
#     return myfunc
#
# def test(mystr):
#     print(mystr)
#
# test = captalize(test)
#
# @captalize
# def test(mystr):
#     print(mystr)


class Game:
    def __init__ (self, numberOfQuestions = 0):
        self._numberOfQuestions = numberOfQuestions

    @property
    def numberOfQuestions(self):
        return self._numberOfQuestions

    def setterNumberOfQuestions(self, value):
        if value < 1:
            print("Minimum Number of Questions = 1")
            print("Hence, number of questions will be set to 1")
            self._numberOfQuestions = 1
        elif value > 10:
            print("Maximum Number of Questions = 10")
            print("Hence, number of questions will be set to 10")
            self._numberOfQuestions = 10
        else:
            self._numberOfQuestions = value

class BinaryGame(Game):
    # import randint from random
    # def __init__ (self,)
    def generateQuestions(self):
        # import randint from random
        score = 0
        for i in range(self.numberOfQuestions):
            base10 = random.randint(1, 100)
            base2 = bin(base10)
            correctAnswer = int(base2.replace("0b", ""))
            userResult = input("Convert this number into binary.")
            while True:
                try: answer = int(userResult)
                    if answer == correctAnswer:
                        print("You're right!")
                        score++
                        break
                    else:
                        print("Sorry, that's wrong. You're a failure.")
                        print("The correct answer is %d." %(correctAnswer))
                        print("...you should be embarrassed.")
                        # their answer below:
                        # print("Wrong answer. The correct answer is {:b}.".format(base10))
                        break
            except TypeError:
                print("Sorry your answer was not a binary number.")
                userResult = input("Please enter your answer again.")
        return score

class MathGame(Game):
    def generateQuestions(self):
        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = ['', '', '', '']
        operatorDict = {
            1: "+",
            2: "-",
            3: "*",
            4: "**"
        }
        prevOpExponent = False
        for i in range(self.numberOfQuestions):
            for num in numberList:
                num = random.randint(1, 9)
            for sym in symbolList:
                if prevOpExponent == True:
                    sym = operatorDict[random.randint(1, 3)]
                else:
                    sym = operatorDict[random.randint(1, 4)]
                if sym == "**":
                    prevOpExponent = True
                else:
                    prevOpExponent = False
            questionString = str(numberList[0])
            j = 0
            while j <= 4:
                if j == 4:
                    questionString += str(numberList[j])
                    break
                questionString += symbolList[j]
                j++
                questionString += str(numberList[j])
            correctAnswer = eval(questionString)
            questionString = questionString.replace("**", "^")
            userResult = input(questionString)
            while True:
                try: answer = int(userResult)
                    if answer == correctAnswer:
                        print("That's absolutely correct!")
                        score++
                        break
                    else:
                        print("Sorry, that's wrong. You're a failure.")
                        print("The correct answer is %d." %(correctAnswer))
                        print("...you should be embarrassed.")
                        break
                except TypeError:
                    print("Sorry your answer was not a number.")
                    userResult = input(questionString)
        return score
