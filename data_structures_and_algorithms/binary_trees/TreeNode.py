# pylint: disable=invalid-name  # Module name fixed by existing file layout.
"""Binary tree node definition shared by traversal solutions.

Provides the :class:`TreeNode` type used as input to the traversal
algorithms in this package.
"""

from __future__ import annotations


class TreeNode:  # pylint: disable=too-few-public-methods  # Data holder.
    """A node in a binary tree.

    Attributes:
        val: The value stored in this node.
        left: The left child node, or None.
        right: The right child node, or None.
    """

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        """Initialize a tree node.

        Args:
            val: The value stored in this node. Defaults to 0.
            left: The left child node. Defaults to None.
            right: The right child node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right
