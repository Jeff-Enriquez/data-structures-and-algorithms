# pylint: disable=invalid-name  # Module name fixed by existing file layout.
"""Undirected graph implemented as an adjacency list.

The graph maps each node to the list of vertices adjacent to it. Edges
are undirected, so adding an edge between two vertices updates both
endpoints.
"""


class Graph:
    """An undirected graph represented as an adjacency list.

    Attributes:
        graph: Mapping of each node to the list of its adjacent
            vertices.
    """

    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}

    def add_node(self, node):
        """Add a node to the graph.

        Args:
            node: The node to add.

        Adding a node that already exists has no effect.
        """
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, v1, v2):
        """Add an undirected edge between two existing vertices.

        Args:
            v1: The first node of the edge.
            v2: The second node of the edge.

        Raises:
            KeyError: If either node is not already present in the
                graph.
        """
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
