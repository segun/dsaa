class Node(object):
    def __init__(self, key=None, data=None, next=None):
        self.data = data
        self.key = key
        self.next = next

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key
        
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next
