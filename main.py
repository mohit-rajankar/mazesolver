# main.py

import matplotlib.pyplot as plt
from maze import ROWS, COLS, start, goal, maze
from astar import astar
from bayesian import bayesian_update
from sensor import sensor
from visualization import draw_maze

# Initial belief
belief = [[0.2 for _ in range(COLS)] for _ in range(ROWS)]

belief[start[0]][start[1]] = 0.0
belief[goal[0]][goal[1]] = 0.0

plt.figure(figsize=(7,7))

current = start
step = 0
visited = set()

while current != goal:
    step += 1
    visited.add(current)

    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = current[0] + dx, current[1] + dy

        if 0 <= nx < ROWS and 0 <= ny < COLS:
            reading = sensor((nx, ny))
            belief[nx][ny] = bayesian_update(belief[nx][ny], reading)

    estimated_grid = [
        [1 if belief[i][j] > 0.6 else 0 for j in range(COLS)]
        for i in range(ROWS)
    ]

    estimated_grid[start[0]][start[1]] = 0
    estimated_grid[goal[0]][goal[1]] = 0

    path = astar(estimated_grid, current, goal)

    draw_maze(current, path, step)

    if not path or len(path) < 2:
        print("No path found.")
        break

    next_pos = path[1]

    if maze[next_pos[0]][next_pos[1]] == 1:
        print("Blocked wall discovered at:", next_pos)
        belief[next_pos[0]][next_pos[1]] = 0.99
        continue

    current = next_pos

draw_maze(current, [], step+1)

if current == goal:
    print("Reached Goal Successfully!")

plt.show()