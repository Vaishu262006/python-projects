# pathfinding.py
from collections import deque

def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    prev = [[None]*cols for _ in range(rows)]
    queue = deque([start])
    visited[start[0]][start[1]] = True

    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    while queue:
        r,c = queue.popleft()
        if (r,c) == goal:
            break
        for dr,dc in directions:
            nr,nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and not visited[nr][nc] and grid[nr][nc]==0:
                queue.append((nr,nc))
                visited[nr][nc] = True
                prev[nr][nc] = (r,c)
    
    # reconstruct path
    path = []
    at = goal
    while at:
        path.append(at)
        at = prev[at[0]][at[1]]
    path.reverse()
    if path[0] == start:
        return path
    else:
        return None

# Example usage
grid = [
    [0,0,0,0],
    [1,1,0,1],
    [0,0,0,0],
    [0,1,1,0],
]
start = (0,0)
goal = (3,3)

path = bfs(grid, start, goal)
print("Path:", path)