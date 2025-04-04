# questions/self_desc.py
import random

NOUNS = ["cat", "dog", "car", "book", "house", "tree", "river", "city", "plane", "ship", "pen", "desk", "chair", "lamp", "phone", "clock", "shoe", "hat", "ball", "cup", "plate", "knife", "fork", "spoon", "bag", "box", "door", "window", "road", "bridge", "mountain", "lake", "ocean", "star", "moon", "sun", "cloud", "rain", "snow", "wind", "fire", "ice", "stone", "sand", "grass", "flower", "bird", "fish", "bear", "wolf", "deer"]
VERBS = ["run", "jump", "sing", "dance", "write", "read", "build", "paint", "cook", "clean", "drive", "fly", "swim", "climb", "dig", "cut", "sew", "draw", "play", "listen", "speak", "watch", "wait", "push", "pull", "lift", "drop", "throw", "catch", "kick", "hit", "roll", "spin", "shake", "mix", "pour", "fill", "empty", "open", "close", "lock", "unlock", "fix", "break", "grow", "shrink", "melt", "freeze", "burn"]
ADJECTIVES = ["big", "small", "fast", "slow", "hot", "cold", "bright", "dark", "loud", "quiet", "hard", "soft", "heavy", "light", "long", "short", "tall", "wide", "narrow", "deep", "shallow", "old", "new", "young", "happy", "sad", "angry", "calm", "busy", "lazy", "strong", "weak", "wet", "dry", "clean", "dirty", "sharp", "dull", "smooth", "rough", "sweet", "sour", "bitter", "salty", "fresh", "stale", "warm", "cool"]

def generate_self_description_questions():
    statements = [
        f"I enjoy {random.choice(VERBS)}ing with {random.choice(NOUNS)}.",
        f"I find {random.choice(ADJECTIVES)} situations {random.choice(VERBS)}ing.",
        f"I am {random.choice(ADJECTIVES)} when {random.choice(VERBS)}ing.",
        f"I prefer {random.choice(NOUNS)} over {random.choice(NOUNS)}.",
        f"I feel {random.choice(ADJECTIVES)} about {random.choice(NOUNS)}."
    ]
    questions, answers = [], []
    for _ in range(240):
        stmt = random.choice(statements)
        q = f"{stmt}\nOptions: Strongly Disagree, Disagree, Neutral, Agree, Strongly Agree"
        questions.append(q)
        answers.append("N/A")
    return questions, answers, None