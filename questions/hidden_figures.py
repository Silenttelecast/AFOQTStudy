# questions/hidden_figures.py
import random

def generate_hidden_figures_questions():
    questions, answers, data = [], [], []
    problems = [
        ("A triangle is hidden in a complex shape. Which option shows the triangle?", ["A: Square", "B: Circle", "C: Triangle", "D: Pentagon"], "C"),
        ("A circle is hidden in a larger pattern. Which option matches the hidden shape?", ["A: Square", "B: Circle", "C: Star", "D: Hexagon"], "B"),
        ("A star is hidden in a complex drawing. Which option shows the star?", ["A: Circle", "B: Triangle", "C: Star", "D: Square"], "C"),
        ("A square is hidden in a pattern. Which option matches the hidden shape?", ["A: Square", "B: Circle", "C: Triangle", "D: Pentagon"], "A"),
        ("A hexagon is hidden in a complex shape. Which option shows the hexagon?", ["A: Circle", "B: Square", "C: Hexagon", "D: Star"], "C")
    ]
    for question, options, answer in random.sample(problems, len(problems)):
        questions.append(question)
        answers.append(options)
        data.append({"question": question, "options": options, "answer": answer})
    return questions, answers, data