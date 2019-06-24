


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
        elif value > 10:
            print("Maximum Number of Questions = 10")
            print("Hence, number of questions will be set to 10")
        else:
            self._numberOfQuestions = value    
