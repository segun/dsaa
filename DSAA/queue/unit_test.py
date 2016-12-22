import unittest
from queue import Queue

class SimpleTest(unittest.TestCase):
    def test_empty(self):
        queue = Queue(size=2)
        self.assertTrue(queue.is_empty())
        queue.enqueue(10)
        self.assertFalse(queue.is_empty())
        queue.enqueue(20)
        self.assertFalse(queue.is_empty())
        queue.dequeue()
        queue.dequeue()
        self.assertTrue(queue.is_empty())



    def test_full(self):
        queue = Queue(size=2)
        self.assertFalse(queue.is_full())
        queue.enqueue(2)
        queue.enqueue(4)
        self.assertTrue(queue.is_full())
        queue.dequeue()
        queue.dequeue()
        self.assertFalse(queue.is_full())
        queue.enqueue(2)
        queue.enqueue(4)
        self.assertTrue(queue.is_full())

    def test_peek(self):
        queue = Queue(2)
        queue.enqueue(2)
        queue.enqueue(4)
        self.assertEqual(2, queue.peek())

    def test_dequeue(self):
        queue = Queue(2)
        queue.enqueue(2)
        queue.enqueue(4)
        self.assertTrue(queue.is_full())
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 4)
        self.assertTrue(queue.is_empty())

if __name__ == '__main__':
    unittest.main()
