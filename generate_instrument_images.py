# generate_instrument_images.py
import random
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import math

# Ensure the instrument images directory exists
os.makedirs("images/instrument", exist_ok=True)

def draw_attitude_indicator(climb, bank, filename):
    # Create a larger canvas for the background (will be rotated and cropped)
    bg_img = Image.new("RGB", (300, 300), "white")
    bg_draw = ImageDraw.Draw(bg_img)

    # Background: sky and ground
    center_y = 150 - climb * 75  # Adjust center based on climb (-1 to 1)
    bg_draw.rectangle([(0, 0), (300, center_y)], fill="skyblue")
    bg_draw.rectangle([(0, center_y), (300, 300)], fill="saddlebrown")

    # Horizon line (dashed)
    dash_length = 10
    for x in range(0, 300, dash_length * 2):
        start_x = x
        end_x = min(x + dash_length, 300)
        bg_draw.line([(start_x, center_y), (end_x, center_y)], fill="black", width=2)

    # Rotate the background to simulate bank
    bank_angle = -bank * 45  # Bank: -1 (left) to 1 (right), max 45 degrees
    bg_img = bg_img.rotate(bank_angle, resample=Image.BICUBIC, expand=False)

    # Create the final image (circular gauge)
    img = Image.new("RGB", (200, 200), "white")
    draw = ImageDraw.Draw(img)

    # Mask for circular gauge
    mask = Image.new("L", (200, 200), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse([0, 0, 200, 200], fill=255)
    img.paste(bg_img.crop((50, 50, 250, 250)), (0, 0), mask)

    # Draw the plane silhouette (fixed in center)
    center_x, center_y = 100, 100
    # Nose (triangle)
    draw.polygon([(center_x, center_y - 15), (center_x - 15, center_y + 15), (center_x + 15, center_y + 15)], fill="black")
    # Body
    draw.line([(center_x, center_y + 15), (center_x, center_y + 35)], fill="black", width=4)
    # Wings (swept)
    draw.line([(center_x - 25, center_y + 10), (center_x + 25, center_y + 10)], fill="black", width=2)
    # Tail fins
    draw.line([(center_x - 10, center_y + 35), (center_x + 10, center_y + 35)], fill="black", width=2)

    # Indicator (top marker)
    draw.polygon([(100, 20), (90, 40), (110, 40)], fill="black")
    draw.line([(90, 40), (80, 40)], fill="black", width=2)
    draw.line([(110, 40), (120, 40)], fill="black", width=2)

    # Label
    try:
        font = ImageFont.truetype("arial.ttf", 12)
    except:
        font = ImageFont.load_default()
    draw.text((10, 180), "ARTIFICIAL HORIZON", fill="black", font=font)

    img.save(filename)

def draw_compass(heading, filename):
    img = Image.new("RGB", (200, 200), "white")
    draw = ImageDraw.Draw(img)
    # Compass circle
    draw.ellipse([20, 20, 180, 180], outline="black", width=2)
    # Cardinal directions
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    draw.text((100, 30), "N", fill="black", font=font, anchor="mm")
    draw.text((100, 170), "S", fill="black", font=font, anchor="mm")
    draw.text((30, 100), "W", fill="black", font=font, anchor="mm")
    draw.text((170, 100), "E", fill="black", font=font, anchor="mm")
    # Heading arrow
    angle_rad = math.radians(heading)
    arrow_end_x = 100 + 60 * math.sin(angle_rad)
    arrow_end_y = 100 - 60 * math.cos(angle_rad)
    draw.line([(100, 100), (arrow_end_x, arrow_end_y)], fill="black", width=2)
    draw.text((10, 180), "COMPASS", fill="black", font=font)
    img.save(filename)

def draw_option(climb, bank, filename):
    # Create a canvas for the plane
    plane_img = Image.new("RGBA", (200, 200), (255, 255, 255, 0))  # Transparent background
    plane_draw = ImageDraw.Draw(plane_img)

    # Draw the plane (fighter jet style)
    center_x, center_y = 100, 100
    # Nose (triangle)
    plane_draw.polygon([(center_x, center_y - 20), (center_x - 20, center_y + 20), (center_x + 20, center_y + 20)], fill="black")
    # Body
    plane_draw.line([(center_x, center_y + 20), (center_x, center_y + 40)], fill="black", width=4)
    # Wings (swept)
    plane_draw.line([(center_x - 30, center_y + 10), (center_x + 30, center_y + 10)], fill="black", width=2)
    # Tail fins
    plane_draw.line([(center_x - 15, center_y + 40), (center_x + 15, center_y + 40)], fill="black", width=2)
    # Vertical stabilizer
    plane_draw.line([(center_x, center_y + 40), (center_x, center_y + 30)], fill="black", width=2)

    # Convert climb and bank to pitch and roll angles
    pitch = -climb * 30  # Climb: -1 (descend) to 1 (climb), max 30 degrees
    roll = -bank * 30    # Bank: -1 (left) to 1 (right), max 30 degrees

    # Rotate the plane for pitch and roll
    plane_img = plane_img.rotate(pitch, resample=Image.BICUBIC, center=(center_x, center_y))
    plane_img = plane_img.rotate(roll, resample=Image.BICUBIC, center=(center_x, center_y))

    # Create the final image (crop to 150x100)
    img = Image.new("RGB", (150, 100), "white")
    img.paste(plane_img, (-25, -50), plane_img)  # Adjust position to center after rotation

    img.save(filename)

# Generate 20 sets of images
for i in range(20):
    # Randomize climb and bank for the attitude indicator
    climb = random.uniform(-1, 1)  # -1 (descend) to 1 (climb)
    bank = random.uniform(-1, 1)   # -1 (left) to 1 (right)
    heading = random.randint(0, 359)

    # Ensure climb and bank are significant enough to avoid near-level ambiguity
    threshold = 0.3
    if abs(climb) < threshold:
        climb = random.choice([-1, 1]) * random.uniform(threshold, 1)
    if abs(bank) < threshold:
        bank = random.choice([-1, 1]) * random.uniform(threshold, 1)

    # Determine the correct answer based on climb and bank
    if climb > 0 and bank > 0:
        correct = "A"
        correct_climb, correct_bank = climb, bank
    elif climb > 0 and bank < 0:
        correct = "B"
        correct_climb, correct_bank = climb, bank
    elif climb < 0 and bank > 0:
        correct = "C"
        correct_climb, correct_bank = climb, bank
    elif climb < 0 and bank < 0:
        correct = "D"
        correct_climb, correct_bank = climb, bank
    else:
        # This case should not occur due to the threshold adjustment
        correct = "A"
        correct_climb, correct_bank = climb, bank

    # Generate incorrect options by perturbing climb and bank
    options = [(correct_climb, correct_bank)]  # Start with the correct option
    while len(options) < 4:
        new_climb = random.uniform(-1, 1)
        new_bank = random.uniform(-1, 1)
        # Ensure the new option is different enough from existing ones
        too_close = False
        for opt_climb, opt_bank in options:
            if abs(new_climb - opt_climb) < 0.5 and abs(new_bank - opt_bank) < 0.5:
                too_close = True
                break
        if not too_close:
            options.append((new_climb, new_bank))

    # Shuffle the options and assign to A, B, C, D
    random.shuffle(options)
    option_labels = ["a", "b", "c", "d"]
    correct_label = None
    for idx, (opt_climb, opt_bank) in enumerate(options):
        if opt_climb == correct_climb and opt_bank == correct_bank:
            correct_label = option_labels[idx].upper()
        draw_option(opt_climb, opt_bank, f"images/instrument/option_{option_labels[idx]}_{i}.png")

    # Save the attitude indicator and compass
    draw_attitude_indicator(climb, bank, f"images/instrument/attitude_{i}.png")
    draw_compass(heading, f"images/instrument/compass_{i}.png")

    # Save question data (for reference)
    with open(f"images/instrument/question_{i}.txt", "w") as f:
        f.write(f"Climb: {climb}, Bank: {bank}, Heading: {heading}, Correct: {correct_label}\n")