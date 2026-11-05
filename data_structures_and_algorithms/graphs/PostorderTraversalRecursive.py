# pylint: disable=invalid-name  # Module name fixed by existing file layout.
"""Graph postorder traversal implemented recursively.

Postorder traversal records a node after all of its unvisited
neighbors have been explored.
"""

from __future__ import annotations

from collections.abc import Hashable

from data_structures_and_algorithms.graphs.Graph import Graph


def postorder_traversal_recursive(graph: Graph, start: Hashable) -> list[Hashable]:
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
    result: list[Hashable] = []
    _postorder(graph, start, visited, result)
    return result


def _postorder(graph: Graph, node: Hashable, visited: set[Hashable], result: list[Hashable]) -> None:
    visited.add(node)
    for neighbor in graph.graph[node]:
        if neighbor not in visited:
            _postorder(graph, neighbor, visited, result)
    result.append(node)
