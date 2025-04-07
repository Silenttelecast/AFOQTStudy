# questions/arithmetic_reasoning.py
import random

def generate_arithmetic_reasoning_questions():
    questions, answers, data = [], [], []
    problems = [
        ("If a car travels 240 miles in 4 hours, what is its average speed in miles per hour?", ["A: 40", "B: 50", "C: 60", "D: 70"], "C"),
        ("A shirt costs $20 after a 20% discount. What was the original price?", ["A: $24", "B: $25", "C: $26", "D: $28"], "B"),
        ("If 3 workers can build a wall in 6 days, how many days will it take 2 workers?", ["A: 7", "B: 8", "C: 9", "D: 10"], "C"),
        ("A recipe for 4 people requires 2 cups of flour. How many cups are needed for 6 people?", ["A: 2.5", "B: 3", "C: 3.5", "D: 4"], "B"),
        ("If a train travels 150 miles in 2.5 hours, what is its speed in miles per hour?", ["A: 50", "B: 60", "C: 70", "D: 80"], "B")
    ]
    for question, options, answer in random.sample(problems, len(problems)):
        questions.append(question)
        answers.append(options)
        data.append({"question": question, "options": options, "answer": answer})
    return questions, answers, data