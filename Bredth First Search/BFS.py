from collections import deque
from typing import Dict, List, Set, Deque

# Define a function to perform BFS with color coding
def bfs_with_colors(graph: Dict[str, List[str]], start: str) -> None:
    # Initialize color dictionaries
    color: Dict[str, str] = {node: 'white' for node in graph}
    # A queue to maintain the nodes to visit
    queue: Deque[str] = deque([start])
    color[start] = 'grey'  # Mark the start node as grey (in queue)

    while queue:
        vertex: str = queue.popleft()
        print(f"{vertex} (black) ", end="")  # Print visited vertex with its color
        color[vertex] = 'black'  # Mark as visited (black)

        for neighbor in graph[vertex]:
            if color[neighbor] == 'white':  # Check if the neighbor is unvisited
                queue.append(neighbor)
                color[neighbor] = 'grey'  # Mark as in queue (grey)
                print(f"{neighbor} (grey) ", end="")  # Print neighbor with its color

# Example usage
if __name__ == '__main__':
    # A sample graph represented as an adjacency list
    graph: Dict[str, List[str]] = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("BFS with color coding starting from node A:")
    bfs_with_colors(graph, 'A')