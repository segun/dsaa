import unittest
from stack import Stack

class SimpleTest(unittest.TestCase):
    def test_empty(self):
        stack = Stack(size=10)
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_full(self):
        stack = Stack(size=2)
        stack.push(1)
        self.assertFalse(stack.is_full())
        stack.push(2)
        self.assertTrue(stack.is_full)

    def test_peek(self):
        stack = Stack(size=4)
        stack.push(3)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        stack.push(4)
        self.assertEqual(stack.peek(), 4)
        stack.push(1)
        self.assertEqual(stack.peek(), 1)

    def test_pop(self):
        stack = Stack(size=10)
        stack.push(3)
        stack.push(2)
        data = stack.pop()
        self.assertEqual(data, 2)
        self.assertFalse(stack.is_empty())
        data = stack.pop()
        self.assertEqual(data, 3)
        self.assertTrue(stack.is_empty())

if __name__ == '__main__':
    unittest.main()
