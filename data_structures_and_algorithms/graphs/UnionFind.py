# pylint: disable=invalid-name  # Module name fixed by existing file layout.
"""Disjoint-set (union-find) data structure with path compression."""

from __future__ import annotations


class UnionFind:
    """Disjoint-set data structure tracking a partition of ``size`` elements.

    Supports near-constant-time ``find`` and ``union`` using union by rank and
    path compression.

    Attributes:
        parent: Maps each element to its parent; a root points to itself.
        rank: Upper bound on the height of each root's tree.
    """

    def __init__(self, size: int) -> None:
        """Initialize ``size`` disjoint singleton sets.

        Args:
            size: Number of elements, labeled ``0`` through ``size - 1``.
        """
        self.parent: list[int] = list(range(size))
        self.rank: list[int] = [1] * size

    def find(self, element: int) -> int:
        """Return the root of ``element``, compressing the path along the way.

        Args:
            element: The element whose set representative is sought.

        Returns:
            The root element of the set containing ``element``.
        """
        root: int = element
        while self.parent[root] != root:
            root = self.parent[root]

        # Compress the path so every visited node points straight at the root.
        while self.parent[element] != element:
            parent: int = self.parent[element]
            self.parent[element] = root
            element = parent
        return root

    def union(self, first: int, second: int) -> None:
        """Merge the sets containing ``first`` and ``second``.

        Args:
            first: An element of the first set.
            second: An element of the second set.
        """
        root_first: int = self.find(first)
        root_second: int = self.find(second)
        if root_first == root_second:
            return

        if self.rank[root_first] > self.rank[root_second]:
            self.parent[root_second] = root_first
        elif self.rank[root_first] < self.rank[root_second]:
            self.parent[root_first] = root_second
        else:
            self.parent[root_second] = root_first
            self.rank[root_first] += 1
