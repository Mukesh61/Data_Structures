"""
A node should have data, left node and right node. 
"""
class Node:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def __str__(self):
        return f"Node Value: {self._data}"


node_10 = Node(10)
node_15 = Node(15)
node_05 = Node(5)

node_10._right = node_15
node_10._left = node_05

print(node_10)
print(node_10._left)
print(node_10._right)
