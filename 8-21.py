class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1

def is_balanced(root):
    def height_and_balance(node):
        if node is None:
            return 0, True

        left_height, left_balanced = height_and_balance(node.left)
        right_height, right_balanced = height_and_balance(node.right)

        current_height = max(left_height, right_height) + 1
        current_balanced = abs(left_height - right_height) <= 1 and left_balanced and right_balanced

        return current_height, current_balanced

    _, balanced = height_and_balance(root)
    return balanced

# 트리 구성
A = TreeNode('A', left=TreeNode('B', left=TreeNode('C'), right=TreeNode('D')), right=TreeNode('E', right=TreeNode('F')))

# 균형 여부 확인
result = is_balanced(A)
print("이진 트리는 균형잡혀있는가?", result)
