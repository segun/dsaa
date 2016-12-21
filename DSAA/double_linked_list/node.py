class Node(object):
    def __init__(self, key=None, data=None, next=None, prev=None):
        self.data = data
        self.key = key
        self.next = next
        self.prev = prev
