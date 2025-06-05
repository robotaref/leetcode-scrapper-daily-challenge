import numpy as np
from typing import List, Optional
from testing.solution_test import BaseSolutionTest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        descriptions = np.array(descriptions)
        parents = np.array([node[0] for node in descriptions])
        tmp = np.empty(parents.shape, dtype=np.bool_)
        children = np.array([node[1] for node in descriptions])
        links = np.unique(np.concatenate([parents, children]))
        root = set(parents) - set(children)

        nodes_dict = {}
        for link in links:
            if link not in nodes_dict.keys():
                nodes_dict[link] = TreeNode(val=link)

            np.equal(parents, link, out=tmp)
            indices = np.where(tmp)[0]
            for i in indices:
                link_desc = descriptions[i]
                if link_desc[2]:
                    if link_desc[1] not in nodes_dict.keys():
                        nodes_dict[link_desc[1]] = TreeNode(val=link_desc[1])
                    nodes_dict[link].left = nodes_dict[link_desc[1]]
                    parents[i] = 0
                    descriptions[i] = [0, 0, 0]
                else:
                    if link_desc[1] not in nodes_dict.keys():
                        nodes_dict[link_desc[1]] = TreeNode(val=link_desc[1])
                    nodes_dict[link].right = nodes_dict[link_desc[1]]
                    parents[i] = 0
                    descriptions[i] = [0, 0, 0]

        return nodes_dict[root.pop()]


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.createBinaryTree


BaseSolutionTest(TestableSolution, )
