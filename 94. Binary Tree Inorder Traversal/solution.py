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

# Alternate recursive solution


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        elements = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            elements.append(root.val)
            inorder(root.right)
        inorder(root)
        return elements

# Iterative solution


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        elements = []
        cur = root
        stack = []

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            elements.append(cur.val)
            cur = cur.right
        return elements
