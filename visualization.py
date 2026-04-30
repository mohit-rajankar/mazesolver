# visualization.py

import matplotlib.pyplot as plt
import numpy as np
from maze import maze, start, goal

def draw_maze(current, path, step):
    plt.clf()

    grid = np.array(maze)
    plt.imshow(grid, cmap="gray_r")

    for p in path:
        plt.text(p[1], p[0], "•",
                 ha='center', va='center',
                 color='blue', fontsize=15)

    plt.text(start[1], start[0], "S",
             ha='center', va='center',
             color='green', fontsize=16, fontweight='bold')

    plt.text(goal[1], goal[0], "G",
             ha='center', va='center',
             color='red', fontsize=16, fontweight='bold')

    plt.text(current[1], current[0], "R",
             ha='center', va='center',
             color='orange', fontsize=16, fontweight='bold')

    plt.title(f"Intelligent Maze Solver | Step {step}")
    plt.xticks([])
    plt.yticks([])
    plt.pause(0.8)