# questions/instrument.py
import random
import os

def generate_instrument_comprehension_questions():
    questions, answers, data = [], [], []
    options = ["A: Climb, Right", "B: Climb, Left", "C: Descend, Right", "D: Descend, Left"]

    # Read pre-generated question data
    for i in range(20):
        try:
            with open(f"images/instrument/question_{i}.txt", "r") as f:
                line = f.read().strip()
                parts = line.split(", ")
                climb = float(parts[0].split(": ")[1])
                bank = float(parts[1].split(": ")[1])
                heading = int(float(parts[2].split(": ")[1]))
                correct = parts[3].split(": ")[1]

            q = f"Interpret the attitude indicator and compass."
            questions.append(f"{q}\nOptions: {', '.join(options)}")
            answers.append(correct)  # 'A', 'B', 'C', or 'D'
            data.append(i)  # Index to reference images
        except FileNotFoundError:
            print(f"Question file images/instrument/question_{i}.txt not found. Please run generate_instrument_images.py first.")
            continue

    return questions, answers, data