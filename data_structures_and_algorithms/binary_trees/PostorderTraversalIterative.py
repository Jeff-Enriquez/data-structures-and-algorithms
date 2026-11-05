# pylint: disable=invalid-name  # Module name fixed by existing file layout.
# pylint: disable=duplicate-code  # Classic traversal variants share structure.
"""Binary tree postorder traversal implemented iteratively.

Postorder traversal visits each node in left subtree, right subtree, root
order. A stack-based approach is used instead of recursion.
"""

from __future__ import annotations

from data_structures_and_algorithms.binary_trees.TreeNode import TreeNode


def postorder_traversal_iterative(root: TreeNode | None) -> list[int]:
    """Return the postorder traversal of a binary tree as a list of values.

    Args:
        root: The root node of the tree, or None for an empty tree.

    Returns:
        A list of node values in postorder order.
    """
    if root is None:
        return []

    stack: list[TreeNode] = []
    result: list[int] = []
    last_visited: TreeNode | None = None
    current: TreeNode | None = root
    while stack or current is not None:
        while current is not None:
            stack.append(current)
            current = current.left

        peek = stack[-1]
        if peek.right is not None and peek.right is not last_visited:
            current = peek.right
        else:
            result.append(peek.val)
            last_visited = stack.pop()

    return result
