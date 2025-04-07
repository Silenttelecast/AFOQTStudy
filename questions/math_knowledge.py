# questions/math_knowledge.py
import random

def generate_math_knowledge_questions():
    questions, answers, data = [], [], []
    problems = [
        ("What is the value of 2^3?", ["A: 6", "B: 8", "C: 9", "D: 12"], "B"),
        ("Solve for x: 2x + 3 = 7", ["A: 1", "B: 2", "C: 3", "D: 4"], "B"),
        ("What is the area of a rectangle with length 5 and width 3?", ["A: 8", "B: 10", "C: 15", "D: 20"], "C"),
        ("What is the perimeter of a square with side length 4?", ["A: 12", "B: 16", "C: 20", "D: 24"], "B"),
        ("What is the value of π (pi) rounded to two decimal places?", ["A: 3.12", "B: 3.14", "C: 3.16", "D: 3.18"], "B")
    ]
    for question, options, answer in random.sample(problems, len(problems)):
        questions.append(question)
        answers.append(options)
        data.append({"question": question, "options": options, "answer": answer})
    return questions, answers, data