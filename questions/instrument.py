# questions/instrument.py
import random

def generate_instrument_comprehension_questions():
    questions, answers, data = [], [], []

    horizon_readings = [
        ("level flight, no bank", "level", 0),
        ("banked 30 degrees to the right", "right_30", 30),
        ("banked 30 degrees to the left", "left_30", -30),
        ("climbing 10 degrees, no bank", "climb_10", 0),
        ("descending 10 degrees, no bank", "descend_10", 0),
        ("climbing 20 degrees, banked 15 degrees to the right", "climb_20_right_15", 15),
        ("descending 20 degrees, banked 15 degrees to the left", "descend_20_left_15", -15),
        ("level flight, banked 45 degrees to the right", "level_right_45", 45),
        ("level flight, banked 45 degrees to the left", "level_left_45", -45),
        ("climbing 5 degrees, banked 10 degrees to the right", "climb_5_right_10", 10),
    ]
    compass_readings = [
        ("heading 0 degrees (North)", 0),
        ("heading 90 degrees (East)", 90),
        ("heading 180 degrees (South)", 180),
        ("heading 270 degrees (West)", 270),
        ("heading 45 degrees (Northeast)", 45),
        ("heading 135 degrees (Southeast)", 135),
        ("heading 225 degrees (Southwest)", 225),
        ("heading 315 degrees (Northwest)", 315),
    ]

    problems = []
    for i, (horizon_desc, horizon_code, bank_angle) in enumerate(horizon_readings * 5):
        compass_desc, heading = compass_readings[i % len(compass_readings)]
        correct_answer = f"Aircraft is {horizon_desc}, heading {heading} degrees."
        if "level" in horizon_code:
            pitch = 0
        elif "climb_20" in horizon_code:
            pitch = 20
        elif "descend_20" in horizon_code:
            pitch = -20
        elif "climb_5" in horizon_code:
            pitch = 5
        elif "climb" in horizon_code:
            pitch = 10
        else:  # descend
            pitch = -10

        incorrect_options = [
            f"Aircraft is level flight, no bank, heading {(heading + 90) % 360} degrees.",
            f"Aircraft is banked 30 degrees to the {'left' if bank_angle >= 0 else 'right'}, heading {(heading + 180) % 360} degrees.",
            f"Aircraft is {'descending' if 'climb' in horizon_code else 'climbing'} 10 degrees, no bank, heading {(heading + 270) % 360} degrees.",
            f"Aircraft is banked 30 degrees to the {'right' if bank_angle <= 0 else 'left'}, heading {heading} degrees."
        ]
        incorrect_options = random.sample([opt for opt in incorrect_options if opt != correct_answer], 3)
        options = [correct_answer] + incorrect_options
        random.shuffle(options)

        option_labels = ["A", "B", "C", "D"]
        labeled_options = [f"{label}: {value}" for label, value in zip(option_labels, options)]
        correct_index = options.index(correct_answer)
        correct_label = option_labels[correct_index]

        question = f"Instrument Readings:\nHorizon Indicator: {horizon_desc}\nCompass: {compass_desc}\nWhat is the aircraft's orientation?\nOptions:\n" + "\n".join(labeled_options)
        problems.append((question, correct_label, {
            "horizon": horizon_code,
            "compass": heading,
            "pitch": pitch,
            "bank": bank_angle,
            "correct_answer": correct_answer,
            "image_id": i
        }))

    while len(problems) < 50:
        horizon_desc, horizon_code, bank_angle = random.choice(horizon_readings)
        compass_desc, heading = random.choice(compass_readings)
        correct_answer = f"Aircraft is {horizon_desc}, heading {heading} degrees."
        if "level" in horizon_code:
            pitch = 0
        elif "climb_20" in horizon_code:
            pitch = 20
        elif "descend_20" in horizon_code:
            pitch = -20
        elif "climb_5" in horizon_code:
            pitch = 5
        elif "climb" in horizon_code:
            pitch = 10
        else:  # descend
            pitch = -10

        incorrect_options = [
            f"Aircraft is level flight, no bank, heading {(heading + 90) % 360} degrees.",
            f"Aircraft is banked 30 degrees to the {'left' if bank_angle >= 0 else 'right'}, heading {(heading + 180) % 360} degrees.",
            f"Aircraft is {'descending' if 'climb' in horizon_code else 'climbing'} 10 degrees, no bank, heading {(heading + 270) % 360} degrees.",
            f"Aircraft is banked 30 degrees to the {'right' if bank_angle <= 0 else 'left'}, heading {heading} degrees."
        ]
        incorrect_options = random.sample([opt for opt in incorrect_options if opt != correct_answer], 3)
        options = [correct_answer] + incorrect_options
        random.shuffle(options)

        option_labels = ["A", "B", "C", "D"]
        labeled_options = [f"{label}: {value}" for label, value in zip(option_labels, options)]
        correct_index = options.index(correct_answer)
        correct_label = option_labels[correct_index]

        question = f"Instrument Readings:\nHorizon Indicator: {horizon_desc}\nCompass: {compass_desc}\nWhat is the aircraft's orientation?\nOptions:\n" + "\n".join(labeled_options)
        problems.append((question, correct_label, {
            "horizon": horizon_code,
            "compass": heading,
            "pitch": pitch,
            "bank": bank_angle,
            "correct_answer": correct_answer,
            "image_id": len(problems)
        }))

    for question, correct_label, problem_data in problems:
        questions.append(question)
        answers.append(correct_label)
        data.append(problem_data)

    return questions, answers, data