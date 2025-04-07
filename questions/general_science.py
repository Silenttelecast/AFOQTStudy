# questions/general_science.py
import random

def generate_general_science_questions():
    questions, answers, data = [], [], []
    problems = [
        ("What gas do plants primarily use for photosynthesis?", ["A: Oxygen", "B: Carbon dioxide", "C: Nitrogen", "D: Hydrogen"], "B"),
        ("What is the boiling point of water in Celsius?", ["A: 0", "B: 50", "C: 100", "D: 150"], "C"),
        ("What type of energy is stored in a battery?", ["A: Kinetic", "B: Thermal", "C: Chemical", "D: Nuclear"], "C"),
        ("What planet is known as the Red Planet?", ["A: Venus", "B: Mars", "C: Jupiter", "D: Saturn"], "B"),
        ("What is the primary source of energy for Earth's climate system?", ["A: The moon", "B: The sun", "C: The ocean", "D: The wind"], "B")
    ]
    for question, options, answer in random.sample(problems, len(problems)):
        questions.append(question)
        answers.append(options)
        data.append({"question": question, "options": options, "answer": answer})
    return questions, answers, data