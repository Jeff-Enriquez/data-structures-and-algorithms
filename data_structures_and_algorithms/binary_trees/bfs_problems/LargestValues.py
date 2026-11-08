# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
# 515. Find Largest Value in Each Tree Row
# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

from collections import deque

from data_structures_and_algorithms.binary_trees.TreeNode import TreeNode

class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        deq: deque[TreeNode] = deque([root])
        result: list[int] = []
        while deq:
            largest_value: int = deq[-1].val
            for i in range(len(deq), 0, -1):
                node: TreeNode = deq.popleft()
                largest_value = max(largest_value, node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            result.append(largest_value)
        return result
