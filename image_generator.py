# image_generator.py
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
import numpy as np

def save_instrument_image(data, filename):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.set_xlim(-1, 1)
    ax1.set_ylim(-1, 1)
    ax1.set_aspect('equal')
    ax1.set_title("Artificial Horizon")
    
    climb_angle = data["climb"]
    bank_angle = data["bank"]
    horizon_y = -climb_angle
    horizon_x1 = -np.cos(np.radians(bank_angle))
    horizon_y1 = horizon_y - np.sin(np.radians(bank_angle))
    horizon_x2 = np.cos(np.radians(bank_angle))
    horizon_y2 = horizon_y + np.sin(np.radians(bank_angle))
    ax1.plot([horizon_x1, horizon_x2], [horizon_y1, horizon_y2], 'k-', lw=2)
    
    pointer_angle = bank_angle + 90
    pointer_x = 0.8 * np.cos(np.radians(pointer_angle))
    pointer_y = 0.8 * np.sin(np.radians(pointer_angle))
    ax1.plot([0, pointer_x], [0, pointer_y], 'k-', lw=2)
    ax1.plot([0, 0.1, -0.1, 0], [0, 0.05, 0.05, 0], 'b-', lw=2)
    
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.set_aspect('equal')
    ax2.set_title("Compass")
    heading = data["heading"]
    ax2.arrow(0, 0, 0.8 * np.cos(np.radians(heading)), 0.8 * np.sin(np.radians(heading)), 
              head_width=0.1, head_length=0.1, fc='k', ec='k')
    
    plt.savefig(filename, dpi=100)
    plt.close(fig)

def save_block_counting_image(data, filename):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    blocks = data["blocks"]
    numbered_block = data["numbered"]
    for (x, y, z) in blocks:
        ax.bar3d(x, y, z, 1, 1, 1, shade=True, color='gray', alpha=0.6)
    ax.text(numbered_block[0] + 0.5, numbered_block[1] + 0.5, numbered_block[2] + 1.5, 
            "1", color='red', fontsize=12)
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_zlim(0, 3)
    plt.savefig(filename, dpi=100)
    plt.close(fig)

def save_table_reading_image(data, filename):
    fig, ax = plt.subplots(figsize=(8, 6))
    table = data["table"]
    x_vals = data["x_vals"]
    y_vals = data["y_vals"]
    ax.table(cellText=table, rowLabels=y_vals, colLabels=x_vals, loc='center')
    ax.axis('off')
    plt.savefig(filename, dpi=100)
    plt.close(fig)

def save_rotated_blocks_image(data, filename):
    fig, axs = plt.subplots(1, 5, figsize=(15, 3))
    original = data["original"]
    options = data["options"]
    axs[0].plot(*zip(*original), 'bo-')
    axs[0].set_title("Original")
    axs[0].set_xlim(-1, 3)
    axs[0].set_ylim(-1, 3)
    for i, rotated in enumerate(options, 1):
        axs[i].plot(*zip(*rotated), 'bo-')
        axs[i].set_title(f"Option {chr(64+i)}")
        axs[i].set_xlim(-3, 3)
        axs[i].set_ylim(-3, 3)
    plt.savefig(filename, dpi=100)
    plt.close(fig)

def save_hidden_figures_image(data, filename):
    fig, axs = plt.subplots(2, 3, figsize=(12, 8))
    figures = data["figures"]
    complex_coords = data["complex"]
    for i, (label, coords) in enumerate(figures.items()):
        row, col = divmod(i, 3)
        if row == 0:
            axs[row, col].plot(*zip(*coords), 'k-')
            axs[row, col].set_title(label)
            axs[row, col].set_xlim(-1, 2)
            axs[row, col].set_ylim(-1, 2)
    axs[1, 0].plot(*zip(*complex_coords), 'ko-', alpha=0.5)
    axs[1, 0].set_title("Find the Hidden Figure")
    axs[1, 0].set_xlim(-1, 2)
    axs[1, 0].set_ylim(-1, 2)
    axs[1, 1].axis('off')
    axs[1, 2].axis('off')
    plt.savefig(filename, dpi=100)
    plt.close(fig)