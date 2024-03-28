#########################################################################
# Date Created: 03/26/2024                                              #
# Name of Project: Quiz Game                                            #
# Conceptes Used: If/Else conditions, Variables, Data Types, Operators. #
#########################################################################

print("--------------------------------")
print("Welcome to the Online Quiz Game!")
print("--------------------------------\n")

gameStart = input("Would you like to play? ")

score = 0

if gameStart.lower() == "yes":
    print("Okay! Let's Start!\n")
    
    questionOne = input("In what country did the first Starbucks open outside of North America? ").lower()
    answerOne = "Japan"
    if questionOne == answerOne.lower():
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

    questionTwo = input("What does CODA stand for? ").lower()
    answerTwo = "Child of Deaf Adults"
    if questionTwo == answerTwo.lower():
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")


    questionThree = input("In a website browser address bar, what does 'www' stand for? ").lower()
    answerThree = "World Wide Web"
    if questionThree == answerThree.lower():
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
        
    questionFour = input("Where were the Declaration of Independence, the Constitution, and the Bill of Rights stored during World War II? ").lower()
    answerFour = "Fort Knox"
    if questionFour == answerFour.lower():
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

    questionFive = input("What is the tiny piece at the end of a shoelace called? ").lower()
    answerFive = "An aglet"
    if questionFive == answerFive.lower():
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
        
    questionSix = input("Which company's slogan is 'You're in good hands?' ").lower()
    answerSix = "Allstate"
    if questionSix == answerSix.lower():
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
        
    questionSeven = input("Who was the first televised President? ").lower()
    answerSeven = "Franklin D. Roosevelt"
    if questionSeven == answerSeven.lower():
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

    questionEight = input("Originally, Amazon only sold what kind of product? ").lower()
    answerEight = "Books"
    if questionEight == answerEight.lower():
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

    questionNine = input("In 2009, what became the first Morse code character to be added since WWII? ").lower()
    answerNine = "The '@' symbol"
    if questionNine == answerNine.lower():
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

    questionTen = input("Who painted the Mona Lisa? ").lower()
    answerTen = "Leonardo da Vinci"
    if questionTen == answerTen.lower():
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

    result = float((score/10) * 100)

    print(f"All finished! Your final score is {result}%")
    
else:
    print("Bye! Thank you for your time!")    