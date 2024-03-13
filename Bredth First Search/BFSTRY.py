from collections import deque
from typing import Dict, List, Deque

# Define a function to perform BFS with color coding and distance calculation
def bfs_with_colors_and_distance(graph: Dict[str, List[str]], start: str) -> None:
    # Initialize color and distance dictionaries
    color: Dict[str, str] = {node: 'white' for node in graph}
    distance: Dict[str, float] = {node: float('inf') for node in graph}  # Use infinity as initial distance
    print("Before starting All",color,distance)
    # A queue to maintain the nodes to visit
    queue: Deque[str] = deque([start])
    
    color[start] = 'grey'  # Mark the start node as grey (in queue)
    distance[start] = 0  # Distance from start to start is 0

    while queue:
        vertex: str = queue.popleft()
        print(f"{vertex} (black, distance {distance[vertex]}) ", end="")  # Print visited vertex with its color and distance
        color[vertex] = 'black'  # Mark as visited (black)

        for neighbor in graph[vertex]:
            if color[neighbor] == 'white':  # Check if the neighbor is unvisited
                queue.append(neighbor)
                color[neighbor] = 'grey'  # Mark as in queue (grey)
                distance[neighbor] = distance[vertex] + 1  # Set distance
                print(f"{neighbor} (grey, distance {distance[neighbor]}) ", end="")  # Print neighbor with its color and distance

# Example usage
if __name__ == '__main__':
    graph: Dict[str, List[str]] = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("BFS with color coding and distance starting from node A:")
    bfs_with_colors_and_distance(graph, 'A')