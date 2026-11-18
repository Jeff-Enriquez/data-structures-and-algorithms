# pylint: disable=invalid-name  # Module name fixed by existing file layout.
"""Disjoint-set (union-find) data structure with path compression."""

from __future__ import annotations

from collections.abc import Hashable, Iterable


class UnionFindDict:
    """Disjoint-set data structure tracking a partition of hashable elements.

    Supports near-constant-time ``find`` and ``union`` using union by rank and
    path compression. Unlike ``UnionFind``, elements are arbitrary hashable
    keys backed by a dictionary instead of a contiguous integer range.

    Attributes:
        parent: Maps each element to its parent; a root points to itself.
        rank: Upper bound on the height of each root's tree.
    """

    def __init__(self, elements: Iterable[Hashable] = ()) -> None:
        """Initialize disjoint singleton sets for ``elements``.

        Args:
            elements: Hashable elements, each forming its own singleton set.
        """
        self.parent: dict[Hashable, Hashable] = {}
        self.rank: dict[Hashable, int] = {}
        for element in elements:
            self.add(element)

    def add(self, element: Hashable) -> None:
        """Insert ``element`` as a new singleton set, if not already present.

        Args:
            element: The element to add.
        """
        if element not in self.parent:
            self.parent[element] = element
            self.rank[element] = 1

    def find(self, element: Hashable) -> Hashable:
        """Return the root of ``element``, compressing the path along the way.

        Args:
            element: The element whose set representative is sought.

        Returns:
            The root element of the set containing ``element``.

        Raises:
            KeyError: If ``element`` has not been added.
        """
        root: Hashable = element
        while self.parent[root] != root:
            root = self.parent[root]

        # Compress the path so every visited node points straight at the root.
        while self.parent[element] != element:
            parent: Hashable = self.parent[element]
            self.parent[element] = root
            element = parent
        return root

    def union(self, first: Hashable, second: Hashable) -> None:
        """Merge the sets containing ``first`` and ``second``.

        Args:
            first: An element of the first set.
            second: An element of the second set.

        Raises:
            KeyError: If ``first`` or ``second`` has not been added.
        """
        root_first: Hashable = self.find(first)
        root_second: Hashable = self.find(second)
        if root_first == root_second:
            return

        if self.rank[root_first] > self.rank[root_second]:
            self.parent[root_second] = root_first
        elif self.rank[root_first] < self.rank[root_second]:
            self.parent[root_first] = root_second
        else:
            self.parent[root_second] = root_first
            self.rank[root_first] += 1
