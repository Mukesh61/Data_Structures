'''
insert and delete from top of the stack. 

LIFO : last in first out

1. push
2. pop
3. peek: return top item without deleting it. like just to check
4. is_empty: return true if the stack is empty. 

Usage: 
1. Syntax parsing
2. used in recursion
3. Undo and redo operations in word processors. 
4. low level assembly programming. 

'''

class CustomStack:
    def __init__(self):
        self._internal_list = []

    def is_empty(self):
        if not len(self._internal_list):
            return True
        return False

    def push(self, item):
        self._internal_list.append(item)

    def pop(self):
        return self._internal_list.pop()

    def peek(self):
        if not self.is_empty():
            return self._internal_list[-1]


if __name__ == '__main__':
    stack = CustomStack()

    print(stack.is_empty())

    print("add 1 and 2 to stack")
    stack.push(1)
    stack.push(2)

    print("peek the item")
    print(stack.peek())

    print("remove one item")
    print(stack.pop())

