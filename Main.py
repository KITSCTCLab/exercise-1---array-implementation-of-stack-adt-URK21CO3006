import os
class Stack:
    def _init_(self, size):
        self.items = []
        self.size = size
        self.top = -1

    def is_empty(self):
        if(stack.top==-1):
            return true
        else:
            return false

    def is_full(self):
        if(stack.top==stack.size-1):
            return true 
        else:
            return false
        

    def push(self, data):
        if not self.is_full():
            stack.top += 1
            stack.items.data.append(data)
        

    def pop(self):
        if not self.is_empty():
            x=stack.items.pop()
            stack.pop-=1
            return x
        

    def status(self):
        for i in range(0,len(stack.items)):
            print(stack.items[i],end="\n")
        
        


# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
