# pylint: disable=invalid-name  # Module name fixed by existing file layout.
"""Graph preorder traversal implemented iteratively.

Preorder traversal records each node when it is first discovered,
visiting the node before its neighbors. A stack replaces recursion.
"""

from __future__ import annotations

from collections.abc import Hashable

from data_structures_and_algorithms.graphs.Graph import Graph


def preorder_traversal_iterative(graph: Graph, start: Hashable) -> list[Hashable]:
    """Return the preorder traversal of a graph from a start node.

    Args:
        graph: The graph to traverse.
        start: The node to begin the traversal from.

    Returns:
        A list of vertices in preorder (discovery) order, or an empty
        list if the start node is not in the graph.
    """
    if start not in graph.graph:
        return []

    visited: set[Hashable] = set()
    stack: list[Hashable] = [start]
    result: list[Hashable] = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)
        # Push successors in reverse order if specific order matters
        for neighbor in reversed(graph.graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return result
