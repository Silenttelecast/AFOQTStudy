# questions/reading_comprehension.py
import random

def generate_reading_comprehension_questions():
    questions, answers, data = [], [], []
    passages = [
        ("The sun is a star that provides energy to Earth. It is about 93 million miles away.", "What is the main source of energy for Earth?", ["A: The moon", "B: The sun", "C: The stars", "D: The ocean"], "B"),
        ("Birds migrate to warmer climates during winter to find food.", "Why do birds migrate in winter?", ["A: To find mates", "B: To find food", "C: To build nests", "D: To avoid rain"], "B"),
        ("Water covers about 71% of Earth's surface, mostly in oceans.", "What percentage of Earth's surface is covered by water?", ["A: 50%", "B: 60%", "C: 71%", "D: 80%"], "C"),
        ("Plants use sunlight to make their own food through photosynthesis.", "How do plants make their food?", ["A: Through digestion", "B: Through photosynthesis", "C: Through respiration", "D: Through absorption"], "B"),
        ("The moon affects the tides on Earth due to its gravitational pull.", "What causes the tides on Earth?", ["A: The sun", "B: The moon", "C: The wind", "D: The clouds"], "B")
    ]
    for passage, question, options, answer in random.sample(passages, len(passages)):
        questions.append(f"Passage: {passage}\nQuestion: {question}")
        answers.append(options)
        data.append({"passage": passage, "question": question, "options": options, "answer": answer})
    return questions, answers, data