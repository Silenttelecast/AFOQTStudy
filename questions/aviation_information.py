# questions/aviation_information.py
import random

def generate_aviation_information_questions():
    questions, answers, data = [], [], []
    problems = [
        ("What is the primary source of lift for an airplane?", ["Engine thrust", "Wing shape", "Tail rudder", "Landing gear"], "Wing shape"),
        ("What instrument indicates an aircraft's altitude?", ["Altimeter", "Airspeed indicator", "Compass", "Turn coordinator"], "Altimeter"),
        ("What does the term 'yaw' refer to?", ["Up and down movement", "Side-to-side movement", "Forward movement", "Roll movement"], "Side-to-side movement"),
        ("What is the purpose of ailerons on an airplane?", ["Control pitch", "Control roll", "Control yaw", "Increase speed"], "Control roll"),
        ("What does the acronym VFR stand for in aviation?", ["Visual Flight Rules", "Variable Flight Range", "Vertical Flight Rate", "Visual Frequency Radar"], "Visual Flight Rules"),
        ("What is the function of the rudder on an airplane?", ["Control roll", "Control yaw", "Control pitch", "Increase lift"], "Control yaw"),
        ("What does the term 'stall' mean in aviation?", ["Engine failure", "Loss of lift due to excessive angle of attack", "Sudden descent", "Loss of fuel"], "Loss of lift due to excessive angle of attack"),
        ("What is the purpose of flaps on an airplane?", ["Increase speed", "Increase lift and drag for takeoff/landing", "Control yaw", "Reduce weight"], "Increase lift and drag for takeoff/landing"),
        ("What does IFR stand for in aviation?", ["Instrument Flight Rules", "International Flight Range", "Internal Flight Recorder", "Instrument Frequency Radar"], "Instrument Flight Rules"),
        ("What is the primary function of the elevator on an airplane?", ["Control roll", "Control yaw", "Control pitch", "Increase speed"], "Control pitch"),
        ("What is the purpose of the altimeter?", ["Measure speed", "Measure altitude", "Measure direction", "Measure temperature"], "Measure altitude"),
        ("What does the term 'pitch' refer to?", ["Side-to-side movement", "Up and down movement", "Forward movement", "Roll movement"], "Up and down movement"),
        ("What is the function of the landing gear?", ["Control direction", "Support the aircraft during takeoff and landing", "Increase lift", "Control speed"], "Support the aircraft during takeoff and landing"),
        ("What does the acronym ATC stand for?", ["Air Traffic Control", "Aviation Training Center", "Aircraft Technical Command", "Air Transport Carrier"], "Air Traffic Control"),
        ("What is the purpose of the throttle in an aircraft?", ["Control direction", "Control engine power", "Control altitude", "Control roll"], "Control engine power"),
        ("What is the primary function of the propeller?", ["Control direction", "Provide thrust", "Control altitude", "Control roll"], "Provide thrust"),
        ("What does the term 'angle of attack' refer to?", ["The angle of the wings relative to the wind", "The angle of the aircraft's nose", "The angle of descent", "The angle of the tail"], "The angle of the wings relative to the wind"),
        ("What is the purpose of the pitot tube?", ["Measure airspeed", "Measure altitude", "Measure direction", "Measure temperature"], "Measure airspeed"),
        ("What does the acronym FAA stand for?", ["Federal Aviation Administration", "Flight Assessment Agency", "Federal Aircraft Association", "Flight Aviation Authority"], "Federal Aviation Administration"),
        ("What is the function of the vertical stabilizer?", ["Control roll", "Provide directional stability", "Control pitch", "Increase lift"], "Provide directional stability"),
        ("What instrument shows the aircraft's heading?", ["Altimeter", "Compass", "Airspeed indicator", "Turn coordinator"], "Compass"),
        ("What does the term 'roll' refer to?", ["Up and down movement", "Side-to-side movement", "Rotation around the longitudinal axis", "Forward movement"], "Rotation around the longitudinal axis"),
        ("What is the purpose of the trim tabs on an aircraft?", ["Increase speed", "Reduce pilot workload by adjusting control surfaces", "Control yaw", "Increase lift"], "Reduce pilot workload by adjusting control surfaces"),
        ("What does the acronym NOTAM stand for?", ["Notice to Airmen", "Navigation of Terrain and Mountains", "Notice of Technical Aviation Maintenance", "Navigation of Tactical Air Missions"], "Notice to Airmen"),
        ("What is the function of the horizontal stabilizer?", ["Control roll", "Provide pitch stability", "Control yaw", "Increase speed"], "Provide pitch stability"),
        # Add more to reach 50
        ("What does the term 'glide slope' refer to?", ["The aircraft's speed", "The path for a safe descent during landing", "The angle of climb", "The rate of turn"], "The path for a safe descent during landing"),
        ("What is the purpose of the airspeed indicator?", ["Measure altitude", "Measure speed through the air", "Measure direction", "Measure temperature"], "Measure speed through the air"),
        ("What does the acronym PAPI stand for?", ["Precision Approach Path Indicator", "Pilot Aviation Performance Index", "Primary Aircraft Position Indicator", "Precision Altitude Path Indicator"], "Precision Approach Path Indicator"),
        ("What is the function of the spoilers on an aircraft?", ["Increase lift", "Reduce lift and increase drag", "Control yaw", "Control pitch"], "Reduce lift and increase drag"),
        ("What does the term 'ceiling' refer to in aviation?", ["The height of the aircraft", "The height of the lowest cloud layer", "The maximum altitude of the aircraft", "The height of the runway"], "The height of the lowest cloud layer"),
        # Continue adding until you have 50 unique problems
    ]

    while len(problems) < 50:
        problems.append(
            (f"What does aviation term {len(problems)} mean?", ["Incorrect", "Correct", "Different", "Unrelated"], "Correct")
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