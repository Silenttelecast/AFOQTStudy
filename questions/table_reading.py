# questions/table_reading.py
import random
import numpy as np

def generate_table_reading_questions():
    # Generate 5 different 7x7 tables with values between 10 and 99
    tables = [np.random.randint(10, 100, (7, 7)) for _ in range(5)]
    x_vals = [-3, -2, -1, 0, 1, 2, 3]
    y_vals = [-3, -2, -1, 0, 1, 2, 3]
    questions, answers, data_list = [], [], []
    seen = set()

    while len(questions) < 50:
        table = random.choice(tables)
        x, y = random.choice(x_vals), random.choice(y_vals)
        correct_answer = table[y_vals.index(y), x_vals.index(x)]

        # Generate 3 incorrect options, ensuring they are unique and different from the correct answer
        incorrect_options = set()
        while len(incorrect_options) < 3:
            val = random.randint(10, 100)
            if val != correct_answer:
                incorrect_options.add(val)
        options = [correct_answer] + list(incorrect_options)
        random.shuffle(options)

        # Format the options as A, B, C, D
        option_labels = ["A", "B", "C", "D"]
        labeled_options = [f"{label}: {value}" for label, value in zip(option_labels, options)]
        correct_label = option_labels[options.index(correct_answer)]

        # Format the table as a string for display
        table_str = "  X | " + " ".join(f"{x:3}" for x in x_vals) + "\n"
        table_str += "----+" + "----" * len(x_vals) + "\n"
        for i, y_val in enumerate(y_vals):
            table_str += f"{y_val:3} | " + " ".join(f"{val:3}" for val in table[i]) + "\n"

        # Create the question
        question = f"Table:\n{table_str}\nWhat is the value at X={x}, Y={y}?\nOptions:\n" + "\n".join(labeled_options)

        if question not in seen:
            seen.add(question)
            questions.append(question)
            answers.append(correct_label)
            data_list.append({
                "table": table,
                "x_vals": x_vals,
                "y_vals": y_vals,
                "x": x,
                "y": y,
                "correct_answer": correct_answer
            })

    return questions[:40], answers[:40], data_list[:40]