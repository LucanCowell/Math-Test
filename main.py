import random

def generate_question():
    question_number1 = random.randint(0, 10)
    question_number2 = random.randint(0, 10)
    question_symbol = random.choice(["+", "-", "*", "/"])
    if question_symbol == "+":
        result = question_number1 + question_number2
    elif question_symbol == "-":
        result = question_number1 - question_number2
    elif question_symbol == "*":
        result = question_number1 * question_number2
    else:
        result = question_number1 / question_number2

    print(question_number1, question_symbol, question_number2)
    user_answer = int(input("What is your answer? "))
    if user_answer == result:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", result)

while True:
    print("(A) New Game")
    print("(B) Today's Highscores")
    print("(C) View Past Highscores")
    print("(D) Exit")
    choice = input("Please select an option: ").strip().upper()
    
    #New Game
    if choice == "A":
        print("Starting a new game...")
        print("10 questions will be asked.")
        for _ in range(10):
            generate_question()
        
    #Today's Highscores
    elif choice == "B":
        print("Displaying today's highscores...")
        
    #View Past Highscores
    elif choice == "C":
        print("Displaying past highscores...")
        
    #Exit
    elif choice == "D":
        print("Thank you for playing!")
        break
    
    else:
        print("Invalid option. Please try again.")
