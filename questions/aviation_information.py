# questions/aviation_information.py
import random

def generate_aviation_information_questions():
    questions, answers, data = [], [], []
    problems = [
        ("What is the primary source of lift for an airplane?", ["A: Engine thrust", "B: Wing shape", "C: Tail rudder", "D: Landing gear"], "B"),
        ("What instrument indicates an aircraft's altitude?", ["A: Altimeter", "B: Airspeed indicator", "C: Compass", "D: Turn coordinator"], "A"),
        ("What does the term 'yaw' refer to?", ["A: Up and down movement", "B: Side-to-side movement", "C: Forward movement", "D: Roll movement"], "B"),
        ("What is the purpose of ailerons on an airplane?", ["A: Control pitch", "B: Control roll", "C: Control yaw", "D: Increase speed"], "B"),
        ("What does the acronym VFR stand for in aviation?", ["A: Visual Flight Rules", "B: Variable Flight Range", "C: Vertical Flight Rate", "D: Visual Frequency Radar"], "A"),
        ("What is the function of the rudder on an airplane?", ["A: Control roll", "B: Control yaw", "C: Control pitch", "D: Increase lift"], "B"),
        ("What does the term 'stall' mean in aviation?", ["A: Engine failure", "B: Loss of lift due to excessive angle of attack", "C: Sudden descent", "D: Loss of fuel"], "B"),
        ("What is the purpose of flaps on an airplane?", ["A: Increase speed", "B: Increase lift and drag for takeoff/landing", "C: Control yaw", "D: Reduce weight"], "B"),
        ("What does IFR stand for in aviation?", ["A: Instrument Flight Rules", "B: International Flight Range", "C: Internal Flight Recorder", "D: Instrument Frequency Radar"], "A"),
        ("What is the primary function of the elevator on an airplane?", ["A: Control roll", "B: Control yaw", "C: Control pitch", "D: Increase speed"], "C")
    ]

    # Generate 40 questions by sampling from the problem set
    selected_problems = random.sample(problems, min(40, len(problems)))
    for question, options, correct_answer in selected_problems:
        # Format the options as A, B, C, D
        option_labels = ["A", "B", "C", "D"]
        labeled_options = [f"{label}: {value}" for label, value in zip(option_labels, options)]
        correct_label = option_labels[options.index(correct_answer)]

        # Create the question
        formatted_question = f"{question}\nOptions:\n" + "\n".join(labeled_options)

        questions.append(formatted_question)
        answers.append(correct_label)
        data.append({
            "question": question,
            "options": options,
            "answer": correct_answer
        })

    return questions, answers, data