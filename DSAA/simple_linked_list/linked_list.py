from node import Node

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        current = self.head
        printed = "[ "
        while current is not None:
            printed += "({}:{}), ".format(current.get_key(), current.get_data())
            current = current.get_next()

        printed = printed[0:printed.rindex(",")]
        printed += " ]"
        print printed

    def insert_first(self, key, data):
        new_node = Node(key=key, data=data)
        new_node.set_next(self.head)
        self.head = new_node

    def delete_first(self):
        current = self.head
        head = head.get_next()
        return current

    def size(self):
        lenght = 0
        current = self.head
        while current is not None:
            lenght = lenght + 1
            current = current.get_next()
        return lenght

    def find(self, key):
        current = self.head
        found = False
        while current and found is False:
            if current.get_key() == key:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Key Is Not In List")
        else:
            return current

    def delete(self, key):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_key() == key:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Key Is Not In List")
        else:
            previous.set_next(current.get_next())
            return current

    def insert_after(self, after_key, key, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_key() == after_key:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Key Is Not In List")
        else:
            new_node = Node(key=key, data=data)
            new_node.set_next(current.get_next())
            current.set_next(new_node)

    def insert_before(self, before_key, key, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_key() == before_key:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Key Is Not In List")
        else:
            if previous is None:
                self.insert_first(key, data)
            else:
                new_node = Node(key=key, data=data)
                new_node.set_next(previous.get_next())
                previous.set_next(new_node)

    def reverse(self):
        current = self.head
        previous = None
        next = current.get_next()

        while current is not None:
            next = current.get_next()
            current.set_next(previous)
            previous = current
            current = next

        self.head = previous
