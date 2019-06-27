import gametasks
import gameclasses


mathInstructions = "In this game, you will be given a simple arithmetic question. Each correct answer gives you one point. There is no loss of points for a wrong answer, just missing out on gaining one....and the embarassment."
binaryInstructions = "In this game, you will be given a number in base 10. Your task is to convert this number to base 2. Each correct answer gives you one point. There is no loss of points for a wrong answer, just missing out on gaining one....and the embarassment."

bg = BinaryGame()
mg = MathGame()

userName = input("What's your name?")

score = int(gametasks.getUserScore(userName))
newUser
if score == -1:
    newUser = True
    score = 0
else:
    newUser = False

print("Welcome %s! Your current score is %d." %(userName, score))

userChoice = 0

while userChoice != '-1':
    game = input("Choose your game mortal! Math Game (1) or Binary Game (2)? Choose wisely...")
    while game != '1' or game != '2':
        game = input("You entered an invalid option. Math Game (1) or Binary Game (2)? Choose wisely...or you will die.")
    numPrompt = input("How many questions do you want per game (1 - 10)? Choose wisely.....")
    while True:
        try:
            num = int(numPrompt)
            if game == '1':
                mg.numberOfQuestions = num
                gametasks.printInstructions(mathInstructions)
                newScore = mg.generateQuestions()
                newScore += score
                print("Your new current score is %d." %(score))
                userChoice = input("Press 'Enter' to Continue, or '-1' to Exit.")
            else:
                bg.numberOfQuestions = num
                gametasks.printInstructions(binaryInstructions)
                newScore = bg.generateQuestions()
                newScore += score
                print("Your new current score is %d." %(score))
                userChoice = input("Press 'Enter' to Continue, or '-1' to Exit.")
# VERY CONFUSED AS TO WHERE THE TRU BLOCK SHOULD BE AND THE WHILE LOOPS
            gametasks.updateUserScore(newUser, userName, str(score))

            break
        except TypeError:
            print("Sorry, you didn't enter a valid number.")
            numPrompt = input("How many questions do you want per game (1 - 10)? Choose wisely.....")
