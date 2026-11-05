# pylint: disable=invalid-name  # Module name fixed by existing file layout.
"""Binary tree postorder traversal implemented recursively.

Postorder traversal visits each node in left subtree, right subtree, root
order.
"""

from __future__ import annotations

from data_structures_and_algorithms.binary_trees.TreeNode import TreeNode


def postorder_traversal_recursive(root: TreeNode | None) -> list[int]:
    """Return the postorder traversal of a binary tree as a list of values.

    Args:
        root: The root node of the tree, or None for an empty tree.

    Returns:
        A list of node values in postorder order.
    """
    result: list[int] = []
    _postorder(root, result)
    return result


def _postorder(node: TreeNode | None, result: list[int]) -> None:
    if node is None:
        return
    _postorder(node.left, result)
    _postorder(node.right, result)
    result.append(node.val)
