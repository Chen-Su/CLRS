class Queue:
    """模拟队列"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        else:
            print("Queue is empty.")

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
print(q.items)