# astar.py

import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))

    came_from = {}
    cost = {start: 0}

    ROWS = len(grid)
    COLS = len(grid[0])

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = current[0] + dx, current[1] + dy

            if 0 <= nx < ROWS and 0 <= ny < COLS:
                if grid[nx][ny] == 1:
                    continue

                new_cost = cost[current] + 1

                if (nx, ny) not in cost or new_cost < cost[(nx, ny)]:
                    cost[(nx, ny)] = new_cost
                    priority = new_cost + heuristic((nx, ny), goal)

                    heapq.heappush(pq, (priority, (nx, ny)))
                    came_from[(nx, ny)] = current

    if goal not in came_from and goal != start:
        return []

    path = []
    curr = goal

    while curr != start:
        path.append(curr)
        curr = came_from[curr]

    path.append(start)
    path.reverse()

    return path