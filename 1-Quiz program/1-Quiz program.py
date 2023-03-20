# a dictonary that stores questions and answer
# have A variable that tracks the score of the player
#loop through the dictonary using the key values pairs
#display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question1": {
        "question": "What is the capital of Perú?",
        "answer": "Lima"
    },
    "question2": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question3": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Chile?",
        "answer": "Santiago"
    },
    "question6": {
        "question": "What is the capital of Austria?",
        "answer": "Viena"
    },
    "question7": {
        "question": "What is the capital of Japan?",
        "answer": "Tokyo"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct!')
        score = score + 1
        print("Your score is: " + str(score))
    
    else:
        print("Wrong :c ")
        print("You score is: " + str(score))

print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score/7 * 100)) + "%")