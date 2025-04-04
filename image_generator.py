# image_generator.py
from PIL import Image, ImageDraw, ImageFont
import random
import os

def draw_block_count(filename):
    # Minimal implementation: Create a simple image with a number
    img = Image.new("RGB", (200, 200), "white")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    number = random.randint(1, 10)  # Placeholder number of blocks
    draw.text((50, 50), f"Blocks: {number}", fill="black", font=font)
    img.save(filename)
    return number

def draw_rotated_blocks(filename):
    # Minimal implementation: Draw a simple rotated square
    img = Image.new("RGB", (200, 200), "white")
    draw = ImageDraw.Draw(img)
    square = Image.new("RGB", (50, 50), "black")
    angle = random.randint(0, 360)
    rotated_square = square.rotate(angle, expand=True)
    img.paste(rotated_square, (75, 75))
    img.save(filename)
    return angle

def draw_table_reading(filename):
    # Minimal implementation: Draw a simple 2x2 table
    img = Image.new("RGB", (200, 200), "white")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    table = [[random.randint(1, 100) for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            draw.text((50 + j * 50, 50 + i * 30), str(table[i][j]), fill="black", font=font)
    draw.rectangle([(40, 40), (140, 100)], outline="black")
    draw.line([(90, 40), (90, 100)], fill="black")
    draw.line([(40, 70), (140, 70)], fill="black")
    img.save(filename)
    return table

def draw_hidden_figures(filename):
    # Minimal implementation: Draw a simple shape in a cluttered background
    img = Image.new("RGB", (200, 200), "white")
    draw = ImageDraw.Draw(img)
    # Background clutter
    for _ in range(10):
        x1, y1 = random.randint(0, 200), random.randint(0, 200)
        x2, y2 = random.randint(0, 200), random.randint(0, 200)
        draw.line([(x1, y1), (x2, y2)], fill="gray")
    # Hidden shape (e.g., a triangle)
    shape = random.randint(0, 3)  # 0: triangle, 1: square, 2: circle, 3: line
    if shape == 0:
        draw.polygon([(100, 50), (80, 90), (120, 90)], fill="black")
    elif shape == 1:
        draw.rectangle([(80, 60), (120, 100)], fill="black")
    elif shape == 2:
        draw.ellipse([(80, 60), (120, 100)], fill="black")
    else:
        draw.line([(80, 60), (120, 100)], fill="black", width=2)
    img.save(filename)
    return shape