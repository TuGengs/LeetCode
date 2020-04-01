# 最小栈
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

class MinStack:

    # 辅助栈和数据栈不同步
    # 关键 1：辅助栈的元素空的时候，必须放入新进来的数
    # 关键 2：新来的数小于或者等于辅助栈栈顶元素的时候，才放入（特别注意这里等于要考虑进去）
    # 关键 3：出栈的时候，辅助栈的栈顶元素等于数据栈的栈顶元素，才出栈，即"出栈保持同步"就可以了

    # 辅助栈和数据栈同步
    def __init__(self):
        # 数据栈
        self.data = []
        # 辅助栈
        self.helper = []

    def push(self, x):
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self):
        if self.data:
            self.helper.pop()
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def getMin(self):
        if self.helper:
            return self.helper[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(1)
# obj.push(2)
# obj.push(3)
# obj.push(5)
# obj.push(4)
# print(obj.helper)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()