# questions/verbal_analogies.py
import random

def generate_verbal_analogies_questions():
    questions, answers, data = [], [], []
    problems = [
        ("Big is to small as tall is to:", ["A: Short", "B: High", "C: Wide", "D: Long"], "A"),
        ("Fast is to slow as big is to:", ["A: Large", "B: Tiny", "C: Huge", "D: Great"], "B"),
        ("Dog is to puppy as cat is to:", ["A: Kitten", "B: Cub", "C: Chick", "D: Foal"], "A"),
        ("Hot is to cold as light is to:", ["A: Bright", "B: Dark", "C: Heavy", "D: Warm"], "B"),
        ("Teacher is to student as doctor is to:", ["A: Nurse", "B: Patient", "C: Hospital", "D: Medicine"], "B")
    ]
    for question, options, answer in random.sample(problems, len(problems)):
        questions.append(question)
        answers.append(options)
        data.append({"question": question, "options": options, "answer": answer})
    return questions, answers, data