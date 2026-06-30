# Math-Test
This is a python based math test, where there are 10 questions where the user will answer the questions to get an end score out of 10 and will be able to riew the leaderboards throgh a seperate function.

There is currently 4 main functions
(A) Quiz
(B) Todays Scores
(C) View Past Scores
(D) Quit

The users name is also collected when starting a new game, allowing for the users score to be recorded with their matching name.

These questions will be either addition, subtraction, multiplication, or division. When the questions are divison based, it is ensured that the result will not be a decimal to avoid unnessary complication.

These questions are randomly generated through the random module, which allows for a near infinite amount of questions to be asked.

These scores will be stored on a seperate text file, which allows for the memory of the revious user inputs to be accessed upon the base menu.

There is now a difficulty function that allows for 3 modes of random question generation:
(A) Easy
(B) Medium
(C) Hard

The users chosen difficulty is also stored on the same text file, meaning that when past scores are reviewed, it will show the users name, the users score, and the users chosen difficuly.

The greatest challenge in developing this math quiz was ensuring that the division could never result in a decimal as that would create problems when users calculate and input their answer due to the difference in rounding.
