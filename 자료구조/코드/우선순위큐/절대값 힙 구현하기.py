#%%

import heapq

class PriorityQueue:

    def __init__(self) :
        self.data = []

    def push(self, value) :
        '''
        우선순위 큐에 value를 삽입합니다.
        '''
        heapq.heappush(self.data, (abs(value), value))
                

    def pop(self) :
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''
        if len(self.data) > 0:
            heapq.heappop(self.data)

    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''
        if len(self.data) == 0:
            return -1
        else:
            return self.data[0][1]

#%%

def main():
    myPQ = PriorityQueue()

    '''
    테스트를 위한 코드입니다.
    '''

    n = int(input())
    
    for i in range(n) :
        line = [int(v) for v in input().split()]
        if line[0] == 0 :
            myPQ.push(line[1])
        elif line[0] == 1 :
            myPQ.pop()
        elif line[0] == 2 :
            print(myPQ.top())
            
if __name__ == "__main__":
    main()


# input
# 8
# 0 5
# 0 4
# 0 -4
# 0 2
# 2
# 1
# 2
# 1