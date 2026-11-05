# pylint: disable=invalid-name  # Module name fixed by existing file layout.
"""Graph postorder traversal implemented iteratively.

Postorder traversal records a node after all of its unvisited
neighbors have been explored. A stack with a marker tracks whether a
node's neighbors have already been expanded.
"""

from __future__ import annotations

from collections.abc import Hashable

from data_structures_and_algorithms.graphs.Graph import Graph


def postorder_traversal_iterative(graph: Graph, start: Hashable) -> list[Hashable]:
    """Return the postorder traversal of a graph from a start node.

    Args:
        graph: The graph to traverse.
        start: The node to begin the traversal from.

    Returns:
        A list of vertices in postorder (finish) order, or an empty
        list if the start node is not in the graph.
    """
    if start not in graph.graph:
        return []

    visited: set[Hashable] = set()
    stack: list[tuple[Hashable, bool]] = [(start, False)]
    result: list[Hashable] = []
    while stack:
        node, expanded = stack.pop()
        if expanded:
            result.append(node)
            continue
        if node in visited:
            continue
        visited.add(node)
        stack.append((node, True))
        # Push successors in reverse order if specific order matters
        for neighbor in reversed(graph.graph[node]):
            if neighbor not in visited:
                stack.append((neighbor, False))

    return result
