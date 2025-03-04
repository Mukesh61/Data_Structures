'''
FIFO : first in first out.

1.	Put: put to the queue. 
2.	Pop: return first person added to the queue.
3.	Is_empty: is queue empty. 

'''

class Queue:
    def __init__(self):
        self._internal_list = []

    def put(self, item):
        self._internal_list.append(item)

    def is_empty(self):
        return len(self._internal_list) == 0

    def pop(self):
        if not self.is_empty():
            item = self._internal_list[0]
            self._internal_list = self._internal_list[1:]
            return item

if __name__ == '__main__':
    queue_obj = Queue()
    queue_obj.put(1)
    queue_obj.put(2)
    queue_obj.put(3)
