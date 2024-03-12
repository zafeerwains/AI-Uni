from typing import Dict, List

# Define a function to perform DFS with color coding and distance calculation
def dfs_with_colors_and_distance(graph: Dict[str, List[str]], vertex: str, color: Dict[str, str], distance: Dict[str, int], current_distance: int = 0) -> None:
    color[vertex] = 'grey'  # Mark the current node as in queue (grey)
    distance[vertex] = current_distance  # Set the distance of the current node
    print(f"{vertex} (grey, distance {distance[vertex]}) ", end="")  # Print current node with its color and distance

    for neighbor in graph[vertex]:
        if color[neighbor] == 'white':  # Check if the neighbor is unvisited
            dfs_with_colors_and_distance(graph, neighbor, color, distance, current_distance + 1)  # Recursive call

    color[vertex] = 'black'  # Mark the current node as visited (black)
    print(f"{vertex} (black, distance {distance[vertex]}) ", end="")  # Print current node again with its final color and distance

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

    # Initialize color and distance dictionaries
    color: Dict[str, str] = {node: 'white' for node in graph}  # All nodes start as white (unvisited)
    distance: Dict[str, float] = {node: float('inf') for node in graph}  # Use infinity as initial distance

    print("DFS with color coding and distance starting from node A:")
    dfs_with_colors_and_distance(graph, 'A', color, distance)