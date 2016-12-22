class Queue(object):
    def __init__(self, size=0):
        self.queue = []
        self.front = 0
        self.rear = -1
        self.size = size

    def is_empty(self):
        return self.rear == -1

    def is_full(self):
        return self.rear + 1 == self.size

    def enqueue(self, data):
        if self.is_full():
            raise ValueError("Queue is full.")
        else:
            self.rear = self.rear + 1
            self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")
        else:
            data = self.queue[self.front]
            if self.front + 1 > self.rear:
                #At this point the queue is empty, reset
                self.front = 0
                self.rear = -1
                self.queue = []
            else:
                self.front = self.front + 1
            return data

    def peek(self):
        return self.queue[self.front]
