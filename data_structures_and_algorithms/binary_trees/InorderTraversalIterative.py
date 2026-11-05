# pylint: disable=invalid-name  # Module name fixed by existing file layout.
"""Binary tree inorder traversal implemented iteratively.

Inorder traversal visits each node in left subtree, root, right subtree
order. A stack-based approach is used instead of recursion.
"""

from __future__ import annotations

from data_structures_and_algorithms.binary_trees.TreeNode import TreeNode


def inorder_traversal_iterative(root: TreeNode | None) -> list[int]:
    """Return the inorder traversal of a binary tree as a list of values.

    Args:
        root: The root node of the tree, or None for an empty tree.

    Returns:
        A list of node values in inorder order.
    """
    result: list[int] = []
    stack: list[TreeNode] = []
    node: TreeNode | None = root
    while node is not None or stack:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.val)
        node = node.right

    return result
