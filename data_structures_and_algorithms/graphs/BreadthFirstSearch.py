# pylint: disable=invalid-name  # Module name fixed by existing file layout.
"""Graph breadth-first search implemented iteratively.

Breadth-first search visits vertices level by level from a start node,
using a queue to process neighbors before moving deeper into the graph.
"""

from __future__ import annotations

from collections import deque
from collections.abc import Hashable

from data_structures_and_algorithms.graphs.Graph import Graph


def breadth_first_search(graph: Graph, start: Hashable) -> list[Hashable]:
    """Return the breadth-first traversal of a graph from a start node.

    Args:
        graph: The graph to traverse.
        start: The node to begin the traversal from.

    Returns:
        A list of vertices in level-by-level order, or an empty list if
        the start node is not in the graph.
    """
    if start not in graph.graph:
        return []

    visited: set[Hashable] = {start}
    queue: deque[Hashable] = deque([start])
    result: list[Hashable] = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result
