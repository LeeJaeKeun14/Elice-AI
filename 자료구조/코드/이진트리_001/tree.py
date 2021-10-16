#%%
class Tree:
    def __init__(self, i, l, r) :
        self.index = i
        self.left = l
        self.right = r

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

print(*preorder(myTree))
print(*inorder(myTree))
print(*postorder(myTree))
print(*BFS(myTree))

# input
# 5
# 1 2 3
# 2 4 5
# 3 -1 -1
# 4 -1 -1
# 5 -1 -1