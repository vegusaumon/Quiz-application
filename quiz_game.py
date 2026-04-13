from quiz_list import *
import copy
import random
import time
from inputimeout import inputimeout, TimeoutOccurred

# Create a quiz game to test how much you know about programming.
# SOURCE URL https://www.w3schools.com/quiztest/quiztest.asp?qtest=PYTHON




""" 
Core function handles the looping of all the questions in the list.
Shuffles them for randomness so no questions are ever in the same order.
Checks for the correct user input..

Needs to add some robustness for error handling

"""

# Time limit of 30 seconds for the user to answer each question
TIME_LIMIT = 30





def main():
    # Prompt the user for the difficulty of quiz they want to use.
    difficulty = input("choose difficulty (Easy/Medium/Hard)").strip().lower()
    if difficulty == "easy":
        quiz_to_use = easy_quiz
    elif difficulty == "medium":
        quiz_to_use = medium_quiz
    elif difficulty == "hard":
        quiz_to_use = hard_quiz
    else:
        print("Invalid choice, defaulting to Easy")
        quiz_to_use = easy_quiz


    # Initialize a copy of the quiz, and a count. 
    # We also shuffle the quiz copy to get a degree of random order.


    quiz_copy = copy.deepcopy(quiz_to_use)
    count = 0
    random.shuffle(quiz_copy)
    for q in quiz_copy:
        random.shuffle(q["options"])
        print("\n"+q["question"])

        for i,option in enumerate(q["options"],1):
            print(f"{i}.{option}")
        
        '''
        Nested try block, the first nesting gets the input. 
        If nothing is input in the time limit it will raise
        Timeoutoccured and skip the question. Otherwise if we do an input
        Then if that input is within the valid range then we accept it and
        continue.

        We need to add robustness so that questions aren't skipped.

        
        '''
        try:
            user_input = inputimeout(
                "Enter the number of your answer: ",
                timeout=TIME_LIMIT

            )

            try:
                user_input = int(user_input)

                if not (1 <=user_input <= len(q["options"])):
                    print("Invalid option number. Skipping question.")
                    user_input = None
            except ValueError:
                print("Invalid input. Skipping question")
                user_input = None

        except TimeoutOccurred:
            print("Too slow! Time's up! Skipping question.")
            user_input = None
            

        
        if user_input is not None:
            selected_option = q["options"][int(user_input) -1 ]
            if selected_option == q["answer"]:
                count +=1
    
    print(f"\nFinal Score: {count}/{len(quiz_copy)}")



    # Asks the user if they want to see the answer sheet
    # This also needs to be formatted so it looks less ugly.
    while True:
        user_check  = input("Would you like to see the answer sheet (Y/N)").strip().upper()

        if user_check == "Y":
            for q in quiz_copy:
                print("\n"+q["question"])
                print("-------------------")
                print(q["answer"])
            break

        elif user_check == "N":
                print("Ending program")
                break

        else:
            print("Please enter Y or N")
    


















if __name__ == "__main__":
    main()