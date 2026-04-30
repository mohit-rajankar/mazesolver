# sensor.py

import random
from maze import maze

def sensor(cell):
    true_value = maze[cell[0]][cell[1]]

    if random.random() < 0.8:
        return true_value
    else:
        return 1 - true_value