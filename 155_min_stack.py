'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
Methods pop, top and getMin operations will always be called on non-empty stacks.
'''
class MinStack:
    def __init__(self):
        self.s = []
        self.min = float('inf')
        self.size = 0

    def push(self, x: int) -> None:
        self.s.insert(0, x)
        self.size = self.size + 1
        if x < self.min:
            self.min = x

    def pop(self) -> None:
        if self.size:
            p = self.s.pop(0)
            self.size = self.size - 1
            if self.size:
                self.min = min(self.s)
            else:
                self.min = float('inf')

    def top(self) -> int:
        if self.size:
            return self.s[0]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()