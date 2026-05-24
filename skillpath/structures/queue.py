class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        if len(self.data) == 0:
            return None

        data = self.data[0]
        del self.data[0]

        return data