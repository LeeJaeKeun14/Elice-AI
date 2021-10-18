# import heapq

# class PriorityQueue:
#     '''
#     우선순위 큐를 힙으로 구현합니다
#     '''

#     def __init__(self) :
#         self.data = []

#     def push(self, value) :
#         '''
#         우선순위 큐에 value를 삽입합니다.
#         '''
#         heapq.heappush(self.data, value)
                

#     def pop(self) :
#         '''
#         우선순위가 가장 높은 원소를 제거합니다.
#         '''
#         if len(self.data) > 0:
#             heapq.heappop(self.data)

#     def top(self) :
#         '''
#         우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
#         '''
#         if len(self.data) == 0:
#             return -1
#         else:
#             return self.data[0]

#%%
class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''

    def __init__(self) :
        self.data = [0]

    def push(self, value) :
        '''
        우선순위 큐에 value를 삽입합니다.
        '''
        self.data.append(value)
        
        index = len(self.data) -1
        
        while index != 1:
            if self.data[index // 2] > self.data[index]:
                temp = self.data[index]
                self.data[index] = self.data[index // 2]
                self.data[index//2] = temp
                
                index = index // 2
            else:
                break
                

    def pop(self) :
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''
        if len(self.data) == 1:
            return
        
        self.data[1] = self.data[-1]
        self.data.pop()
        
        index = 1
        
        while True:
            if len(self.data) -1 < index * 2:
                break
            elif len(self.data) -1 < index * 2 + 1:
                priority = index * 2
            else:
                if self.data[index * 2] < self.data[index * 2 + 1]:
                    priority = index * 2
                else:
                    priority = index * 2 + 1
            if self.data[index] > self.data[priority]:
                temp = self.data[index]
                self.data[index] = self.data[priority]
                self.data[priority] = temp
                
                index = priority
            else:
                break
                
                
        

    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''
        if len(self.data) == 1:
            return -1
        else:
            return self.data[1]

# %%
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


# 8
# 0 1
# 0 4
# 0 3
# 0 2
# 2
# 1
# 2
# 1
# %%
