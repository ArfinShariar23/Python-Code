def quiz_game():
    questions = [
        {"question": "What is the capital of Bangladesh?",
         "options": ["A) Dhaka", "B) Sylhet", "C) Chittagong", "D) Rangpur"],
         "answer": "A"},

        {"question": "Who is the greatest Cricketer of All time in Bangladesh?",
         "options": ["A) Tamim", "B) Mashrafee", "C) Shakib", "D) Mushfiq"],
         "answer": "C"},

        {"question": "What is the largest ocean on Earth?",
         "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
         "answer": "D"},

        {"question": "Who is the CEO of Tesla?",
         "options": ["A) Isaac Newton", "B) Donald Trumph", "C) Nikola Tesla", "D) Elon Mask"],
         "answer": "D"},

        {"question": "What is the chemical symbol for water?",
         "options": ["A) CO2", "B) O2", "C) H2O", "D) H2"],
         "answer": "C"}
    ]

    score = 0

    for i in questions:
        print(i["question"])
        for options in i["options"]:
            print(options)

        user_answer = input("Enter your Answer(A/B/C/D):").upper()
        if user_answer == i["answer"]:
            print("🎉 Correct Answer 🎉")
            score = score + 1

        else:
            print("Wrong Answer ❌")

        print()

        print(f"Your Final Score: {score}/{len(questions)}")

    print("\n Correct Answers: ")
    for i in questions:
        print(f"{i['question']}: Correct Answer: {i["answer"]}")

quiz_game()