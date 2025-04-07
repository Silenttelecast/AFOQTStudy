# questions/table_reading.py
import random
import numpy as np

def generate_table_reading_questions():
    tables = [np.random.randint(10, 100, (7, 7)) for _ in range(10)]
    x_vals = [-3, -2, -1, 0, 1, 2, 3]
    y_vals = [-3, -2, -1, 0, 1, 2, 3]
    questions, answers, data_list = [], [], []
    seen = set()

    while len(questions) < 50:
        table = random.choice(tables)
        x, y = random.choice(x_vals), random.choice(y_vals)
        correct_answer = str(table[y_vals.index(y), x_vals.index(x)])

        incorrect_options = set()
        while len(incorrect_options) < 3:
            val = random.randint(10, 100)
            if val != int(correct_answer):
                incorrect_options.add(str(val))
        options = [correct_answer] + list(incorrect_options)
        random.shuffle(options)

        option_labels = ["A", "B", "C", "D"]
        labeled_options = [f"{label}: {value}" for label, value in zip(option_labels, options)]
        correct_index = options.index(correct_answer)
        correct_label = option_labels[correct_index]

        table_str = "  X | " + " ".join(f"{x:3}" for x in x_vals) + "\n"
        table_str += "----+" + "----" * len(x_vals) + "\n"
        for i, y_val in enumerate(y_vals):
            table_str += f"{y_val:3} | " + " ".join(f"{val:3}" for val in table[i]) + "\n"

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

    return questions, answers, data_list