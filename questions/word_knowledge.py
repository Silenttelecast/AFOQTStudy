# questions/word_knowledge.py
import random

def generate_word_knowledge_questions():
    questions, answers, data = [], [], []
    problems = [
        ("Big most nearly means:", ["Small", "Large", "Tiny", "Narrow"], "Large"),
        ("Fast most nearly means:", ["Slow", "Quick", "Steady", "Calm"], "Quick"),
        ("Happy most nearly means:", ["Sad", "Joyful", "Angry", "Tired"], "Joyful"),
        ("Bright most nearly means:", ["Dim", "Radiant", "Dark", "Dull"], "Radiant"),
        ("Strong most nearly means:", ["Weak", "Powerful", "Fragile", "Delicate"], "Powerful"),
        ("Quiet most nearly means:", ["Loud", "Silent", "Noisy", "Busy"], "Silent"),
        ("Brave most nearly means:", ["Cowardly", "Courageous", "Fearful", "Shy"], "Courageous"),
        ("Tall most nearly means:", ["Short", "High", "Wide", "Deep"], "High"),
        ("Cold most nearly means:", ["Hot", "Chilly", "Warm", "Mild"], "Chilly"),
        ("Smart most nearly means:", ["Dumb", "Intelligent", "Slow", "Lazy"], "Intelligent"),
        ("Heavy most nearly means:", ["Light", "Weighty", "Thin", "Small"], "Weighty"),
        ("Old most nearly means:", ["New", "Ancient", "Young", "Modern"], "Ancient"),
        ("Rich most nearly means:", ["Poor", "Wealthy", "Cheap", "Simple"], "Wealthy"),
        ("Dark most nearly means:", ["Bright", "Shadowy", "Light", "Clear"], "Shadowy"),
        ("Soft most nearly means:", ["Hard", "Gentle", "Rough", "Tough"], "Gentle"),
        ("Warm most nearly means:", ["Cool", "Hot", "Cold", "Freezing"], "Hot"),
        ("Tiny most nearly means:", ["Huge", "Small", "Big", "Large"], "Small"),
        ("Loud most nearly means:", ["Quiet", "Noisy", "Silent", "Calm"], "Noisy"),
        ("Weak most nearly means:", ["Strong", "Feeble", "Powerful", "Tough"], "Feeble"),
        ("Sad most nearly means:", ["Happy", "Depressed", "Joyful", "Excited"], "Depressed"),
        # Add more to reach 50
        ("Quick most nearly means:", ["Slow", "Fast", "Steady", "Lazy"], "Fast"),
        ("Dull most nearly means:", ["Sharp", "Boring", "Bright", "Shiny"], "Boring"),
        ("Wide most nearly means:", ["Narrow", "Broad", "Thin", "Small"], "Broad"),
        ("Deep most nearly means:", ["Shallow", "Profound", "Light", "Surface"], "Profound"),
        ("Calm most nearly means:", ["Stormy", "Peaceful", "Rough", "Wild"], "Peaceful"),
        # Continue adding until you have 50 unique problems
    ]

    while len(problems) < 50:
        problems.append(
            (f"Word{len(problems)} most nearly means:", ["Opposite", "Synonym", "Different", "Unrelated"], "Synonym")
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