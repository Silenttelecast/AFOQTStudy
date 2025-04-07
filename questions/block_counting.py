# questions/block_counting.py
import random

def generate_block_counting_questions():
    questions, answers, data = [], [], []
    problems = [
        ("A stack of blocks is shown. How many blocks are in the stack?", ["A: 3", "B: 4", "C: 5", "D: 6"], "C"),
        ("A 3D block structure is shown. How many blocks are visible?", ["A: 2", "B: 3", "C: 4", "D: 5"], "B"),
        ("A block tower is shown. How many blocks are in the tower?", ["A: 5", "B: 6", "C: 7", "D: 8"], "A"),
        ("A block arrangement is shown. How many blocks are there?", ["A: 4", "B: 5", "C: 6", "D: 7"], "C"),
        ("A 3D block pile is shown. How many blocks are in the pile?", ["A: 3", "B: 4", "C: 5", "D: 6"], "D")
    ]
    for question, options, answer in random.sample(problems, len(problems)):
        questions.append(question)
        answers.append(options)
        data.append({"question": question, "options": options, "answer": answer})
    return questions, answers, data