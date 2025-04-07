# questions/rotated_blocks.py
import random

def generate_rotated_blocks_questions():
    questions, answers, data = [], [], []

    block_structures = [
        {"description": "A 2x2x2 cube structure (8 cubes total).", "base": "2x2x2 cube"},
        {"description": "A 3x1x2 structure (6 cubes total).", "base": "3x1x2 structure"},
        {"description": "A 2x2x3 structure (12 cubes total).", "base": "2x2x3 structure"},
        {"description": "A 1x3x3 structure (9 cubes total).", "base": "1x3x3 structure"},
        {"description": "A 2x3x2 structure (12 cubes total).", "base": "2x3x2 structure"},
    ]

    rotations = [
        ("rotated 90 degrees clockwise around the vertical axis", "90CW"),
        ("rotated 90 degrees counterclockwise around the vertical axis", "90CCW"),
        ("rotated 180 degrees around the vertical axis", "180"),
        ("rotated 90 degrees clockwise around the horizontal axis (front to top)", "90H"),
        ("rotated 90 degrees counterclockwise around the horizontal axis (top to front)", "90HC")
    ]

    problems = []
    for i in range(50):
        structure = random.choice(block_structures)
        rotation_desc, rotation_code = random.choice(rotations)

        if structure["base"] == "2x2x2 cube":
            if rotation_code == "90CW":
                correct_answer = "The front face now shows 4 cubes (2x2), and the right face shows 4 cubes (2x2)."
            elif rotation_code == "90CCW":
                correct_answer = "The front face now shows 4 cubes (2x2), and the left face shows 4 cubes (2x2)."
            elif rotation_code == "180":
                correct_answer = "The front face now shows 4 cubes (2x2), and the back face is now in front."
            elif rotation_code == "90H":
                correct_answer = "The front face now shows 4 cubes (2x2), and the top face is now in front."
            else:  # 90HC
                correct_answer = "The front face now shows 4 cubes (2x2), and the bottom face is now in front."
        elif structure["base"] == "3x1x2 structure":
            if rotation_code == "90CW":
                correct_answer = "The front face now shows 2 cubes (1x2), and the right face shows 6 cubes (3x2)."
            elif rotation_code == "90CCW":
                correct_answer = "The front face now shows 2 cubes (1x2), and the left face shows 6 cubes (3x2)."
            elif rotation_code == "180":
                correct_answer = "The front face now shows 2 cubes (1x2), and the back face is now in front."
            elif rotation_code == "90H":
                correct_answer = "The front face now shows 3 cubes (3x1), and the top face is now in front."
            else:  # 90HC
                correct_answer = "The front face now shows 3 cubes (3x1), and the bottom face is now in front."
        elif structure["base"] == "2x2x3 structure":
            if rotation_code == "90CW":
                correct_answer = "The front face now shows 6 cubes (2x3), and the right face shows 6 cubes (2x3)."
            elif rotation_code == "90CCW":
                correct_answer = "The front face now shows 6 cubes (2x3), and the left face shows 6 cubes (2x3)."
            elif rotation_code == "180":
                correct_answer = "The front face now shows 6 cubes (2x3), and the back face is now in front."
            elif rotation_code == "90H":
                correct_answer = "The front face now shows 4 cubes (2x2), and the top face is now in front."
            else:  # 90HC
                correct_answer = "The front face now shows 4 cubes (2x2), and the bottom face is now in front."
        elif structure["base"] == "1x3x3 structure":
            if rotation_code == "90CW":
                correct_answer = "The front face now shows 9 cubes (3x3), and the right face shows 3 cubes (1x3)."
            elif rotation_code == "90CCW":
                correct_answer = "The front face now shows 9 cubes (3x3), and the left face shows 3 cubes (1x3)."
            elif rotation_code == "180":
                correct_answer = "The front face now shows 9 cubes (3x3), and the back face is now in front."
            elif rotation_code == "90H":
                correct_answer = "The front face now shows 3 cubes (1x3), and the top face is now in front."
            else:  # 90HC
                correct_answer = "The front face now shows 3 cubes (1x3), and the bottom face is now in front."
        else:  # 2x3x2 structure
            if rotation_code == "90CW":
                correct_answer = "The front face now shows 6 cubes (3x2), and the right face shows 4 cubes (2x2)."
            elif rotation_code == "90CCW":
                correct_answer = "The front face now shows 6 cubes (3x2), and the left face shows 4 cubes (2x2)."
            elif rotation_code == "180":
                correct_answer = "The front face now shows 6 cubes (3x2), and the back face is now in front."
            elif rotation_code == "90H":
                correct_answer = "The front face now shows 6 cubes (2x3), and the top face is now in front."
            else:  # 90HC
                correct_answer = "The front face now shows 6 cubes (2x3), and the bottom face is now in front."

        incorrect_options = [
            "The front face now shows 2 cubes (1x2), and the top face shows 4 cubes (2x2).",
            "The front face now shows 3 cubes (3x1), and the right face shows 2 cubes (1x2).",
            "The front face now shows 4 cubes (2x2), and the left face shows 3 cubes (3x1).",
            "The front face now shows 6 cubes (3x2), and the bottom face shows 2 cubes (1x2)."
        ]
        incorrect_options = random.sample([opt for opt in incorrect_options if opt != correct_answer], 3)
        options = [correct_answer] + incorrect_options
        random.shuffle(options)

        option_labels = ["A", "B", "C", "D"]
        labeled_options = [f"{label}: {value}" for label, value in zip(option_labels, options)]
        correct_index = options.index(correct_answer)
        correct_label = option_labels[correct_index]

        question = f"Block Structure: {structure['description']}\nThe structure is {rotation_desc}.\nWhat does the structure look like now?\nOptions:\n" + "\n".join(labeled_options)
        problems.append((question, correct_label, {
            "structure": structure["description"],
            "rotation": rotation_desc,
            "correct_answer": correct_answer
        }))

    for question, correct_label, problem_data in problems:
        questions.append(question)
        answers.append(correct_label)
        data.append(problem_data)

    return questions, answers, data