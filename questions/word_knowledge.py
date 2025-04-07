# questions/word_knowledge.py
import random

def generate_word_knowledge_questions():
    questions, answers, data = [], [], []
    problems = [
        ("Big most nearly means:", ["A: Small", "B: Large", "C: Tiny", "D: Narrow"], "B"),
        ("Fast most nearly means:", ["A: Slow", "B: Quick", "C: Steady", "D: Calm"], "B"),
        ("Happy most nearly means:", ["A: Sad", "B: Joyful", "C: Angry", "D: Tired"], "B"),
        ("Bright most nearly means:", ["A: Dim", "B: Radiant", "C: Dark", "D: Dull"], "B"),
        ("Strong most nearly means:", ["A: Weak", "B: Powerful", "C: Fragile", "D: Delicate"], "B")
    ]
    for question, options, answer in random.sample(problems, len(problems)):
        questions.append(question)
        answers.append(options)
        data.append({"question": question, "options": options, "answer": answer})
    return questions, answers, data