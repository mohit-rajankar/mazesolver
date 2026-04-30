# Intelligent Maze Solver with Uncertainty  
### Using A* Search Algorithm and Bayesian Reasoning

## Project Overview
This project demonstrates an AI-based maze solving system that can find a path from the start point to the goal even when the environment contains uncertainty.

Unlike a normal maze solver, this system can handle:

- Hidden obstacles  
- Unknown paths  
- Noisy or inaccurate sensor readings  

The project combines **A* Search Algorithm** for pathfinding and **Bayesian Reasoning** for decision-making under uncertainty.

---

## Objective
To build an intelligent agent that can:

- Navigate a maze efficiently  
- Predict blocked paths using probability  
- Update decisions using sensor input  
- Reach the goal with smart path replanning  

---

## Core Techniques Used

### 1. A* Search Algorithm
A* is used to find the shortest and best path from current position to goal.

It uses:

- Actual cost travelled  
- Estimated distance to goal (Heuristic)

This makes it faster and smarter than normal BFS or DFS.

### 2. Bayesian Reasoning
Bayesian logic is used when sensor data is uncertain.

Example:

- Sensor says obstacle detected with 80% confidence  
- System updates probability of wall in that cell

This helps the robot make better decisions.

---

## How System Works

1. Robot starts at Start cell  
2. Sensors check nearby cells  
3. Bayesian update adjusts wall probabilities  
4. A* calculates best path  
5. Robot moves one step  
6. Process repeats until Goal is reached

---

## Technologies Used

- Python  
- Matplotlib (Visualization)  
- Heapq (Priority Queue)  
- Random module  
- NumPy

---

## Input Maze Format

```python
0 = Free Path
1 = Wall