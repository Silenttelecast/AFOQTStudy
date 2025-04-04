# questions/table.py
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
        a = table[y_vals.index(y), x_vals.index(x)]
        opts = sorted(list(set([a] + [random.randint(10, 100) for _ in range(4)])))
        q = f"What is the value at X={x}, Y={y}?\nOptions: {', '.join(map(str, opts))}"
        if q not in seen:
            seen.add(q)
            questions.append(q)
            answers.append(str(a))
            data_list.append({"table": table, "x_vals": x_vals, "y_vals": y_vals})
    return questions[:40], answers[:40], random.choice(data_list)