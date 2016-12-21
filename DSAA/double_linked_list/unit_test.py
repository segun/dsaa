import unittest
from linked_list import LinkedList

class SimplisticTest(unittest.TestCase):

    def test_insert_first(self):
        list = LinkedList(head=None)
        list.insert_first(2, 20)
        list.insert_last(3, 30)
        self.assertEqual(list.head.key, 2)
        self.assertEqual(list.head.data, 20)
        self.assertEqual(list.last.key, 3)
        self.assertEqual(list.last.data, 30)
        self.assertEqual(list.head.next.data, list.last.data)
        self.assertEqual(list.last.prev.data, list.head.data)

    def test_insert_last(self):
        list = LinkedList(head=None)
        list.insert_first(2, 20)
        list.insert_last(3, 30)
        self.assertEqual(list.head.key, 2)
        self.assertEqual(list.head.data, 20)
        self.assertEqual(list.last.key, 3)
        self.assertEqual(list.last.data, 30)
        self.assertEqual(list.head.next, list.last)
        self.assertEqual(list.last.prev, list.head)

    def test_delete_first(self):
        list = LinkedList(head=None)
        list.insert_first(2, 20)
        list.insert_last(3, 30)
        list.delete_first()
        self.assertEqual(list.head.key, 3)
        self.assertEqual(list.head.data, 30)
        self.assertEqual(list.last.key, 3)
        self.assertEqual(list.last.data, 30)

    def test_delete_last(self):
        list = LinkedList(head=None)
        list.insert_last(2, 20)
        list.insert_first(3, 30)
        list.delete_last()
        self.assertEqual(list.head.key, 3)
        self.assertEqual(list.head.data, 30)
        self.assertEqual(list.last.key, 3)
        self.assertEqual(list.last.data, 30)

    def test_size(self):
        list = LinkedList(head=None)
        list.insert_first(1,1)
        list.insert_first(1,1)
        list.insert_first(1,1)
        self.assertEqual(list.size(), 3)

    def test_find(self):
        list = LinkedList(head=None)
        list.insert_last(4, 40)
        list.insert_first(2, 20)
        list.insert_first(3, 30)
        found = list.find(2)
        self.assertEqual(found.key, 2)
        self.assertEqual(found.data, 20)

    def test_delete(self):
        list = LinkedList(head=None)
        list.insert_last(4, 40)
        list.insert_first(2, 20)
        list.insert_first(3, 30)
        deleted = list.delete(2)
        self.assertEqual(deleted.key, 2)
        self.assertEqual(deleted.data, 20)
        self.assertEqual(list.head.key, 3)
        self.assertEqual(list.head.data, 30)
        self.assertEqual(list.last.key, 4)
        self.assertEqual(list.last.data, 40)
        self.assertEqual(list.head.next, list.last)
        self.assertEqual(list.last.prev, list.head)

    def test_insert_before(self):
        list = LinkedList(head=None)
        list.insert_last(4, 40)
        list.insert_first(2, 20)
        list.insert_first(3, 30)
        list.insert_before(3, 1, 10)
        self.assertEqual(list.head.key, 1)
        self.assertEqual(list.head.data, 10)
        self.assertEqual(list.head.next.key, 3)

    def test_insert_after(self):
        list = LinkedList(head=None)
        list.insert_last(4, 40)
        list.insert_first(2, 20)
        list.insert_first(3, 30)
        list.insert_after(3, 1, 10)
        self.assertEqual(list.head.key, 3)
        self.assertEqual(list.head.data, 30)
        self.assertEqual(list.head.next.key, 1)
        self.assertEqual(list.head.next.data, 10)


if __name__ == '__main__':
    unittest.main()
