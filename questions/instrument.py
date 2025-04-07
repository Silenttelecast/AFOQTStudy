# questions/instrument.py
import random

def generate_instrument_comprehension_questions():
    questions, answers, data = [], [], []

    # Define possible instrument readings
    horizon_readings = [
        ("level flight, no bank", "level", 0),
        ("banked 30 degrees to the right", "right_30", 30),
        ("banked 30 degrees to the left", "left_30", -30),
        ("climbing 10 degrees, no bank", "climb_10", 0),
        ("descending 10 degrees, no bank", "descend_10", 0)
    ]
    compass_readings = [
        ("heading 0 degrees (North)", 0),
        ("heading 90 degrees (East)", 90),
        ("heading 180 degrees (South)", 180),
        ("heading 270 degrees (West)", 270)
    ]

    for i in range(40):  # Generate 40 questions
        horizon_desc, horizon_code, bank_angle = random.choice(horizon_readings)
        compass_desc, heading = random.choice(compass_readings)

        # Determine the correct aircraft orientation
        correct_answer = f"Aircraft is {horizon_desc}, heading {heading} degrees."
        if "level" in horizon_code:
            pitch = 0
        elif "climb" in horizon_code:
            pitch = 10
        else:  # descend
            pitch = -10

        # Generate incorrect options
        incorrect_options = [
            f"Aircraft is level flight, no bank, heading {(heading + 90) % 360} degrees.",
            f"Aircraft is banked 30 degrees to the {'left' if bank_angle >= 0 else 'right'}, heading {(heading + 180) % 360} degrees.",
            f"Aircraft is {'descending' if 'climb' in horizon_code else 'climbing'} 10 degrees, no bank, heading {(heading + 270) % 360} degrees.",
            f"Aircraft is banked 30 degrees to the {'right' if bank_angle <= 0 else 'left'}, heading {heading} degrees."
        ]
        incorrect_options = random.sample([opt for opt in incorrect_options if opt != correct_answer], 3)
        options = [correct_answer] + incorrect_options
        random.shuffle(options)

        # Format the options as A, B, C, D
        option_labels = ["A", "B", "C", "D"]
        labeled_options = [f"{label}: {value}" for label, value in zip(option_labels, options)]
        correct_label = option_labels[options.index(correct_answer)]

        # Create the question (image will be displayed in the GUI)
        question = f"Instrument Readings:\nHorizon Indicator: {horizon_desc}\nCompass: {compass_desc}\nWhat is the aircraft's orientation?\nOptions:\n" + "\n".join(labeled_options)

        questions.append(question)
        answers.append(correct_label)
        data.append({
            "horizon": horizon_code,
            "compass": heading,
            "pitch": pitch,
            "bank": bank_angle,
            "correct_answer": correct_answer,
            "image_id": i  # Assumes generate_instrument_images.py creates images with IDs 0 to 39
        })

    return questions, answers, data