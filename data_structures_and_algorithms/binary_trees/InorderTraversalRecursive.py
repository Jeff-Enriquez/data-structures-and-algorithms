# pylint: disable=invalid-name  # Module name fixed by existing file layout.
"""Binary tree inorder traversal implemented recursively.

Inorder traversal visits each node in left subtree, root, right subtree
order.
"""

from __future__ import annotations

from data_structures_and_algorithms.binary_trees.TreeNode import TreeNode


def inorder_traversal_recursive(root: TreeNode | None) -> list[int]:
    """Return the inorder traversal of a binary tree as a list of values.

    Args:
        root: The root node of the tree, or None for an empty tree.

    Returns:
        A list of node values in inorder order.
    """
    result: list[int] = []
    _inorder(root, result)
    return result


def _inorder(node: TreeNode | None, result: list[int]) -> None:
    if node is None:
        return
    _inorder(node.left, result)
    result.append(node.val)
    _inorder(node.right, result)
