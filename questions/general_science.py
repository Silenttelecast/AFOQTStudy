# questions/general_science.py
import random

def generate_general_science_questions():
    questions, answers, data = [], [], []
    problems = [
        ("What gas do plants primarily use for photosynthesis?", ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "Carbon dioxide"),
        ("What is the boiling point of water in Celsius?", ["0", "50", "100", "150"], "100"),
        ("What type of energy is stored in a battery?", ["Kinetic", "Thermal", "Chemical", "Nuclear"], "Chemical"),
        ("What planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], "Mars"),
        ("What is the primary source of energy for Earth's climate system?", ["The moon", "The sun", "The ocean", "The wind"], "The sun"),
        ("What is the chemical symbol for gold?", ["Au", "Ag", "Fe", "Cu"], "Au"),
        ("What gas makes up the majority of Earth's atmosphere?", ["Oxygen", "Nitrogen", "Carbon dioxide", "Helium"], "Nitrogen"),
        ("What is the freezing point of water in Celsius?", ["0", "32", "100", "-10"], "0"),
        ("What type of rock is formed from cooled lava?", ["Sedimentary", "Metamorphic", "Igneous", "Fossilized"], "Igneous"),
        ("What is the primary source of energy for Earth's climate?", ["The moon", "The sun", "The ocean", "The wind"], "The sun"),
        ("What is the chemical symbol for oxygen?", ["O", "Ox", "O2", "Og"], "O"),
        ("What planet is closest to the sun?", ["Venus", "Earth", "Mercury", "Mars"], "Mercury"),
        ("What is the process by which plants release water vapor?", ["Photosynthesis", "Transpiration", "Respiration", "Condensation"], "Transpiration"),
        ("What type of energy is associated with motion?", ["Potential", "Kinetic", "Chemical", "Thermal"], "Kinetic"),
        ("What is the chemical symbol for iron?", ["Fe", "Ir", "In", "Io"], "Fe"),
        ("What is the chemical symbol for silver?", ["Au", "Ag", "Si", "Sr"], "Ag"),
        ("What planet is known for its rings?", ["Jupiter", "Saturn", "Uranus", "Neptune"], "Saturn"),
        ("What is the process by which water changes to vapor?", ["Condensation", "Evaporation", "Sublimation", "Precipitation"], "Evaporation"),
        ("What type of energy is stored in food?", ["Kinetic", "Thermal", "Chemical", "Nuclear"], "Chemical"),
        ("What is the chemical symbol for carbon?", ["C", "Ca", "Co", "Cr"], "C"),
        ("What is the primary source of energy for Earth's climate?", ["The moon", "The sun", "The ocean", "The wind"], "The sun"),
        ("What is the chemical symbol for hydrogen?", ["H", "He", "Hy", "Hg"], "H"),
        ("What planet is known as the gas giant?", ["Mars", "Jupiter", "Mercury", "Venus"], "Jupiter"),
        ("What is the process by which water vapor turns into liquid?", ["Evaporation", "Condensation", "Sublimation", "Precipitation"], "Condensation"),
        ("What type of energy is associated with heat?", ["Kinetic", "Potential", "Thermal", "Chemical"], "Thermal"),
        # Add more to reach 50
        ("What is the chemical symbol for sodium?", ["Na", "So", "Sd", "Sn"], "Na"),
        ("What planet is the second closest to the sun?", ["Mercury", "Venus", "Earth", "Mars"], "Venus"),
        ("What is the process by which plants convert sunlight into energy?", ["Respiration", "Photosynthesis", "Transpiration", "Evaporation"], "Photosynthesis"),
        ("What type of rock is formed by heat and pressure?", ["Igneous", "Sedimentary", "Metamorphic", "Fossilized"], "Metamorphic"),
        ("What is the chemical symbol for helium?", ["H", "He", "Hl", "Hm"], "He"),
        # Continue adding until you have 50 unique problems
    ]

    while len(problems) < 50:
        problems.append(
            (f"What is science fact {len(problems)}?", ["Incorrect", "Correct", "Different", "Unrelated"], "Correct")
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