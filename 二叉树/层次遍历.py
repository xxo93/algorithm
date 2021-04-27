class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        array_2D = []

        def loopTreeNode(TreeNode):
            array = []
            if TreeNode is not None:
                if TreeNode.left is not None:
                    array.append(TreeNode.left.val)
                    loopTreeNode(TreeNode.left)
                if TreeNode.right is not None:
                    array.append(TreeNode.right.val)
                    loopTreeNode(TreeNode.right)
            return None if array == [] else array

        if root is not None:
            array_1D = loopTreeNode(root)
            if array_1D is not None:
                array_2D.insert(0, array_1D)

        return array_2D



if __name__ == '__main__':

    pass
