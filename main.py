import os
import random

todays_scores = []

def generate_question():
    if difficulty == ("A"):
        question_number1 = random.randint(0, 10)
        question_number2 = random.randint(0, 10)
        answer = random.randint(0, 10)
        divisor = random.randint(1, 10)
        
        question_symbol = random.choice(["+", "-", "*", "/"])
        
        if question_symbol == "+":
            result = question_number1 + question_number2
        elif question_symbol == "-":
            result = question_number1 - question_number2
        elif question_symbol == "/":
            question_number1 = answer * divisor
            question_number2 = divisor
            result = answer
            
        else:
            result = question_number1 * question_number2

        print(question_number1, question_symbol, question_number2)
        user_answer = input("What is your answer? (or type 'x' to exit): ")
        
        if user_answer == "x":
            print("Exiting the game...")
            return "x"
        
        user_answer = int(user_answer)
        
        if user_answer == result:
            print("Correct!")
            return True
        
        else:
            print("Incorrect. The correct answer is:", result)
            return False
    elif difficulty == ("B"):
        question_number1 = random.randint(0, 50)
        question_number2 = random.randint(0, 50)
        answer = random.randint(0, 50)
        divisor = random.randint(1, 50)
        
        question_symbol = random.choice(["+", "-", "*", "/"])
        
        if question_symbol == "+":
            result = question_number1 + question_number2
        elif question_symbol == "-":
            result = question_number1 - question_number2
        elif question_symbol == "/":
            question_number1 = answer * divisor
            question_number2 = divisor
            result = answer
            
        else:
            result = question_number1 * question_number2

        print(question_number1, question_symbol, question_number2)
        user_answer = input("What is your answer? (or type 'x' to exit): ")
        
        if user_answer == "x":
            print("Exiting the game...")
            return "x"
        
        user_answer = int(user_answer)
        
        if user_answer == result:
            print("Correct!")
            return True
        
        else:
            print("Incorrect. The correct answer is:", result)
            return False
    else:
        question_number1 = random.randint(0, 100)
        question_number2 = random.randint(0, 100)
        answer = random.randint(0, 100)
        divisor = random.randint(1, 100)
        
        question_symbol = random.choice(["+", "-", "*", "/"])
        
        if question_symbol == "+":
            result = question_number1 + question_number2
        elif question_symbol == "-":
            result = question_number1 - question_number2
        elif question_symbol == "/":
            question_number1 = answer * divisor
            question_number2 = divisor
            result = answer
            
        else:
            result = question_number1 * question_number2

        print(question_number1, question_symbol, question_number2)
        user_answer = input("What is your answer? (or type 'x' to exit): ")
        
        if user_answer == "x":
            print("Exiting the game...")
            return "x"
        
        user_answer = int(user_answer)
        
        if user_answer == result:
            print("Correct!")
            return True
        
        else:
            print("Incorrect. The correct answer is:", result)
            return False
        
while True:
    print("(A) New Game")
    print("(B) Today's Highscores")
    print("(C) View Past Highscores")
    print("(D) Exit")
    choice = input("Please select an option: ").strip().upper()
    
    #New Game
    if choice == "A":
        print("Select your difficulty:")
        print("Easy (A)")
        print("Medium (B)")
        print("Hard (C)")
        difficulty = input("Selection: ").upper()
        if difficulty == ("A"):
            difficultyscore= ("Easy")
        elif difficulty == ("B"):
            difficultyscore= ("Medium")
        else:
            difficultyscore= ("Hard")
        
        name = input("Enter your name: ").title()
        print("Starting a new game...")
        print("10 questions will be asked.")
        score = 0
        for _ in range(10):
            correct = generate_question()
            
            if correct == "x":
                break
            elif correct:
                score += 1
            
        print("Game over!", name + "'s", "score is:", score, "on", difficultyscore, "mode")
        with open("highscores.txt", "a") as file:
            file.write(f"{name}: {score}: {difficultyscore}\n")
            todays_scores.append((name, score, difficultyscore))
        
    #Today's Highscores
    elif choice == "B":
        print("Displaying today's highscores...")
        for name, score in todays_scores:
            print(f"{name}: {score}:")
        
    #View Past Highscores
    elif choice == "C":
        print("Displaying past highscores...")
        if os.path.exists("highscores.txt"):
            with open("highscores.txt", "r") as file:
                past_scores = file.readlines()
                for line in past_scores:
                    print(line.strip())
        else:
            print("No past highscores found.")
        
    #Exit
    elif choice == "D":
        print("Thank you for playing!")
        break
    
    else:
        print("Invalid option. Please try again.")
