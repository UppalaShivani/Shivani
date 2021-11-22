# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# Output
# [null,null,null,null,-3,null,0,-2]
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

class MinStack:

    def __init__(self):
        self.s=[]

    def push(self, val: int) -> None:
        if len(self.s)==0:
            self.s.append([val,val])
        else:
            self.s.append([val,min(val,self.s[-1][-1])])

    def pop(self) -> None:
        if len(self.s):
            self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]
        

    def getMin(self) -> int:
        return self.s[-1][-1]
