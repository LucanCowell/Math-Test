import os
import random

todays_scores = []

def generate_question():
    question_number1 = random.randint(0, 10)
    question_number2 = random.randint(0, 10)
    question_symbol = random.choice(["+", "-", "*"])
    if question_symbol == "+":
        result = question_number1 + question_number2
    elif question_symbol == "-":
        result = question_number1 - question_number2
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
            
        print("Game over!", name + "'s", "score is:", score)
        with open("highscores.txt", "a") as file:
            file.write(f"{name}: {score}\n")
            todays_scores.append((name, score))
        
    #Today's Highscores
    elif choice == "B":
        print("Displaying today's highscores...")
        for name, score in todays_scores:
            print(f"{name}: {score}")
        
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
