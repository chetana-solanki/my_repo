# Simple CLI Quiz App

def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}")
    return score


# Questions for the quiz
quiz_questions = [
    {
        "question": "1. What is the output of print(2**3)?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
        "answer": "B"
    },
    {
        "question": "2. What does len('Python') return?",
        "options": ["A. 5", "B. 7", "C. 6", "D. 8"],
        "answer": "C"
    },
    {
        "question": "3. What is the correct way to start a function in Python?",
        "options": ["A. function myFunc():", "B. def myFunc():", "C. create myFunc():", "D. func myFunc()"],
        "answer": "B"
    },
    {
        "question": "4. What data type is used to store True or False?",
        "options": ["A. int", "B. str", "C. bool", "D. list"],
        "answer": "C"
    },
    {
        "question": "5. Which keyword is used to exit a loop early?",
        "options": ["A. exit", "B. stop", "C. break", "D. end"],
        "answer": "C"
    }
]

# Run the quiz
print("🧠 Welcome to the Python Quiz!")
total_score = run_quiz(quiz_questions)
print(f"\n🎯 Your final score is {total_score}/{len(quiz_questions)}")
