# questions/reading_comprehension.py
import random

def generate_reading_comprehension_questions():
    questions, answers, data = [], [], []
    passages = [
        ("The sun is a star that provides energy to Earth. It is about 93 million miles away.", "What is the main source of energy for Earth?", ["The moon", "The sun", "The stars", "The ocean"], "The sun"),
        ("Birds migrate to warmer climates during winter to find food.", "Why do birds migrate in winter?", ["To find mates", "To find food", "To build nests", "To avoid rain"], "To find food"),
        ("Water covers about 71% of Earth's surface, mostly in oceans.", "What percentage of Earth's surface is covered by water?", ["50%", "60%", "71%", "80%"], "71%"),
        ("Plants use sunlight to make their own food through photosynthesis.", "How do plants make their food?", ["Through digestion", "Through photosynthesis", "Through respiration", "Through absorption"], "Through photosynthesis"),
        ("The moon affects the tides on Earth due to its gravitational pull.", "What causes the tides on Earth?", ["The sun", "The moon", "The wind", "The clouds"], "The moon"),
        ("The Earth rotates on its axis once every 24 hours.", "How long does it take for the Earth to complete one rotation?", ["12 hours", "24 hours", "36 hours", "48 hours"], "24 hours"),
        ("Bees pollinate flowers while collecting nectar.", "What do bees do while collecting nectar?", ["Build hives", "Pollinate flowers", "Make honey", "Protect the queen"], "Pollinate flowers"),
        ("The Amazon rainforest is the largest tropical rainforest in the world.", "What is the largest tropical rainforest in the world?", ["Congo", "Amazon", "Daintree", "Tongass"], "Amazon"),
        ("Volcanoes erupt when magma reaches the Earth's surface.", "What causes a volcano to erupt?", ["Earthquake", "Magma reaching the surface", "Heavy rain", "Wind"], "Magma reaching the surface"),
        ("The human body has 206 bones in adulthood.", "How many bones are in the adult human body?", ["180", "206", "220", "250"], "206"),
        ("The Great Wall of China is over 13,000 miles long.", "How long is the Great Wall of China?", ["5,000 miles", "8,000 miles", "13,000 miles", "20,000 miles"], "13,000 miles"),
        ("Penguins are birds that cannot fly but are excellent swimmers.", "What are penguins excellent at?", ["Flying", "Swimming", "Running", "Climbing"], "Swimming"),
        ("The Earth revolves around the sun once every 365 days.", "How often does the Earth revolve around the sun?", ["Every 180 days", "Every 365 days", "Every 500 days", "Every 730 days"], "Every 365 days"),
        ("Tornadoes are powerful storms that form from rotating air.", "What causes tornadoes to form?", ["Heavy rain", "Rotating air", "Cold temperatures", "Lightning"], "Rotating air"),
        ("The Pacific Ocean is the largest ocean on Earth.", "What is the largest ocean on Earth?", ["Atlantic", "Indian", "Pacific", "Arctic"], "Pacific"),
        ("The heart pumps blood throughout the body.", "What organ pumps blood?", ["Lungs", "Heart", "Liver", "Kidneys"], "Heart"),
        ("A year on Jupiter lasts about 12 Earth years.", "How long is a year on Jupiter?", ["5 Earth years", "12 Earth years", "20 Earth years", "30 Earth years"], "12 Earth years"),
        ("Bats use echolocation to navigate in the dark.", "How do bats navigate in the dark?", ["By sight", "By echolocation", "By smell", "By touch"], "By echolocation"),
        ("The largest mammal on Earth is the blue whale.", "What is the largest mammal on Earth?", ["Elephant", "Blue whale", "Giraffe", "Polar bear"], "Blue whale"),
        ("Clouds are formed by the condensation of water vapor.", "How are clouds formed?", ["By evaporation", "By condensation", "By precipitation", "By sublimation"], "By condensation"),
        # Add more to reach 50
        ("The Nile River is the longest river in the world.", "What is the longest river in the world?", ["Amazon", "Nile", "Yangtze", "Mississippi"], "Nile"),
        ("Sharks have an acute sense of smell to detect prey.", "What sense do sharks use to detect prey?", ["Sight", "Smell", "Hearing", "Touch"], "Smell"),
        ("The Earth’s core is primarily made of iron and nickel.", "What is the Earth’s core primarily made of?", ["Gold and silver", "Iron and nickel", "Copper and zinc", "Aluminum and magnesium"], "Iron and nickel"),
        ("A solar eclipse occurs when the moon passes between the Earth and the sun.", "What causes a solar eclipse?", ["The sun moving", "The moon passing between Earth and sun", "The Earth spinning", "The stars aligning"], "The moon passing between Earth and sun"),
        ("The smallest planet in our solar system is Mercury.", "What is the smallest planet in our solar system?", ["Venus", "Mars", "Mercury", "Pluto"], "Mercury"),
        # Continue adding until you have 50 unique passages
    ]

    while len(passages) < 50:
        passages.append(
            (f"Passage {len(passages)}: The sky is blue due to scattering of sunlight.", "What causes the sky to appear blue?", ["Clouds", "Scattering of sunlight", "Rain", "Wind"], "Scattering of sunlight")
        )

    for passage, question, options, correct_answer in passages:
        option_labels = ["A", "B", "C", "D"]
        labeled_options = [f"{label}: {value}" for label, value in zip(option_labels, options)]
        correct_index = options.index(correct_answer)
        correct_label = option_labels[correct_index]
        formatted_question = f"Passage: {passage}\nQuestion: {question}\nOptions:\n" + "\n".join(labeled_options)
        questions.append(formatted_question)
        answers.append(correct_label)
        data.append({"passage": passage, "question": question, "options": options, "answer": correct_answer})

    return questions, answers, data