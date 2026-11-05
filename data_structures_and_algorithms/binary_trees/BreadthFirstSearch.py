# pylint: disable=invalid-name  # Module name fixed by existing file layout.
"""Binary tree breadth-first search implemented iteratively.

Breadth-first search visits nodes level by level, left to right within each
level, using a queue.
"""

from __future__ import annotations

from collections import deque

from data_structures_and_algorithms.binary_trees.TreeNode import TreeNode


def breadth_first_search(root: TreeNode | None) -> list[int]:
    """Return the breadth-first traversal of a binary tree as a list of values.

    Args:
        root: The root node of the tree, or None for an empty tree.

    Returns:
        A list of node values in level-by-level order.
    """
    if root is None:
        return []

    queue: deque[TreeNode] = deque([root])
    result: list[int] = []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return result
