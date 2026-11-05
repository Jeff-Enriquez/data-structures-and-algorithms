# pylint: disable=invalid-name  # Module name fixed by existing file layout.
# pylint: disable=duplicate-code  # Classic traversal variants share structure.
"""Binary tree preorder traversal implemented iteratively.

Preorder traversal visits each node in root, left subtree, right subtree
order. A stack-based approach is used instead of recursion.
"""

from __future__ import annotations

from data_structures_and_algorithms.binary_trees.TreeNode import TreeNode


def preorder_traversal_iterative(root: TreeNode | None) -> list[int]:
    """Return the preorder traversal of a binary tree as a list of values.

    Args:
        root: The root node of the tree, or None for an empty tree.

    Returns:
        A list of node values in preorder order.
    """
    if root is None:
        return []

    stack: list[TreeNode] = [root]
    result: list[int] = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

    return result
