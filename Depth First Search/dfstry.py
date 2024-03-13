from typing import Dict, List

def dfs_with_colors_and_distance(graph: Dict[str, List[str]], vertex: str, color: Dict[str, str], distance: Dict[str, int], current_distance: int = 0) -> None:
    color[vertex] = 'grey'  
    distance[vertex] = current_distance 
    print(f"{vertex} (grey, distance {distance[vertex]}) ", end="") 
    for neighbor in graph[vertex]:
        if color[neighbor] == 'white':  
            dfs_with_colors_and_distance(graph, neighbor, color, distance, current_distance + 1)  

    color[vertex] = 'black'  
    print(f"{vertex} (black, distance {distance[vertex]}) ", end="") 
if __name__ == '__main__':
   
    graph: Dict[str, List[str]] = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    color: Dict[str, str] = {node: 'white' for node in graph}  
    distance: Dict[str, float] = {node: float('inf') for node in graph} 

    print("DFS with color coding and distance starting from node A:")
    dfs_with_colors_and_distance(graph, 'A', color, distance)