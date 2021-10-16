#%%
class Tree:
    def __init__(self, i, l, r) :
        self.index = i
        self.left = l
        self.right = r
        self.depth = -1

    def setDepth(self, d):
        self.depth = d

    def addNode(self, i, l, r) :
        '''
        트리 내의 정점 i에 대하여 왼쪽자식을 l, 오른쪽 자식을 r로
        설정해주는 함수를 작성하세요.
        '''
        if self.index == None or self.index == i:
            self.index = i
            self.left = Tree(l, None, None) if l != None else None
            self.right = Tree(r, None, None) if r != None else None
            
            return True
        else:
            flag = False
            if self.left != None:
                flag = self.left.addNode(i, l, r)
            if flag == False and self.right != None:
                flag = self.right.addNode(i, l, r)
            
            return flag
#%%
'''
preorder, inorder, postorder 함수를 구현하세요.
'''
def preorder(tree) :
    '''
    tree를 전위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []
    
    result.append(tree.index)
    
    if tree.left != None:
        result += preorder(tree.left)
    if tree.right != None:
        result += preorder(tree.right)

    return result

def inorder(tree) :
    '''
    tree를 중위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []
    
    if tree.left != None:
        result += inorder(tree.left)
        
    result.append(tree.index)
    
    if tree.right != None:
        result += inorder(tree.right)

    return result

def postorder(tree) :
    '''
    tree를 후위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []
    
    if tree.left != None:
        result += postorder(tree.left)
    if tree.right != None:
        result += postorder(tree.right)
        
    result.append(tree.index)
    

    return result

'''
BFS 함수를 구현하세요.
'''
from queue import Queue

def BFS(tree) :
    '''
    tree를 너비 우선 탐색으로 순회하여 리스트로 반환하는 함수를 작성하세요.
    '''
    q = Queue()
    q.put(tree)
    result = []
    
    while len(q.queue) > 0:
        cur = q.get()
        if cur == None:
            continue
        
        result.append(cur.index)
        
        q.put(cur.left)
        q.put(cur.right)
    return result

'''
getHeight 함수를 작성하세요.
'''
def getHeight(myTree) :
    '''
    myTree의 높이를 반환하는 함수를 작성하세요.
    '''
    if myTree == None:
        return 0
    else:
        return 1 + max(getHeight(myTree.left), getHeight(myTree.right))
    
    return height


def inorder_depth(tree, depth) :
    result = []
    
    if tree.left != None:
        result += inorder_depth(tree.left, depth + 1)
        
    tree.setDepth(depth)
    result.append(tree)
    
    if tree.right != None:
        result += inorder_depth(tree.right, depth + 1)

    return result
'''
getWidth 함수를 작성하세요.
'''
def getWidth(myTree) :
    '''
    myTree의 너비가 가장 넓은 레벨과 그 레벨의 너비를 반환하는 함수를 작성하세요.
    가장 넓은 레벨 l과 그 레벨의 너비 w를 튜플로 반환해야 합니다.
    
    반환값 형식 : (l, w)
    '''

    result = inorder_depth(myTree, 1)
    n = len(result)
    
    # 정점의 개수는 1000 이하
    # 깊이 퇴댓값은 1000
    
    # left[i] = 깊이가 i 인 모든 노드들 중에서, 가장 우ㅚㄴ쪽에 있는 노드 행
    # right[i] = 깊이가 i인 모든 노드들 중에서, 가장 오른쪽에 있는 노드 행
    left = [1001 for i in range(1001)]
    right = [-1 for i in range(1001)]
    maxDepth = 0

    for i in range(n):
        d = result[i].depth
        
        left[d] = min(left[d], i)
        right[d] = max(right[d], i)
        
        maxDepth = max(maxDepth, d)
        
    ansDepth = 0
    ans = 0
    
    for i in range(1, maxDepth + 1):
        temp = right[i] - left[i] + 1
        
        if ans < temp:
            ansDepth = i
            ans = temp
    
    return (ansDepth, ans)

#%%

myTree = Tree(None, None, None)

n = int(input())

for i in range(n) :
    myList = [int(v) for v in input().split()]

    if myList[1] == -1 :
        myList[1] = None

    if myList[2] == -1 :
        myList[2] = None

    myTree.addNode(myList[0], myList[1], myList[2])

print(*preorder(myTree)) # 전위 탐색
print(*inorder(myTree)) # 중위 탐색
print(*postorder(myTree)) # 후위 탐색
print(*BFS(myTree))  # 너비 탐색
print(getHeight(myTree)) # 깊이
print(*getWidth(myTree)) # 너비

# input
# 5
# 1 2 3
# 2 4 5
# 3 -1 -1
# 4 -1 -1
# 5 -1 -1