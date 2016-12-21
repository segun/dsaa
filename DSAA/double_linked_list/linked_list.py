from node import Node

class LinkedList(object):
    def __init__(self, head=None, last=None):
        self.head = head
        self.last = last

    def print_forward(self):
        current = self.head
        printed = "[ "
        while current is not None:
            printed += "({}:{}), ".format(current.key, current.data)
            current = current.next

        printed = printed[0:printed.rindex(",")]
        printed += " ]"
        print printed

    def print_backward(self):
        current = self.last
        printed = "[ "
        while current != None:
            printed += "({}:{}), ".format(current.key, current.data)
            current = current.prev

        printed = printed[0:printed.rindex(",")]
        printed += " ]"
        print printed

    def insert_first(self, key, data):
        new_node = Node(key=key, data=data)
        new_node.next = self.head
        new_node.prev = None
        if self.last is None:
            self.last = new_node
        else:
            self.head.prev = new_node
        self.head = new_node

    def insert_last(self, key, data):
        new_node = Node(key=key, data=data)
        new_node.next = None
        new_node.prev = self.last
        if self.head is None:
            self.head = new_node
        else:
            self.last.next = new_node
        self.last = new_node

    def delete_first(self):
        self.head = self.head.next
        self.head.prev = None

    def delete_last(self):
        self.last = self.last.prev
        self.last.next = None

    def size(self):
        lenght = 0
        current = self.head
        while current is not None:
            lenght = lenght + 1
            current = current.next
        return lenght

    def find(self, key):
        current = self.head
        found = False
        while current and found is False:
            if current.key == key:
                found = True
            else:
                current = current.next
        if current is None:
            raise ValueError("Key Is Not In List")
        else:
            return current

    def delete(self, key):
        current = self.head
        previous = None
        next = None
        found = False
        while current and found is False:
            if current.key == key:
                found = True
            else:
                previous = current
                current = current.next
        if current is None:
            raise ValueError("Key Is Not In List")
        else:
            if previous is None:
                #Means we are at head
                self.delete_first()
            elif current.next is None:
                #Means we are at last
                self.delete_last()
            else:
                next = current.next
                previous.next = next
                current.prev = None
                next.prev = previous
                current.next = None
            return current

    def insert_after(self, after_key, key, data):
        current = self.head
        found = False
        while current and found is False:
            if current.key == after_key:
                found = True
            else:
                current = current.next
        if current is None:
            raise ValueError("Key Is Not In List")
        else:
            next = current.next
            if next is None:
                #We are last
                self.insert_last(key, data)
            else:
                new_node = Node(key=key, data=data)
                new_node.next = next
                next.prev = new_node
                current.next = new_node
                new_node.prev = current

    def insert_before(self, before_key, key, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.key == before_key:
                found = True
            else:
                previous = current
                current = current.next
        if current is None:
            raise ValueError("Key Is Not In List")
        else:
            if previous is None:
                #We are at head
                self.insert_first(key, data)
            else:
                new_node = Node(key=key, data=data)
                new_node.next = previous.next
                previous.next = new_node
                current.prev = new_node
                new_node.prev = previous
