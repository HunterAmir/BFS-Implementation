
from collections import deque


def read_grid_from_user():
    print("Enter the grid row by row. Use S, G, ., #")
    print("Press Enter on an empty line when done.\n")

    grid = []
    while True:
        line = input().strip()
        if line == "":
            break
        grid.append(list(line))

    return grid
def read_grid():
    grid = []
    while True:
        try:
            line = input().strip()
            if line:
                grid.append(line.split())
        except EOFError:
            break
    return grid

def find_positions(grid):
    start = goal = None
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 'S':
                start = (r, c)
            elif val == 'G':
                goal = (r, c)
    return start, goal

def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = {start: None}  # maps node → predecessor

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        r, c = queue.popleft()

        if (r, c) == goal:
            break

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != '#' and (nr, nc) not in visited:
                    visited[(nr, nc)] = (r, c)
                    queue.append((nr, nc))

    return visited

def reconstruct_path(visited, start, goal):
    if goal not in visited:
        return None

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = visited[cur]
    path.reverse()
    return path

def main():
    grid = read_grid_from_user()
    start, goal = find_positions(grid)

    visited = bfs(grid, start, goal)
    path = reconstruct_path(visited, start, goal)

    if not path:
        print("No path found.")
        return

    print("Shortest path length:", len(path) - 1)
    print("Path:")
    for step in path:
        print(step)

if __name__ == "__main__":
    main()