# Store ques answer in a dictionary
# Track the score of a player
# Loop through dictionary using key and values pair
# display each ques and allow them to answer
# Show the final result when all question are completed.

quiz = {
    "question1": {
        "question": "What is my full name",
        "answer": "Paul Prabahar"
    },
    "question2": {
        "question": "What is my native place",
        "answer": "Tuticorn"
    },
    "question3": {
        "question": "what is my date of birth",
        "answer": "6/9/2000"
    },
    "question4": {
        "question": "Do i have a girlfriend say yes or no",
        "answer": "yes"
    },
    "question5": {
        "question": "Do i have beard say yes or know",
        "answer": "yes"
    },
    "question6": {
        "question": "What's the color of my skin",
        "answer": "brown"
    },
    "question7": {
        "question": "Am I short say yes or no",
        "answer": "no"
    },
    "question8": {
        "question": "What's my favourite vegetable",
        "answer": "Mushroom"
    },
    "question9": {
        "question": "Am I vegetarian or non-vegetarian",
        "answer": "non-vegetarian"
    },
}

score = 0

for key, value in quiz.items():
    print("Question: ", value["question"])
    answer = input("Enter your answer : ")

    if answer.lower() == value['answer'].lower():
        score += 1
        print("")
        print("")

    else:
        print("Wrong")
        print("The Answer is : " + value["answer"])
        print("")
        print("")

print("You got " + str(score) + "out of 9 question correctly")
