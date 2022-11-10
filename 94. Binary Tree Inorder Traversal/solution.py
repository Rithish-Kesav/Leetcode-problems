class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        elements = []

        if root == None:
            return elements

        if root.left == None and root.right == None:
            elements.append(root.val)
            return elements

        if root.left:
            elements += self.inorderTraversal(root.left)

        elements.append(root.val)

        if root.right:
            elements += self.inorderTraversal(root.right)

        return elements
