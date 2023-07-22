# Pseudocode for the program
# - Create a dict that holds the questions (Later this can be an API or received from a bank of questions)
# - Create a variable that holds and tracks the score of user
# - Print each question to the user for user to input answer
# - Check if the answer given is correct - If yes, Increment score, else return previous score
# - Calculate total score, percentage and return same to user.

# Quiz questions bank
Quiz = {
    "Question 1": {
        "Question": "What is the first element in the periodic table",
        "answer": "Hydrogen"
    },
    "Question 2": {
        "Question": "What are animals that eat grass called",
        "answer": "Herbivores"
    },
    "Question 3": {
        "Question": "What are animals that eat flesh called",
        "answer": "Carnivores"
    },
    "Question 4": {
        "Question": "What are animals that eats both flesh and herbs called",
        "answer": "Omnivores"
    },
    "Question 5": {
        "Question": "Who is the president of Nigeria",
        "answer": "Peter Obi"
    },
}

# Variable to track score
score = 0

# loop through the dictionary to get each of the question
for key, value in Quiz.items():
    print(value["Question"])
    answer = input("Your Answer is: ")

    # Check if imputed answer is correct & factor in possible casing differences
    if answer.lower() == value["answer"].lower():
        print("answer is correct!")
        score = score + 1
        print("Your Score is :", score)

    else:
        print("Your answer is wrong")
        print("The right answer is: ", value["answer"])
        print("Your score is: ", score)






