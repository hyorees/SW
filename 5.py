questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "Who wrote 'Hamlet'?", "answer": "Shakespeare"},
]

def start_quiz():
    score = 0
    for q in questions:
        print(q["question"])
        answer = input("Your answer: ")
        if answer.lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
    print(f"Your final score: {score}/{len(questions)}")

start_quiz()
