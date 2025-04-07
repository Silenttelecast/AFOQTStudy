# questions/block_counting.py
import random

def generate_block_counting_questions():
    questions, answers, data = [], [], []
    problems = []
    for i in range(50):
        num_blocks = random.randint(5, 15)
        question = f"A 3D block structure is shown with {num_blocks} blocks. How many blocks are in the structure?"
        correct_answer = str(num_blocks)
        incorrect_options = set()
        while len(incorrect_options) < 3:
            val = random.randint(5, 15)
            if val != num_blocks:
                incorrect_options.add(str(val))
        options = [correct_answer] + list(incorrect_options)
        random.shuffle(options)
        option_labels = ["A", "B", "C", "D"]
        labeled_options = [f"{label}: {value}" for label, value in zip(option_labels, options)]
        correct_index = options.index(correct_answer)
        correct_label = option_labels[correct_index]
        formatted_question = f"{question}\nOptions:\n" + "\n".join(labeled_options)
        problems.append((formatted_question, correct_label, {
            "question": question,
            "options": options,
            "answer": correct_answer
        }))

    for question, correct_label, problem_data in problems:
        questions.append(question)
        answers.append(correct_label)
        data.append(problem_data)

    return questions, answers, data