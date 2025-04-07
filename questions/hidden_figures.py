# questions/hidden_figures.py
import random

def generate_hidden_figures_questions():
    questions, answers, data = [], [], []
    shapes = ["triangle", "circle", "star", "square", "hexagon", "pentagon", "diamond", "octagon"]
    problems = []
    for i in range(50):
        hidden_shape = random.choice(shapes)
        question = f"A {hidden_shape} is hidden in a complex pattern. Which option matches the hidden shape?"
        correct_answer = hidden_shape
        incorrect_options = random.sample([s for s in shapes if s != hidden_shape], 3)
        options = [correct_answer] + incorrect_options
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