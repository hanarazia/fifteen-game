class PQueue:
    def __init__(self):
        self.values = [] 

    def __str__(self):
        return str(self.values)

    def empty(self):
        return len(self.values) == 0

    def enqueue(self, value):
        if value > value - 1:
            self.values.append(value)
            max_val = max(self.values)
            if value < max_val:
                self.values.remove(max_val)
                if value not in self.values:
                    self.values.append(value)
                self.values.append(max_val)
            return self.values

    def dequeue(self):
        return self.values.pop()
    
if __name__ == '__main__':
    pq = PQueue()
    data = [1, 3, 5, 2, 0, 6, 4]
    for i in data:
        pq.enqueue(i)
        print(pq)
        
    while not pq.empty():
        pq.dequeue()
        print(pq)