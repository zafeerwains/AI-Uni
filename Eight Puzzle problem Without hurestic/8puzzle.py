from collections import deque

def print_path(node):
    """Utility function to print the path from root to the current node"""
    path = []
    while node:
        path.append(node['state'])
        node = node['parent']
    for state in path[::-1]:
        print_state(state)
        print()
    print("----- End of Path -----")

def print_state(state):
    """Utility function to print a state"""
    for row in state:
        print(' '.join(str(cell) for cell in row))

def move(state, direction):
    """Returns a new state after moving the empty tile in the given direction, if possible"""
    moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    new_state = [list(row) for row in state]  # Create a deep copy of the state
    row, col = next((r, c) for r, row in enumerate(state) for c, val in enumerate(row) if val == 0)
    dr, dc = moves[direction]
    new_row, new_col = row + dr, col + dc
    if 0 <= new_row < 3 and 0 <= new_col < 3:
        new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
        return new_state
    return None

def bfs(initial, goal):
    """Performs a BFS search from the initial state to the goal state and prints paths for every node"""
    visited = set()
    queue = deque([{'state': initial, 'parent': None}])

    while queue:
        node = queue.popleft()
        state = node['state']
        state_str = str(state)
        if state_str in visited:
            continue
        visited.add(state_str)

        # Print path for the current node
        print_path(node)

        if state == goal:
            print("Goal state reached.")
            continue  # Keep this to find all solutions or remove to stop after finding the goal

        for direction in ['up', 'down', 'left', 'right']:
            new_state = move(state, direction)
            if new_state and str(new_state) not in visited:
                queue.append({'state': new_state, 'parent': node})

# Example usage
initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

bfs(initial_state, goal_state)