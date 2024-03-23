def preorder(root):
    if root != ".":
        print(root, end="")
        preorder(tree[root][0])  # left c
        preorder(tree[root][1])  # right c


def inorder(root):
    if root != ".":
        inorder(tree[root][0])  # left
        print(root, end="")
        inorder(tree[root][1])  # right


def postorder(root):
    if root != ".":
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end="")


n = int(input())
tree = {}
for i in range(n):
    p, lc, rc = input().split()
    tree[p] = [lc, rc]

preorder("A")
print()
inorder("A")
print()
postorder("A")

# 메모리 초과
# tree = [None] * (2**n)
# for i in range(n):
#     p, l, r = input().split()
#     # 부모 인덱스 찾기
#     p_idx = None
#     for j in range(len(tree)):
#         if tree[j] == p:
#             p_idx = j
#             break
#     if p_idx is not None:
#         if l != ".":
#             tree[p_idx*2+1] = l
#         if r != ".":
#             tree[p_idx*2+2] = r
#     else:
#         for j in range(len(tree)):
#             if tree[j] is None:
#                 tree[j] = p
#                 if l != ".":
#                     tree[j * 2 + 1] = l
#                 if r != ".":
#                     tree[j * 2 + 2] = r
#                 break
