# pylint: disable=invalid-name  # Module name fixed by existing file layout.
"""Binary tree preorder traversal implemented recursively.

Preorder traversal visits each node in root, left subtree, right subtree
order.
"""

from __future__ import annotations

from data_structures_and_algorithms.binary_trees.TreeNode import TreeNode


def preorder_traversal_recursive(root: TreeNode | None) -> list[int]:
    """Return the preorder traversal of a binary tree as a list of values.

    Args:
        root: The root node of the tree, or None for an empty tree.

    Returns:
        A list of node values in preorder order.
    """
    result: list[int] = []
    _preorder(root, result)
    return result


def _preorder(node: TreeNode | None, result: list[int]) -> None:
    if node is None:
        return
    result.append(node.val)
    _preorder(node.left, result)
    _preorder(node.right, result)
