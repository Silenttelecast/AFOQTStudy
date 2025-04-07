# questions/arithmetic_reasoning.py
import random

def generate_arithmetic_reasoning_questions():
    questions, answers, data = [], [], []
    problems = [
        ("If a car travels 240 miles in 4 hours, what is its average speed in miles per hour?", ["40", "50", "60", "70"], "60"),
        ("A shirt costs $20 after a 20% discount. What was the original price?", ["24", "25", "26", "28"], "25"),
        ("If 3 workers can build a wall in 6 days, how many days will it take 2 workers?", ["7", "8", "9", "10"], "9"),
        ("A recipe for 4 people requires 2 cups of flour. How many cups are needed for 6 people?", ["2.5", "3", "3.5", "4"], "3"),
        ("If a train travels 150 miles in 2.5 hours, what is its speed in miles per hour?", ["50", "60", "70", "80"], "60"),
        ("A book costs $15 after a 25% discount. What was the original price?", ["18", "20", "22", "25"], "20"),
        ("If 5 machines produce 500 units in 10 hours, how many units will 2 machines produce in 5 hours?", ["50", "100", "150", "200"], "100"),
        ("A plane flies 600 miles in 2 hours. What is its speed in miles per hour?", ["200", "250", "300", "350"], "300"),
        ("A store offers a 15% discount on a $40 item. What is the sale price?", ["32", "34", "36", "38"], "34"),
        ("If 4 painters can paint a house in 8 days, how many days will it take 2 painters?", ["12", "14", "16", "18"], "16"),
        ("A car rental costs $30 per day plus $0.20 per mile. If you drive 50 miles in one day, what is the total cost?", ["35", "40", "45", "50"], "40"),
        ("If a box contains 12 apples and you take 25% of them, how many apples do you take?", ["2", "3", "4", "5"], "3"),
        ("A train travels 300 miles in 5 hours. What is its average speed?", ["50 mph", "60 mph", "70 mph", "80 mph"], "60 mph"),
        ("A jacket costs $50 after a 10% discount. What was the original price?", ["55", "60", "65", "70"], "55"),
        ("If 6 workers can complete a project in 12 days, how many days will it take 3 workers?", ["18", "20", "24", "28"], "24"),
        # Add more to reach 50
        ("A bus travels 180 miles in 3 hours. What is its speed?", ["50 mph", "60 mph", "70 mph", "80 mph"], "60 mph"),
        ("A coat costs $80 after a 20% discount. What was the original price?", ["90", "100", "110", "120"], "100"),
        ("If 2 workers can build a fence in 5 days, how many days will it take 4 workers?", ["2", "2.5", "3", "3.5"], "2.5"),
        ("A recipe for 5 people requires 3 cups of sugar. How many cups are needed for 10 people?", ["4", "5", "6", "7"], "6"),
        ("A plane travels 400 miles in 2 hours. What is its speed?", ["150 mph", "200 mph", "250 mph", "300 mph"], "200 mph"),
        # Continue adding until you have 50 unique problems
    ]

    while len(problems) < 50:
        problems.append(
            (f"A car travels {len(problems) * 10} miles in 2 hours. What is its speed?", [f"{len(problems) * 5 - 10}", f"{len(problems) * 5}", f"{len(problems) * 5 + 10}", f"{len(problems) * 5 + 20}"], f"{len(problems) * 5}")
        )

    for question, options, correct_answer in problems:
        option_labels = ["A", "B", "C", "D"]
        labeled_options = [f"{label}: {value}" for label, value in zip(option_labels, options)]
        correct_index = options.index(correct_answer)
        correct_label = option_labels[correct_index]
        formatted_question = f"{question}\nOptions:\n" + "\n".join(labeled_options)
        questions.append(formatted_question)
        answers.append(correct_label)
        data.append({"question": question, "options": options, "answer": correct_answer})

    return questions, answers, data