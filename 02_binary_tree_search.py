class Node:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def search(self, target):
        if self._data == target:
            return self
        elif self._left and target < self._data:
            return self._left.search(target)
        elif self._right and target > self._data:
            return self._right.search(target)

        print("Data not found")

    def __str__(self):
        return f"Node Value: {self._data}"


root = Node(10)
node_15 = Node(15)
node_05 = Node(5)
node_01 = Node(1)

root._right = node_15
root._left = node_05
node_05._left = node_01

target = root.search(1)

if target:
    print("Value found")
    print(target)
