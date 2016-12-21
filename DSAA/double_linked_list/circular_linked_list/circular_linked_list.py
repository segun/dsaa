from linked_list import LinkedList

class CircularLinkedLink(LinkedList):
    def __init__(self):
        LinkedList.__init__(head=None, last=None)
        head.prev = last.next
