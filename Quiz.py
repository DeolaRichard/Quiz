# Pseudocode for the program
# - Create a dict that holds the questions (Later this can be an API or received from a bank of questions)
# - Create a variable that holds and tracks the score of user
# - Print each question to the user for user to input answer
# - Check if the answer given is correct - If yes, Increment score, else return previous score
# - Calculate total score, percentage and return same to user.

Quiz = {
    "Question 1": {
        "Question": "What is the first element in the periodic table",
        "Answer": "Hydrogen"
    },
    "Question 2": {
        "Question": "What are animals that eat grass called",
        "Answer": "Herbivores"
    },
    "Question 3": {
        "Question": "What are animals that eat flesh called",
        "Answer": "Carnivores"
    },
    "Question 4": {
        "Question": "What are animals that eats both flesh and herbs called",
        "Answer": "Omnivores"
    },
    "Question 5": {
        "Question": "Who is the president of Nigeria",
        "Answer": "Peter Obi"
    },
}

score = 0

