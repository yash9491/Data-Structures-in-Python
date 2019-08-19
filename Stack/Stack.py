class Stack:
    stack_list = []
    def InsertIntoStack(self, data):

        if len(self.stack_list) == 0:
            self.stack_list.insert(1, data)
        else:
            self.stack_list.append(data)
    
    def printstack(self):
        print(self.stack_list)

    def RemoveFromStack(self):
        self.stack_list.pop()

if __name__ == '__main__':
    
    stk = Stack()
    stk.InsertIntoStack("Hii")
    stk.InsertIntoStack("Hiiii")
    stk.InsertIntoStack("Hello")
    stk.printstack()
    stk.RemoveFromStack()
    stk.printstack()