# questions/verbal_analogies.py
import random

def generate_verbal_analogies_questions():
    questions, answers, data = [], [], []
    problems = [
        ("Big is to small as tall is to:", ["Short", "High", "Wide", "Long"], "Short"),
        ("Fast is to slow as big is to:", ["Large", "Tiny", "Huge", "Great"], "Tiny"),
        ("Dog is to puppy as cat is to:", ["Kitten", "Cub", "Chick", "Foal"], "Kitten"),
        ("Hot is to cold as light is to:", ["Bright", "Dark", "Heavy", "Warm"], "Dark"),
        ("Teacher is to student as doctor is to:", ["Nurse", "Patient", "Hospital", "Medicine"], "Patient"),
        ("Pen is to write as knife is to:", ["Cut", "Draw", "Paint", "Read"], "Cut"),
        ("Bird is to wing as fish is to:", ["Fin", "Tail", "Scale", "Gills"], "Fin"),
        ("Day is to night as summer is to:", ["Spring", "Winter", "Fall", "Morning"], "Winter"),
        ("Car is to road as boat is to:", ["Sky", "Water", "Dock", "Garage"], "Water"),
        ("Book is to read as song is to:", ["Sing", "Write", "Play", "Dance"], "Sing"),
        ("Happy is to sad as big is to:", ["Tall", "Small", "Wide", "Long"], "Small"),
        ("Shoe is to foot as glove is to:", ["Hand", "Arm", "Head", "Leg"], "Hand"),
        ("Sun is to day as moon is to:", ["Morning", "Night", "Evening", "Dawn"], "Night"),
        ("Tree is to forest as star is to:", ["Sky", "Galaxy", "Planet", "Moon"], "Galaxy"),
        ("Clock is to time as thermometer is to:", ["Temperature", "Weather", "Heat", "Pressure"], "Temperature"),
        # Add more to reach 50
        ("Rain is to umbrella as sun is to:", ["Sunglasses", "Raincoat", "Boots", "Scarf"], "Sunglasses"),
        ("Father is to son as mother is to:", ["Daughter", "Brother", "Sister", "Uncle"], "Daughter"),
        ("Square is to four as triangle is to:", ["Three", "Five", "Six", "Two"], "Three"),
        ("Loud is to quiet as bright is to:", ["Dim", "Shiny", "Colorful", "Dark"], "Dim"),
        ("Pilot is to airplane as captain is to:", ["Ship", "Car", "Train", "Bus"], "Ship"),
        # Continue adding until you have 50 unique problems
    ]

    # Ensure at least 50 questions
    while len(problems) < 50:
        problems.append(
            (f"Word{len(problems)} is to opposite{len(problems)} as up is to:", ["Down", "Left", "Right", "Side"], "Down")
        )

    # Format the questions
    for question, options, correct_answer in problems:
        option_labels = ["A", "B", "C", "D"]
        # Format options with labels (e.g., "A: Short")
        labeled_options = [f"{label}: {value}" for label, value in zip(option_labels, options)]
        # Find the index of the correct answer in the options list
        correct_index = options.index(correct_answer)
        # Get the corresponding label (e.g., "A")
        correct_label = option_labels[correct_index]
        # Create the formatted question
        formatted_question = f"{question}\nOptions:\n" + "\n".join(labeled_options)
        questions.append(formatted_question)
        answers.append(correct_label)
        data.append({"question": question, "options": options, "answer": correct_answer})

    return questions, answers, data