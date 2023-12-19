class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 먼저 트리노드 생성하기
A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')

# 트리 연결 관계 설정하기
A.left = B
A.right = C
B.left = D
C.left = E
C.right = F

# 트리 순회 함수
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.data, end=' ')
        inorder_traversal(node.right)

# 로 출력하기
inorder_traversal(A)

#20214291 김세현
