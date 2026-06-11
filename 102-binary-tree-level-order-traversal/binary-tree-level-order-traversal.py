# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])

        while queue:
            level = []
            level_size = len(queue)

            for i in range(level_size):
                ele = queue.popleft()
                level.append(ele.val)

                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
            result.append(level)
        return result
        