# questions/math_knowledge.py
import random

def generate_math_knowledge_questions():
    questions, answers, data = [], [], []
    problems = [
        ("What is the value of 2^3?", ["6", "8", "9", "12"], "8"),
        ("Solve for x: 2x + 3 = 7", ["1", "2", "3", "4"], "2"),
        ("What is the area of a rectangle with length 5 and width 3?", ["8", "10", "15", "20"], "15"),
        ("What is the perimeter of a square with side length 4?", ["12", "16", "20", "24"], "16"),
        ("What is the value of π (pi) rounded to two decimal places?", ["3.12", "3.14", "3.16", "3.18"], "3.14"),
        ("What is the value of 5! (5 factorial)?", ["60", "100", "120", "150"], "120"),
        ("Solve for x: 3x - 5 = 10", ["3", "5", "7", "9"], "5"),
        ("What is the area of a circle with radius 3? (Use π = 3.14)", ["18.84", "28.26", "37.68", "47.10"], "28.26"),
        ("What is the slope of the line y = 2x + 3?", ["1", "2", "3", "4"], "2"),
        ("What is the value of 10^2?", ["50", "100", "150", "200"], "100"),
        ("What is the circumference of a circle with diameter 6? (Use π = 3.14)", ["12.56", "18.84", "25.12", "31.40"], "18.84"),
        ("Solve for x: 4x + 2 = 18", ["2", "4", "6", "8"], "4"),
        ("What is the area of a triangle with base 4 and height 3?", ["6", "8", "10", "12"], "6"),
        ("What is the value of 3^4?", ["27", "54", "81", "108"], "81"),
        ("What is the perimeter of a rectangle with length 6 and width 4?", ["16", "20", "24", "28"], "20"),
        ("What is the value of 4^2?", ["12", "14", "16", "18"], "16"),
        ("Solve for x: 5x - 10 = 15", ["3", "5", "7", "9"], "5"),
        ("What is the area of a square with side length 5?", ["15", "20", "25", "30"], "25"),
        ("What is the circumference of a circle with radius 2? (Use π = 3.14)", ["6.28", "12.56", "18.84", "25.12"], "12.56"),
        ("What is the value of 6! (6 factorial)?", ["360", "480", "720", "840"], "720"),
        # Add more to reach 50
        ("What is the slope of the line y = 3x - 2?", ["1", "2", "3", "4"], "3"),
        ("What is the area of a circle with diameter 4? (Use π = 3.14)", ["12.56", "18.84", "25.12", "31.40"], "12.56"),
        ("Solve for x: 2x - 8 = 0", ["2", "4", "6", "8"], "4"),
        ("What is the perimeter of a triangle with sides 3, 4, and 5?", ["10", "12", "14", "16"], "12"),
        ("What is the value of 7^2?", ["42", "49", "56", "63"], "49"),
        # Continue adding until you have 50 unique problems
    ]

    while len(problems) < 50:
        problems.append(
            (f"What is the value of {len(problems)}^2?", [f"{len(problems) * len(problems) - 10}", f"{len(problems) * len(problems)}", f"{len(problems) * len(problems) + 10}", f"{len(problems) * len(problems) + 20}"], f"{len(problems) * len(problems)}")
        )

    for question, options, correct_answer in problems:
        option_labels = ["A", "B", "C", "D"]
        labeled_options = [f"{label}: {value}" for label, value in zip(option_labels, options)]
        correct_index = options.index(correct_answer)
        correct_label = option_labels[correct_index]
        formatted_question = f"{question}\nOptions:\n" + "\n".join(labeled_options)
        questions.append(formatted_question)
        answers.append(correct_label)
        data.append({"question": question, "options": options, "answer": correct_answer})

    return questions, answers, data