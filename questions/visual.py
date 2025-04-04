# questions/visual.py
import random
import numpy as np

def generate_instrument_questions():
    questions, answers, data_list = [], [], []
    seen = set()
    while len(questions) < 50:
        climb = random.uniform(-0.5, 0.5)
        bank = random.uniform(-45, 45)
        heading = random.uniform(0, 360)
        opts = ["A", "B", "C", "D"]
        correct = random.choice(opts)
        q = f"Which aircraft matches: {'climb' if climb > 0 else 'dive'}, {'right' if bank > 0 else 'left'} bank, heading {int(heading)}°?\nOptions: {', '.join(opts)}"
        if q not in seen:
            seen.add(q)
            questions.append(q)
            answers.append(correct)
            data_list.append({"climb": climb, "bank": bank, "heading": heading})
    return questions[:25], answers[:25], random.choice(data_list)

def generate_block_counting_questions():
    questions, answers, data_list = [], [], []
    for _ in range(50):
        blocks = [(x, y, z) for x in range(3) for y in range(3) for z in range(3) if random.random() > 0.3]
        numbered = random.choice(blocks)
        touching = sum(1 for (x, y, z) in blocks if 
                       abs(x - numbered[0]) + abs(y - numbered[1]) + abs(z - numbered[2]) == 1)
        opts = sorted(list(set([touching] + [random.randint(0, 6) for _ in range(4)])))
        q = f"How many blocks touch Block 1?\nOptions: {', '.join(map(str, opts))}"
        questions.append(q)
        answers.append(str(touching))
        data_list.append({"blocks": blocks, "numbered": numbered})
    return questions[:30], answers[:30], random.choice(data_list)

def generate_rotated_blocks_questions():
    shapes = [
        [(0, 0), (0, 1), (0, 2), (1, 2)],  # L-shape
        [(0, 0), (1, 0), (1, 1), (2, 1)],  # Z-shape
        [(0, 0), (0, 1), (1, 0), (1, 1)]   # Square
    ]
    rotations = [0, 90, 180, 270]
    questions, answers, data_list = [], [], []
    for _ in range(50):
        original = random.choice(shapes)
        correct_rotation = random.choice(rotations)
        opts = ["A", "B", "C", "D"]
        correct = opts[rotations.index(correct_rotation)]
        rotated_options = [
            [(x * np.cos(np.radians(angle)) - y * np.sin(np.radians(angle)),
              x * np.sin(np.radians(angle)) + y * np.cos(np.radians(angle)))
             for x, y in original] for angle in rotations
        ]
        q = "Which block matches the original after rotation?\nOptions: A, B, C, D"
        questions.append(q)
        answers.append(correct)
        data_list.append({"original": original, "options": rotated_options})
    return questions[:15], answers[:15], random.choice(data_list)

def generate_hidden_figures_questions():
    figures = {
        "A": [(0, 0), (1, 0), (1, 1), (0, 1)],
        "B": [(0, 0), (1, 1), (0, 1)],
        "C": [(0, 0), (1, 0), (0.5, 1)],
        "D": [(0, 0), (1, 0)],
        "E": [(0, 0), (0, 1)]
    }
    questions, answers, data_list = [], [], []
    for _ in range(50):
        correct_figure = random.choice(list(figures.keys()))
        complex_coords = [(random.uniform(-1, 2), random.uniform(-1, 2)) for _ in range(10)]
        complex_coords.extend(figures[correct_figure])
        q = "Which figure is hidden in the complex drawing?\nOptions: A, B, C, D, E"
        questions.append(q)
        answers.append(correct_figure)
        data_list.append({"figures": figures, "complex": complex_coords})
    return questions[:15], answers[:15], random.choice(data_list)