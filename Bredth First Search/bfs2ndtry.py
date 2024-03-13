from collections import deque
from typing import Dict, List, Deque, Optional

def bfs_with_colors_distance_and_parent(graph: Dict[str, List[str]], start: str) -> None:
 
    color: Dict[str, str] = {node: 'white' for node in graph}
    distance: Dict[str, float] = {node: float('inf') for node in graph}  
    parent: Dict[str, Optional[str]] = {node: None for node in graph}  
    
    print("Before starting All", color, distance, parent)

    queue: Deque[str] = deque([start])
    
    color[start] = 'grey' 
    distance[start] = 0 

    while queue:
        vertex: str = queue.popleft()
        print(f"{vertex} (black, distance {distance[vertex]}, parent {parent[vertex]}) ", end="")  # Print visited vertex with its color, distance, and parent
        color[vertex] = 'black' 

        for neighbor in graph[vertex]:
            if color[neighbor] == 'white':  
                queue.append(neighbor)
                color[neighbor] = 'grey'  
                distance[neighbor] = distance[vertex] + 1  
                parent[neighbor] = vertex  
                print(f"{neighbor} (grey, distance {distance[neighbor]}, parent {parent[neighbor]}) ", end="")  # Print neighbor with its color, distance, and parent

if __name__ == '__main__':
    graph: Dict[str, List[str]] = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("BFS with color coding, distance, and parent tracking starting from node A:")
    bfs_with_colors_distance_and_parent(graph, 'A')