from typing import List, Dict, Set, Tuple

def bidirectional_search(graph: Dict[int, List[int]], start: int, goal: int) -> bool:
   
    if start == goal:
        return True

    # Initialize the frontiers for both forward and backward search
    frontier_forward: Set[int] = {start}
    frontier_backward: Set[int] = {goal}

    # Initialize the explored sets for both directions
    explored_forward: Set[int] = set()
    explored_backward: Set[int] = set()

    while frontier_forward and frontier_backward:
        # Expand in the forward direction
        next_frontier_forward: Set[int] = set()
        for node in frontier_forward:
            for neighbor in graph.get(node, []):
                if neighbor in frontier_backward:
                    return True
                if neighbor not in explored_forward:
                    next_frontier_forward.add(neighbor)
            explored_forward.add(node)
        frontier_forward = next_frontier_forward

        # Expand in the backward direction
        next_frontier_backward: Set[int] = set()
        for node in frontier_backward:
            for neighbor, neighbors in graph.items():
                if node in neighbors and neighbor not in explored_backward:
                    if neighbor in frontier_forward:
                        return True
                    next_frontier_backward.add(neighbor)
            explored_backward.add(node)
        frontier_backward = next_frontier_backward

    return False

# Example usage
if __name__ == "__main__":
    graph: Dict[int, List[int]] = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5, 6],
        3: [1],
        4: [1, 7, 8],
        5: [2],
        6: [2],
        7: [4],
        8: [4]
    }
    start_vertex: int = 0
    goal_vertex: int = 7
    path_exists: bool = bidirectional_search(graph, start_vertex, goal_vertex)
    print(f"Path exists: {path_exists}")