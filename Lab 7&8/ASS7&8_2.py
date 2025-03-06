class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"add :{item}")
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue:", " <- ".join(map(str, self.queue)))
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print(f" remove : {q.dequeue()}")
q.display()
