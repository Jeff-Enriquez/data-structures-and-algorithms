# pylint: disable=invalid-name  # Module name fixed by existing file layout.
"""Graph preorder traversal implemented recursively.

Preorder traversal records each node when it is first discovered,
visiting the node before its neighbors.
"""

from __future__ import annotations

from collections.abc import Hashable

from data_structures_and_algorithms.graphs.Graph import Graph


def preorder_traversal_recursive(graph: Graph, start: Hashable) -> list[Hashable]:
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
    result: list[Hashable] = []
    _preorder(graph, start, visited, result)
    return result


def _preorder(graph: Graph, node: Hashable, visited: set[Hashable], result: list[Hashable]) -> None:
    visited.add(node)
    result.append(node)
    for neighbor in graph.graph[node]:
        if neighbor not in visited:
            _preorder(graph, neighbor, visited, result)
